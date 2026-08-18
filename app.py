import streamlit as st
import pandas as pd
import numpy as np
import sys
import os

# Add the src directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# HEADER
st.title("📚 Student Performance Predictor")
st.markdown("""
This app predicts **Math Score** based on student characteristics and previous test scores.
Enter the student details below to get a prediction!
""")

st.divider()

# INPUT SECTION - TWO COLUMNS
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("📝 Student Information")
    
    gender = st.selectbox(
        "Gender",
        options=['male', 'female'],
        help="Student's gender"
    )
    
    race_ethnicity = st.selectbox(
        "Race/Ethnicity",
        options=['group A', 'group B', 'group C', 'group D', 'group E'],
        help="Student's race/ethnicity group"
    )
    
    parental_level_of_education = st.selectbox(
        "Parental Level of Education",
        options=[
            "associate's degree",
            "bachelor's degree",
            "high school",
            "master's degree",
            "some college",
            "some high school"
        ],
        help="Highest education level of parents"
    )
    
    lunch = st.selectbox(
        "Lunch Type",
        options=['standard', 'free/reduced'],
        help="Type of lunch program"
    )
    
    test_preparation_course = st.selectbox(
        "Test Preparation Course",
        options=['none', 'completed'],
        help="Whether student completed test prep course"
    )

with col2:
    st.subheader("📊 Previous Scores")
    
    reading_score = st.slider(
        "Reading Score",
        min_value=0,
        max_value=100,
        value=70,
        step=1,
        help="Previous reading test score (0-100)"
    )
    
    writing_score = st.slider(
        "Writing Score",
        min_value=0,
        max_value=100,
        value=70,
        step=1,
        help="Previous writing test score (0-100)"
    )
    
    st.subheader("ℹ️ About the Model")
    st.info("""
    **Algorithm**: Best performing model from evaluation  
    **Features**: Gender, race, education, lunch, test prep, reading score, writing score  
    **Target**: Math score (0-100)  
    **Training Data**: Student performance dataset
    """)

st.divider()

# ============================================
# PREDICTION BUTTON
# ============================================
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    predict_button = st.button("🎯 Predict Math Score", type="primary", use_container_width=True)

# ============================================
# PREDICTION LOGIC
# ============================================
if predict_button:
    try:
        with st.spinner("Making prediction..."):
            # Create CustomData object with input values
            data = CustomData(
                gender=gender,
                race_ethnicity=race_ethnicity,
                parental_level_of_education=parental_level_of_education,
                lunch=lunch,
                test_preparation_course=test_preparation_course,
                reading_score=reading_score,
                writing_score=writing_score
            )
            
            # Convert to DataFrame
            pred_df = data.get_data_as_data_frame()
            
            # Show input data in expander
            with st.expander("📋 View Input Data", expanded=False):
                st.dataframe(pred_df, use_container_width=True)
            
            # Make prediction
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            score = float(results[0])
            
            # ============================================
            # DISPLAY RESULTS
            # ============================================
            st.divider()
            
            # Main result
            st.success(f"## ✅ Predicted Math Score: **{score:.2f}**")
            
            # Metric display
            col_m1, col_m2, col_m3 = st.columns(3)
            with col_m1:
                st.metric("Predicted Score", f"{score:.2f}", delta=None)
            with col_m2:
                if score >= 80:
                    st.metric("Performance", "🌟 Excellent")
                elif score >= 60:
                    st.metric("Performance", "📈 Good")
                elif score >= 40:
                    st.metric("Performance", "📊 Average")
                else:
                    st.metric("Performance", "📉 Needs Improvement")
            with col_m3:
                st.metric("Max Score", "100", delta=None)
            
            # Performance indicator
            if score >= 80:
                st.balloons()
                st.success("🌟 **Excellent performance!** Keep up the great work!")
            elif score >= 60:
                st.success("📈 **Good performance!** You're on the right track!")
            elif score >= 40:
                st.warning("📊 **Average performance.** Some improvement needed.")
            else:
                st.error("📉 **Needs improvement.** Consider additional help.")
            
            # Progress bar for visual representation
            st.progress(score/100, text=f"Score: {score:.2f}/100")
            
    except Exception as e:
        st.error(f"❌ Error making prediction: {str(e)}")
        st.exception(e)

# ============================================
# FOOTER
# ============================================
st.divider()
st.markdown("""
<div style='text-align: center'>
    <p>Built with ❤️ using <a href='https://streamlit.io/' target='_blank'>Streamlit</a> | 
    <a href='https://github.com/' target='_blank'>GitHub</a></p>
    <p style='font-size: 0.8em; color: #666;'>Student Performance Predictor v1.0</p>
</div>
""", unsafe_allow_html=True)