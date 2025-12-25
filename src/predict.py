"""
Prediction Module
Load trained model and make predictions on new data
"""

import pandas as pd
import numpy as np
import joblib


class HousePricePredictor:
    """Make predictions using trained model"""
    
    def __init__(self, model_path='models/best_model.pkl'):
        """Load trained model and preprocessors"""
        print("Loading model and preprocessors...")
        self.model = joblib.load(model_path)
        self.scaler = joblib.load('models/scaler.pkl')
        self.label_encoders = joblib.load('models/label_encoders.pkl')
        self.feature_names = joblib.load('models/feature_names.pkl')
        print("✅ Model loaded successfully!")
    
    def preprocess_input(self, input_data):
        """Preprocess input data for prediction"""
        # Convert to DataFrame if dict
        if isinstance(input_data, dict):
            input_data = pd.DataFrame([input_data])
        
        # Handle missing values
        numerical_cols = input_data.select_dtypes(include=[np.number]).columns
        for col in numerical_cols:
            if input_data[col].isnull().sum() > 0:
                input_data[col].fillna(input_data[col].median(), inplace=True)
        
        categorical_cols = input_data.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            if input_data[col].isnull().sum() > 0:
                input_data[col].fillna('None', inplace=True)
        
        # Feature engineering
        input_data['TotalSF'] = input_data['TotalBsmtSF'] + input_data['1stFlrSF'] + input_data['2ndFlrSF']
        input_data['TotalBath'] = (input_data['FullBath'] + 0.5 * input_data['HalfBath'] + 
                                   input_data['BsmtFullBath'] + 0.5 * input_data['BsmtHalfBath'])
        input_data['HouseAge'] = input_data['YrSold'] - input_data['YearBuilt']
        input_data['IsRemodeled'] = (input_data['YearRemodAdd'] != input_data['YearBuilt']).astype(int)
        
        # Encode categorical variables
        for col in categorical_cols:
            if col in self.label_encoders:
                le = self.label_encoders[col]
                input_data[col] = input_data[col].astype(str).apply(
                    lambda x: le.transform([x])[0] if x in le.classes_ else -1
                )
        
        # Drop ID if exists
        if 'Id' in input_data.columns:
            input_data = input_data.drop('Id', axis=1)
        
        # Ensure same features as training
        for col in self.feature_names:
            if col not in input_data.columns:
                input_data[col] = 0
        
        input_data = input_data[self.feature_names]
        
        # Scale
        input_scaled = self.scaler.transform(input_data)
        
        return input_scaled
    
    def predict(self, input_data):
        """Make prediction on input data"""
        # Preprocess
        X = self.preprocess_input(input_data)
        
        # Predict
        prediction = self.model.predict(X)
        
        return prediction[0]
    
    def predict_with_confidence(self, input_data):
        """Make prediction with confidence interval (for Random Forest)"""
        X = self.preprocess_input(input_data)
        
        # Main prediction
        prediction = self.model.predict(X)[0]
        
        # If Random Forest, get predictions from all trees
        if hasattr(self.model, 'estimators_'):
            tree_predictions = np.array([tree.predict(X)[0] for tree in self.model.estimators_])
            std = np.std(tree_predictions)
            lower_bound = prediction - 1.96 * std
            upper_bound = prediction + 1.96 * std
            
            return {
                'prediction': prediction,
                'lower_bound': max(0, lower_bound),
                'upper_bound': upper_bound,
                'confidence_interval': (lower_bound, upper_bound)
            }
        else:
            return {
                'prediction': prediction,
                'lower_bound': None,
                'upper_bound': None
            }


if __name__ == "__main__":
    # Example usage
    predictor = HousePricePredictor()
    
    # Sample house data
    sample_house = {
        'MSSubClass': 60,
        'MSZoning': 'RL',
        'LotArea': 8450,
        'Street': 'Pave',
        'LotShape': 'Reg',
        'LandContour': 'Lvl',
        'Utilities': 'AllPub',
        'LotConfig': 'Inside',
        'LandSlope': 'Gtl',
        'Neighborhood': 'CollgCr',
        'Condition1': 'Norm',
        'Condition2': 'Norm',
        'BldgType': '1Fam',
        'HouseStyle': '2Story',
        'OverallQual': 7,
        'OverallCond': 5,
        'YearBuilt': 2003,
        'YearRemodAdd': 2003,
        'RoofStyle': 'Gable',
        'RoofMatl': 'CompShg',
        'Exterior1st': 'VinylSd',
        'Exterior2nd': 'VinylSd',
        'MasVnrType': 'BrkFace',
        'MasVnrArea': 196,
        'ExterQual': 'Gd',
        'ExterCond': 'TA',
        'Foundation': 'PConc',
        'BsmtQual': 'Gd',
        'BsmtCond': 'TA',
        'BsmtExposure': 'No',
        'BsmtFinType1': 'GLQ',
        'BsmtFinSF1': 706,
        'BsmtFinType2': 'Unf',
        'BsmtFinSF2': 0,
        'BsmtUnfSF': 150,
        'TotalBsmtSF': 856,
        'Heating': 'GasA',
        'HeatingQC': 'Ex',
        'CentralAir': 'Y',
        'Electrical': 'SBrkr',
        '1stFlrSF': 856,
        '2ndFlrSF': 854,
        'LowQualFinSF': 0,
        'GrLivArea': 1710,
        'BsmtFullBath': 1,
        'BsmtHalfBath': 0,
        'FullBath': 2,
        'HalfBath': 1,
        'BedroomAbvGr': 3,
        'KitchenAbvGr': 1,
        'KitchenQual': 'Gd',
        'TotRmsAbvGrd': 8,
        'Functional': 'Typ',
        'Fireplaces': 0,
        'GarageType': 'Attchd',
        'GarageYrBlt': 2003,
        'GarageFinish': 'RFn',
        'GarageCars': 2,
        'GarageArea': 548,
        'GarageQual': 'TA',
        'GarageCond': 'TA',
        'PavedDrive': 'Y',
        'WoodDeckSF': 0,
        'OpenPorchSF': 61,
        'EnclosedPorch': 0,
        '3SsnPorch': 0,
        'ScreenPorch': 0,
        'PoolArea': 0,
        'MiscVal': 0,
        'MoSold': 2,
        'YrSold': 2008,
        'SaleType': 'WD',
        'SaleCondition': 'Normal'
    }
    
    result = predictor.predict_with_confidence(sample_house)
    print(f"\nPredicted Price: ${result['prediction']:,.2f}")
    if result['lower_bound']:
        print(f"95% Confidence Interval: ${result['lower_bound']:,.2f} - ${result['upper_bound']:,.2f}")
