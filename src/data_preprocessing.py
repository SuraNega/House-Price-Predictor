"""
Data Preprocessing Module
Handles data loading, cleaning, and feature engineering for house price prediction
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib


class HousePricePreprocessor:
    """Preprocessor for house price data"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.feature_names = None
        
    def load_data(self, train_path='train.csv', test_path='test.csv'):
        """Load training and test data"""
        print("Loading data...")
        self.train_df = pd.read_csv(train_path)
        self.test_df = pd.read_csv(test_path)
        print(f"Train data shape: {self.train_df.shape}")
        print(f"Test data shape: {self.test_df.shape}")
        return self.train_df, self.test_df
    
    def explore_data(self):
        """Basic data exploration"""
        print("\n=== DATA EXPLORATION ===")
        print("\nFirst few rows:")
        print(self.train_df.head())
        
        print("\nData Info:")
        print(self.train_df.info())
        
        print("\nMissing Values:")
        missing = self.train_df.isnull().sum()
        missing = missing[missing > 0].sort_values(ascending=False)
        print(missing)
        
        print("\nTarget Variable (SalePrice) Statistics:")
        print(self.train_df['SalePrice'].describe())
        
        return missing
    
    def handle_missing_values(self, df):
        """Handle missing values in the dataset"""
        # Numerical features - fill with median
        numerical_cols = df.select_dtypes(include=[np.number]).columns
        for col in numerical_cols:
            if df[col].isnull().sum() > 0:
                df[col].fillna(df[col].median(), inplace=True)
        
        # Categorical features - fill with mode or 'None'
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            if df[col].isnull().sum() > 0:
                df[col].fillna(df[col].mode()[0] if len(df[col].mode()) > 0 else 'None', inplace=True)
        
        return df
    
    def feature_engineering(self, df):
        """Create new features from existing ones"""
        # Total square footage
        df['TotalSF'] = df['TotalBsmtSF'] + df['1stFlrSF'] + df['2ndFlrSF']
        
        # Total bathrooms
        df['TotalBath'] = df['FullBath'] + 0.5 * df['HalfBath'] + df['BsmtFullBath'] + 0.5 * df['BsmtHalfBath']
        
        # Age of house
        df['HouseAge'] = df['YrSold'] - df['YearBuilt']
        
        # Remodeled or not
        df['IsRemodeled'] = (df['YearRemodAdd'] != df['YearBuilt']).astype(int)
        
        return df
    
    def encode_categorical(self, df, is_training=True):
        """Encode categorical variables"""
        categorical_cols = df.select_dtypes(include=['object']).columns
        
        for col in categorical_cols:
            if is_training:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col].astype(str))
                self.label_encoders[col] = le
            else:
                if col in self.label_encoders:
                    # Handle unseen categories
                    le = self.label_encoders[col]
                    df[col] = df[col].astype(str).apply(
                        lambda x: le.transform([x])[0] if x in le.classes_ else -1
                    )
        
        return df
    
    def prepare_features(self, df, is_training=True):
        """Prepare features for modeling"""
        # Handle missing values
        df = self.handle_missing_values(df)
        
        # Feature engineering
        df = self.feature_engineering(df)
        
        # Encode categorical variables
        df = self.encode_categorical(df, is_training)
        
        # Drop ID column if exists
        if 'Id' in df.columns:
            df = df.drop('Id', axis=1)
        
        return df
    
    def preprocess(self, save_preprocessor=True):
        """Complete preprocessing pipeline"""
        print("\n=== PREPROCESSING DATA ===")
        
        # Separate target variable
        y = self.train_df['SalePrice'].copy()
        X = self.train_df.drop('SalePrice', axis=1)
        
        # Prepare features
        X = self.prepare_features(X, is_training=True)
        
        # Store feature names
        self.feature_names = X.columns.tolist()
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        X = pd.DataFrame(X_scaled, columns=X.columns)
        
        # Split data
        X_train, X_val, y_train, y_val = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        print(f"Training set: {X_train.shape}")
        print(f"Validation set: {X_val.shape}")
        
        # Save preprocessor
        if save_preprocessor:
            joblib.dump(self.scaler, 'models/scaler.pkl')
            joblib.dump(self.label_encoders, 'models/label_encoders.pkl')
            joblib.dump(self.feature_names, 'models/feature_names.pkl')
            print("\nPreprocessor saved!")
        
        return X_train, X_val, y_train, y_val
    
    def preprocess_test_data(self):
        """Preprocess test data using saved preprocessor"""
        X_test = self.prepare_features(self.test_df.copy(), is_training=False)
        
        # Ensure same features as training
        for col in self.feature_names:
            if col not in X_test.columns:
                X_test[col] = 0
        
        X_test = X_test[self.feature_names]
        
        # Scale
        X_test_scaled = self.scaler.transform(X_test)
        X_test = pd.DataFrame(X_test_scaled, columns=self.feature_names)
        
        return X_test


if __name__ == "__main__":
    # Example usage
    preprocessor = HousePricePreprocessor()
    preprocessor.load_data()
    preprocessor.explore_data()
    X_train, X_val, y_train, y_val = preprocessor.preprocess()
    
    print("\n✅ Preprocessing completed successfully!")
