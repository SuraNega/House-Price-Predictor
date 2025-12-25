# House Price Prediction - AI Project

A machine learning project that predicts house prices using the Kaggle "House Prices - Advanced Regression Techniques" dataset. This project compares two regression algorithms and provides a user-friendly web interface for making predictions.

## 🎯 Project Overview

**Problem**: Predict house sale prices based on various features like area, quality, location, and amenities.

**Dataset**: [Kaggle - House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)

**Algorithms Compared**:
1. **Ridge Regression** - Linear model with L2 regularization
2. **Random Forest Regressor** - Ensemble of decision trees

## 📁 Project Structure

```
project/
├── data/                          # Dataset files
│   ├── train.csv                  # Training data
│   ├── test.csv                   # Test data
│   └── data_description.txt       # Feature descriptions
├── src/                           # Source code
│   ├── data_preprocessing.py      # Data cleaning and preparation
│   ├── train_models.py           # Model training and comparison
│   └── predict.py                # Prediction pipeline
├── models/                        # Saved models and results
│   ├── best_model.pkl            # Best performing model
│   ├── ridge_regression.pkl      # Ridge model
│   ├── random_forest.pkl         # Random Forest model
│   ├── scaler.pkl                # Feature scaler
│   ├── label_encoders.pkl        # Categorical encoders
│   └── training_results.pkl      # Performance metrics
├── notebooks/                     # Jupyter notebooks (optional)
├── app.py                        # Streamlit web interface
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd "E:/Class/3rd year/1st semester/AI/project"
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Step 1: Train the Models

Run the training script to preprocess data, train both algorithms, and compare their performance:

```bash
python src/train_models.py
```

This will:
- Load and preprocess the data
- Train Ridge Regression and Random Forest models
- Perform hyperparameter tuning
- Compare model performance
- Save the best model and results

**Expected Output**:
- Trained models saved in `models/` directory
- Performance comparison printed to console
- Comparison chart saved as `models/model_comparison.png`

#### Step 2: Launch the Web Interface

Start the Streamlit web application:

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

#### Step 3: Make Predictions

1. Enter house details in the web interface
2. Click "Predict House Price"
3. View the predicted price and confidence interval

## 📊 Model Performance

The models are evaluated using three key metrics:

- **RMSE (Root Mean Squared Error)**: Measures average prediction error in dollars
- **MAE (Mean Absolute Error)**: Average absolute difference between predicted and actual prices
- **R² Score**: Proportion of variance explained by the model (0-1, higher is better)

After training, you can view detailed comparison in:
- Console output from `train_models.py`
- Web interface "Model Comparison" tab
- `models/model_comparison.png` chart

## 🎨 Web Interface Features

The Streamlit application includes:

1. **Predict Price Tab**
   - Input form for house features
   - Real-time price prediction
   - Confidence interval display
   - Key metrics (price per sq ft, total area, etc.)

2. **Model Comparison Tab**
   - Performance metrics table
   - Visual comparison charts
   - Metrics explanation

3. **How to Use Tab**
   - Quick start guide
   - Input fields explanation
   - Troubleshooting tips

## 🔬 Algorithms Explained

### Ridge Regression
- **Type**: Linear regression with L2 regularization
- **Pros**: Fast, interpretable, works well with linear relationships
- **Cons**: May underperform with complex non-linear patterns
- **Best for**: Understanding feature importance and linear trends

### Random Forest Regressor
- **Type**: Ensemble of decision trees
- **Pros**: Handles non-linearity, robust to outliers, provides feature importance
- **Cons**: Slower training, less interpretable
- **Best for**: Capturing complex relationships in data

## 📈 Key Features

### Data Preprocessing
- Handles missing values intelligently
- Encodes categorical variables
- Scales numerical features
- Creates engineered features (TotalSF, TotalBath, HouseAge, etc.)

### Model Training
- Automated hyperparameter tuning using GridSearchCV
- Cross-validation for robust evaluation
- Saves best model automatically

### Prediction Pipeline
- Loads trained model and preprocessors
- Handles new input data
- Provides confidence intervals (for Random Forest)

## 🛠️ Technical Details

### Dependencies
- **pandas**: Data manipulation
- **numpy**: Numerical operations
- **scikit-learn**: Machine learning algorithms
- **matplotlib & seaborn**: Visualization
- **streamlit**: Web interface
- **joblib**: Model persistence

### Data Processing Steps
1. Load training and test data
2. Handle missing values (median for numerical, mode for categorical)
3. Feature engineering (create TotalSF, TotalBath, HouseAge, IsRemodeled)
4. Encode categorical variables (Label Encoding)
5. Scale numerical features (StandardScaler)
6. Split into training and validation sets (80/20)

### Model Training Steps
1. Define hyperparameter grids
2. Perform grid search with cross-validation
3. Train models with best parameters
4. Evaluate on validation set
5. Compare performance metrics
6. Select and save best model

## 📝 Example Prediction

```python
from src.predict import HousePricePredictor

# Load predictor
predictor = HousePricePredictor()

# Sample house data
house = {
    'OverallQual': 7,
    'GrLivArea': 1500,
    'YearBuilt': 2000,
    'FullBath': 2,
    # ... other features
}

# Make prediction
result = predictor.predict_with_confidence(house)
print(f"Predicted Price: ${result['prediction']:,.2f}")
```

## 🎓 For Instructors

This project demonstrates:

✅ **Problem Selection**: Real-world regression problem from Kaggle  
✅ **Data Preprocessing**: Comprehensive data cleaning and feature engineering  
✅ **Algorithm Comparison**: Two different ML approaches (linear vs. tree-based)  
✅ **Model Evaluation**: Multiple metrics (RMSE, MAE, R²)  
✅ **Best Model Selection**: Data-driven decision based on validation performance  
✅ **User Interface**: Professional web application for predictions  
✅ **Documentation**: Complete README and code comments  

## 🐛 Troubleshooting

**Issue**: `ModuleNotFoundError`  
**Solution**: Install dependencies with `pip install -r requirements.txt`

**Issue**: `FileNotFoundError: models/best_model.pkl`  
**Solution**: Train the models first with `python src/train_models.py`

**Issue**: Web app shows "Model not found"  
**Solution**: Ensure you've run the training script before launching the app

**Issue**: Predictions seem unrealistic  
**Solution**: Check input values are reasonable and within training data range

## 📚 Additional Resources

- [Kaggle Competition](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)

## 🙏 Acknowledgments

- Dataset: Kaggle House Prices Competition
- Libraries: Scikit-learn, Streamlit, Pandas, NumPy

---

**Author**: AI Project - House Price Prediction  
**Date**: December 2025  
**Course**: 3rd Year, 1st Semester - AI
