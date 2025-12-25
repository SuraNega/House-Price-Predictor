"""
Model Training Module
Trains Ridge Regression and Random Forest models and compares their performance
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import HousePricePreprocessor
import time


class ModelTrainer:
    """Train and compare multiple regression models"""
    
    def __init__(self):
        self.models = {}
        self.results = {}
        self.best_model = None
        self.best_model_name = None
        
    def train_ridge_regression(self, X_train, y_train, X_val, y_val):
        """Train Ridge Regression with hyperparameter tuning"""
        print("\n=== TRAINING RIDGE REGRESSION ===")
        
        # Hyperparameter grid
        param_grid = {
            'alpha': [0.001, 0.01, 0.1, 1, 10, 100, 1000]
        }
        
        # Grid search with cross-validation
        ridge = Ridge(random_state=42)
        grid_search = GridSearchCV(
            ridge, param_grid, cv=5, 
            scoring='neg_mean_squared_error',
            n_jobs=-1, verbose=1
        )
        
        start_time = time.time()
        grid_search.fit(X_train, y_train)
        training_time = time.time() - start_time
        
        # Best model
        best_ridge = grid_search.best_estimator_
        print(f"Best parameters: {grid_search.best_params_}")
        print(f"Training time: {training_time:.2f} seconds")
        
        # Predictions
        y_pred_train = best_ridge.predict(X_train)
        y_pred_val = best_ridge.predict(X_val)
        
        # Evaluate
        results = self.evaluate_model(y_train, y_pred_train, y_val, y_pred_val, "Ridge Regression")
        results['training_time'] = training_time
        results['best_params'] = grid_search.best_params_
        
        self.models['Ridge Regression'] = best_ridge
        self.results['Ridge Regression'] = results
        
        return best_ridge, results
    
    def train_random_forest(self, X_train, y_train, X_val, y_val):
        """Train Random Forest with hyperparameter tuning"""
        print("\n=== TRAINING RANDOM FOREST ===")
        
        # Hyperparameter grid
        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [10, 20, 30, None],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }
        
        # Grid search with cross-validation
        rf = RandomForestRegressor(random_state=42, n_jobs=-1)
        grid_search = GridSearchCV(
            rf, param_grid, cv=3,  # Using 3-fold CV to save time
            scoring='neg_mean_squared_error',
            n_jobs=-1, verbose=1
        )
        
        start_time = time.time()
        grid_search.fit(X_train, y_train)
        training_time = time.time() - start_time
        
        # Best model
        best_rf = grid_search.best_estimator_
        print(f"Best parameters: {grid_search.best_params_}")
        print(f"Training time: {training_time:.2f} seconds")
        
        # Predictions
        y_pred_train = best_rf.predict(X_train)
        y_pred_val = best_rf.predict(X_val)
        
        # Evaluate
        results = self.evaluate_model(y_train, y_pred_train, y_val, y_pred_val, "Random Forest")
        results['training_time'] = training_time
        results['best_params'] = grid_search.best_params_
        
        self.models['Random Forest'] = best_rf
        self.results['Random Forest'] = results
        
        return best_rf, results
    
    def evaluate_model(self, y_train, y_pred_train, y_val, y_pred_val, model_name):
        """Evaluate model performance"""
        print(f"\n--- {model_name} Performance ---")
        
        # Training metrics
        train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
        train_mae = mean_absolute_error(y_train, y_pred_train)
        train_r2 = r2_score(y_train, y_pred_train)
        
        # Validation metrics
        val_rmse = np.sqrt(mean_squared_error(y_val, y_pred_val))
        val_mae = mean_absolute_error(y_val, y_pred_val)
        val_r2 = r2_score(y_val, y_pred_val)
        
        print(f"Training RMSE: ${train_rmse:,.2f}")
        print(f"Training MAE: ${train_mae:,.2f}")
        print(f"Training R²: {train_r2:.4f}")
        print(f"\nValidation RMSE: ${val_rmse:,.2f}")
        print(f"Validation MAE: ${val_mae:,.2f}")
        print(f"Validation R²: {val_r2:.4f}")
        
        return {
            'train_rmse': train_rmse,
            'train_mae': train_mae,
            'train_r2': train_r2,
            'val_rmse': val_rmse,
            'val_mae': val_mae,
            'val_r2': val_r2
        }
    
    def compare_models(self):
        """Compare all trained models"""
        print("\n=== MODEL COMPARISON ===")
        
        comparison_df = pd.DataFrame({
            'Model': list(self.results.keys()),
            'Validation RMSE': [self.results[m]['val_rmse'] for m in self.results],
            'Validation MAE': [self.results[m]['val_mae'] for m in self.results],
            'Validation R²': [self.results[m]['val_r2'] for m in self.results],
            'Training Time (s)': [self.results[m]['training_time'] for m in self.results]
        })
        
        print("\n", comparison_df.to_string(index=False))
        
        # Select best model (lowest validation RMSE)
        best_idx = comparison_df['Validation RMSE'].idxmin()
        self.best_model_name = comparison_df.loc[best_idx, 'Model']
        self.best_model = self.models[self.best_model_name]
        
        print(f"\n🏆 Best Model: {self.best_model_name}")
        print(f"   Validation RMSE: ${comparison_df.loc[best_idx, 'Validation RMSE']:,.2f}")
        
        return comparison_df
    
    def plot_comparison(self, comparison_df):
        """Create comparison visualizations"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Model Comparison', fontsize=16, fontweight='bold')
        
        # RMSE comparison
        axes[0, 0].bar(comparison_df['Model'], comparison_df['Validation RMSE'], color=['#3498db', '#e74c3c'])
        axes[0, 0].set_title('Validation RMSE (Lower is Better)')
        axes[0, 0].set_ylabel('RMSE ($)')
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # MAE comparison
        axes[0, 1].bar(comparison_df['Model'], comparison_df['Validation MAE'], color=['#3498db', '#e74c3c'])
        axes[0, 1].set_title('Validation MAE (Lower is Better)')
        axes[0, 1].set_ylabel('MAE ($)')
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # R² comparison
        axes[1, 0].bar(comparison_df['Model'], comparison_df['Validation R²'], color=['#3498db', '#e74c3c'])
        axes[1, 0].set_title('Validation R² (Higher is Better)')
        axes[1, 0].set_ylabel('R² Score')
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Training time comparison
        axes[1, 1].bar(comparison_df['Model'], comparison_df['Training Time (s)'], color=['#3498db', '#e74c3c'])
        axes[1, 1].set_title('Training Time')
        axes[1, 1].set_ylabel('Time (seconds)')
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('models/model_comparison.png', dpi=300, bbox_inches='tight')
        print("\n📊 Comparison plot saved to 'models/model_comparison.png'")
        plt.show()
    
    def save_models(self):
        """Save all trained models"""
        for name, model in self.models.items():
            filename = f"models/{name.lower().replace(' ', '_')}.pkl"
            joblib.dump(model, filename)
            print(f"✅ Saved {name} to {filename}")
        
        # Save best model separately
        joblib.dump(self.best_model, 'models/best_model.pkl')
        
        # Save results
        joblib.dump(self.results, 'models/training_results.pkl')
        
        print(f"\n🏆 Best model ({self.best_model_name}) saved as 'models/best_model.pkl'")


def main():
    """Main training pipeline"""
    print("=" * 60)
    print("HOUSE PRICE PREDICTION - MODEL TRAINING")
    print("=" * 60)
    
    # Step 1: Preprocess data
    preprocessor = HousePricePreprocessor()
    preprocessor.load_data()
    X_train, X_val, y_train, y_val = preprocessor.preprocess()
    
    # Step 2: Train models
    trainer = ModelTrainer()
    
    # Train Ridge Regression
    trainer.train_ridge_regression(X_train, y_train, X_val, y_val)
    
    # Train Random Forest
    trainer.train_random_forest(X_train, y_train, X_val, y_val)
    
    # Step 3: Compare models
    comparison_df = trainer.compare_models()
    
    # Step 4: Visualize comparison
    trainer.plot_comparison(comparison_df)
    
    # Step 5: Save models
    trainer.save_models()
    
    print("\n" + "=" * 60)
    print("✅ TRAINING COMPLETED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    main()
