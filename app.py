"""
House Price Prediction Web Application
A Streamlit-based user interface for predicting house prices
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sys
import os

# Add src to path
sys.path.append('src')
from predict import HousePricePredictor

# Page configuration
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 2rem;
    }
    .prediction-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin: 2rem 0;
    }
    .prediction-value {
        font-size: 3rem;
        font-weight: bold;
        margin: 1rem 0;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 0.75rem;
        border-radius: 10px;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🏠 House Price Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">AI-Powered Real Estate Valuation using Machine Learning</div>', unsafe_allow_html=True)

# Sidebar - Model Information
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/000000/home.png", width=150)
    st.title("📊 Model Information")
    
    try:
        # Load model results
        results = joblib.load('models/training_results.pkl')
        
        st.markdown("### 🏆 Best Model")
        # Determine best model
        best_model = min(results.items(), key=lambda x: x[1]['val_rmse'])
        st.success(f"**{best_model[0]}**")
        
        st.markdown("### 📈 Performance Metrics")
        st.metric("Validation RMSE", f"${best_model[1]['val_rmse']:,.0f}")
        st.metric("Validation R² Score", f"{best_model[1]['val_r2']:.4f}")
        st.metric("Validation MAE", f"${best_model[1]['val_mae']:,.0f}")
        
        st.markdown("---")
        st.markdown("### 🔬 Algorithms Compared")
        for model_name in results.keys():
            st.write(f"✓ {model_name}")
        
    except FileNotFoundError:
        st.warning("⚠️ Model not trained yet. Please run `train_models.py` first.")
    
    st.markdown("---")
    st.markdown("### 👨‍💻 About")
    st.info("""
    This application predicts house prices using machine learning algorithms trained on the Kaggle House Prices dataset.
    
    **Dataset**: House Prices - Advanced Regression Techniques
    """)

# Main content
tab1, tab2, tab3 = st.tabs(["🏡 Predict Price", "📊 Model Comparison", "ℹ️ How to Use"])

with tab1:
    st.markdown("## Enter House Details")
    
    # Check if model exists
    if not os.path.exists('models/best_model.pkl'):
        st.error("❌ Model not found! Please train the model first by running: `python src/train_models.py`")
        st.stop()
    
    # Create input form
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🏗️ General Information")
        overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 7, help="Overall material and finish quality")
        overall_cond = st.slider("Overall Condition (1-10)", 1, 10, 5, help="Overall condition rating")
        year_built = st.number_input("Year Built", 1872, 2024, 2000)
        year_remod = st.number_input("Year Remodeled", 1872, 2024, 2000)
        
    with col2:
        st.markdown("### 📐 Area & Space")
        gr_liv_area = st.number_input("Above Ground Living Area (sq ft)", 300, 6000, 1500)
        total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", 0, 3000, 800)
        first_flr_sf = st.number_input("First Floor Area (sq ft)", 300, 5000, 1000)
        second_flr_sf = st.number_input("Second Floor Area (sq ft)", 0, 2000, 500)
        lot_area = st.number_input("Lot Area (sq ft)", 1300, 100000, 8000)
        
    with col3:
        st.markdown("### 🛏️ Rooms & Features")
        bedroom_abvgr = st.number_input("Bedrooms Above Ground", 0, 10, 3)
        full_bath = st.number_input("Full Bathrooms", 0, 5, 2)
        half_bath = st.number_input("Half Bathrooms", 0, 3, 1)
        bsmt_full_bath = st.number_input("Basement Full Bathrooms", 0, 3, 1)
        bsmt_half_bath = st.number_input("Basement Half Bathrooms", 0, 2, 0)
        garage_cars = st.number_input("Garage Car Capacity", 0, 5, 2)
        garage_area = st.number_input("Garage Area (sq ft)", 0, 1500, 500)
    
    # Additional features in expander
    with st.expander("🔧 Additional Features (Optional)"):
        col4, col5 = st.columns(2)
        
        with col4:
            ms_zoning = st.selectbox("Zoning Classification", 
                ['RL', 'RM', 'FV', 'RH', 'C (all)'], index=0)
            neighborhood = st.selectbox("Neighborhood", 
                ['CollgCr', 'Veenker', 'Crawfor', 'NoRidge', 'Mitchel', 'Somerst', 
                 'NWAmes', 'OldTown', 'BrkSide', 'Sawyer', 'NridgHt', 'NAmes', 
                 'SawyerW', 'IDOTRR', 'MeadowV', 'Edwards', 'Timber', 'Gilbert', 
                 'StoneBr', 'ClearCr', 'NPkVill', 'Blmngtn', 'BrDale', 'SWISU', 
                 'Blueste'], index=0)
            house_style = st.selectbox("House Style", 
                ['2Story', '1Story', '1.5Fin', '1.5Unf', 'SFoyer', 'SLvl', '2.5Unf', '2.5Fin'], index=0)
            
        with col5:
            central_air = st.selectbox("Central Air Conditioning", ['Y', 'N'], index=0)
            kitchen_qual = st.selectbox("Kitchen Quality", 
                ['Ex', 'Gd', 'TA', 'Fa'], index=1)
            fireplace = st.number_input("Number of Fireplaces", 0, 4, 0)
    
    # Predict button
    st.markdown("---")
    if st.button("🔮 Predict House Price", use_container_width=True):
        with st.spinner("Calculating prediction..."):
            # Prepare input data (simplified version with key features)
            input_data = {
                'MSSubClass': 60,
                'MSZoning': ms_zoning,
                'LotArea': lot_area,
                'Street': 'Pave',
                'LotShape': 'Reg',
                'LandContour': 'Lvl',
                'Utilities': 'AllPub',
                'LotConfig': 'Inside',
                'LandSlope': 'Gtl',
                'Neighborhood': neighborhood,
                'Condition1': 'Norm',
                'Condition2': 'Norm',
                'BldgType': '1Fam',
                'HouseStyle': house_style,
                'OverallQual': overall_qual,
                'OverallCond': overall_cond,
                'YearBuilt': year_built,
                'YearRemodAdd': year_remod,
                'RoofStyle': 'Gable',
                'RoofMatl': 'CompShg',
                'Exterior1st': 'VinylSd',
                'Exterior2nd': 'VinylSd',
                'MasVnrType': 'None',
                'MasVnrArea': 0,
                'ExterQual': 'TA',
                'ExterCond': 'TA',
                'Foundation': 'PConc',
                'BsmtQual': 'TA',
                'BsmtCond': 'TA',
                'BsmtExposure': 'No',
                'BsmtFinType1': 'Unf',
                'BsmtFinSF1': 0,
                'BsmtFinType2': 'Unf',
                'BsmtFinSF2': 0,
                'BsmtUnfSF': total_bsmt_sf,
                'TotalBsmtSF': total_bsmt_sf,
                'Heating': 'GasA',
                'HeatingQC': 'Ex',
                'CentralAir': central_air,
                'Electrical': 'SBrkr',
                '1stFlrSF': first_flr_sf,
                '2ndFlrSF': second_flr_sf,
                'LowQualFinSF': 0,
                'GrLivArea': gr_liv_area,
                'BsmtFullBath': bsmt_full_bath,
                'BsmtHalfBath': bsmt_half_bath,
                'FullBath': full_bath,
                'HalfBath': half_bath,
                'BedroomAbvGr': bedroom_abvgr,
                'KitchenAbvGr': 1,
                'KitchenQual': kitchen_qual,
                'TotRmsAbvGrd': bedroom_abvgr + full_bath + 2,
                'Functional': 'Typ',
                'Fireplaces': fireplace,
                'GarageType': 'Attchd',
                'GarageYrBlt': year_built,
                'GarageFinish': 'Unf',
                'GarageCars': garage_cars,
                'GarageArea': garage_area,
                'GarageQual': 'TA',
                'GarageCond': 'TA',
                'PavedDrive': 'Y',
                'WoodDeckSF': 0,
                'OpenPorchSF': 0,
                'EnclosedPorch': 0,
                '3SsnPorch': 0,
                'ScreenPorch': 0,
                'PoolArea': 0,
                'MiscVal': 0,
                'MoSold': 6,
                'YrSold': 2024,
                'SaleType': 'WD',
                'SaleCondition': 'Normal'
            }
            
            try:
                # Make prediction
                predictor = HousePricePredictor()
                result = predictor.predict_with_confidence(input_data)
                
                # Display prediction
                st.markdown(f"""
                    <div class="prediction-box">
                        <h2>Predicted House Price</h2>
                        <div class="prediction-value">${result['prediction']:,.0f}</div>
                        {f'<p>95% Confidence Interval: ${result["lower_bound"]:,.0f} - ${result["upper_bound"]:,.0f}</p>' if result['lower_bound'] else ''}
                    </div>
                """, unsafe_allow_html=True)
                
                # Additional insights
                col_a, col_b, col_c = st.columns(3)
                
                with col_a:
                    price_per_sqft = result['prediction'] / gr_liv_area
                    st.metric("Price per Sq Ft", f"${price_per_sqft:.2f}")
                
                with col_b:
                    total_sf = first_flr_sf + second_flr_sf + total_bsmt_sf
                    st.metric("Total Square Footage", f"{total_sf:,} sq ft")
                
                with col_c:
                    total_bath = full_bath + 0.5 * half_bath + bsmt_full_bath + 0.5 * bsmt_half_bath
                    st.metric("Total Bathrooms", f"{total_bath:.1f}")
                
                st.success("✅ Prediction completed successfully!")
                
            except Exception as e:
                st.error(f"❌ Error making prediction: {str(e)}")
                st.info("Make sure you have trained the model first by running: `python src/train_models.py`")

with tab2:
    st.markdown("## 📊 Model Performance Comparison")
    
    try:
        results = joblib.load('models/training_results.pkl')
        
        # Create comparison dataframe
        comparison_data = []
        for model_name, metrics in results.items():
            comparison_data.append({
                'Model': model_name,
                'Validation RMSE': f"${metrics['val_rmse']:,.0f}",
                'Validation MAE': f"${metrics['val_mae']:,.0f}",
                'Validation R²': f"{metrics['val_r2']:.4f}",
                'Training Time': f"{metrics['training_time']:.2f}s"
            })
        
        df_comparison = pd.DataFrame(comparison_data)
        
        st.dataframe(df_comparison, use_container_width=True, hide_index=True)
        
        # Display comparison chart
        st.markdown("### 📈 Visual Comparison")
        if os.path.exists('models/model_comparison.png'):
            st.image('models/model_comparison.png', use_column_width=True)
        else:
            st.info("Run the training script to generate comparison charts.")
        
        # Explanation
        st.markdown("### 📖 Metrics Explanation")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            **RMSE** (Root Mean Squared Error)
            - Measures average prediction error
            - Lower is better
            - In dollars ($)
            """)
        
        with col2:
            st.markdown("""
            **MAE** (Mean Absolute Error)
            - Average absolute difference
            - Lower is better
            - More interpretable than RMSE
            """)
        
        with col3:
            st.markdown("""
            **R² Score**
            - Proportion of variance explained
            - Higher is better (max = 1.0)
            - Indicates model fit quality
            """)
        
    except FileNotFoundError:
        st.warning("⚠️ No training results found. Please train the models first.")
        st.code("python src/train_models.py", language="bash")

with tab3:
    st.markdown("## ℹ️ How to Use This Application")
    
    st.markdown("""
    ### 🚀 Quick Start Guide
    
    #### Step 1: Train the Models (First Time Only)
    Before using the predictor, you need to train the machine learning models:
    ```bash
    # Install dependencies
    pip install -r requirements.txt
    
    # Train the models
    python src/train_models.py
    ```
    
    #### Step 2: Make Predictions
    1. Go to the **"Predict Price"** tab
    2. Enter house details in the input fields
    3. Click **"Predict House Price"** button
    4. View the predicted price and confidence interval
    
    #### Step 3: Compare Models
    - Check the **"Model Comparison"** tab to see how different algorithms performed
    - Review metrics like RMSE, MAE, and R² score
    
    ---
    
    ### 📋 Input Fields Guide
    
    **General Information**
    - **Overall Quality**: Rate the overall material and finish (1-10)
    - **Overall Condition**: Rate the overall condition (1-10)
    - **Year Built**: Construction year
    - **Year Remodeled**: Last remodeling year
    
    **Area & Space**
    - **Living Area**: Above ground living area in square feet
    - **Basement Area**: Total basement area
    - **Floor Areas**: First and second floor areas
    - **Lot Area**: Lot size in square feet
    
    **Rooms & Features**
    - **Bedrooms**: Number of bedrooms above ground
    - **Bathrooms**: Full and half bathrooms (above ground and basement)
    - **Garage**: Car capacity and area
    
    ---
    
    ### 🎯 Project Information
    
    **Dataset**: Kaggle - House Prices: Advanced Regression Techniques
    
    **Algorithms Used**:
    1. **Ridge Regression**: Linear regression with L2 regularization
    2. **Random Forest**: Ensemble of decision trees
    
    **Evaluation Metrics**:
    - RMSE (Root Mean Squared Error)
    - MAE (Mean Absolute Error)
    - R² Score (Coefficient of Determination)
    
    ---
    
    ### 💡 Tips for Best Results
    
    - Provide accurate measurements for better predictions
    - Use the optional features for more precise estimates
    - Check the confidence interval to understand prediction uncertainty
    - Compare with similar houses in the neighborhood
    
    ---
    
    ### 🐛 Troubleshooting
    
    **Error: Model not found**
    - Solution: Run `python src/train_models.py` to train the models
    
    **Error: Module not found**
    - Solution: Install dependencies with `pip install -r requirements.txt`
    
    **Unexpected predictions**
    - Check if all input values are reasonable
    - Verify that the model has been trained on similar data
    """)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #7f8c8d;'>
        <p>🏠 House Price Predictor | Built with Streamlit & Scikit-learn</p>
        <p>AI Project - Advanced Regression Techniques</p>
    </div>
""", unsafe_allow_html=True)
