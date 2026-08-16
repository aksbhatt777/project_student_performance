import sys
import pandas as pd
import numpy as np
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        self.model_path = os.path.join('artifacts', 'model.pkl')
        self.preprocessor_path = os.path.join('artifacts', 'proprocessor.pkl')
        
        logging.info(f"Model path: {self.model_path}")
        logging.info(f"Preprocessor path: {self.preprocessor_path}")
    
    def predict(self, features):
        try:
            logging.info("Starting prediction...")
            
            # Check if artifacts exist
            if not os.path.exists(self.model_path):
                raise FileNotFoundError(f"Model file not found at: {self.model_path}")
            if not os.path.exists(self.preprocessor_path):
                raise FileNotFoundError(f"Preprocessor file not found at: {self.preprocessor_path}")
            
            logging.info("Loading model and preprocessor...")
            model = load_object(file_path=self.model_path)
            preprocessor = load_object(file_path=self.preprocessor_path)
            
            logging.info(f"Input features shape: {features.shape}")
            logging.info(f"Input features columns: {features.columns.tolist()}")
            
            logging.info("Transforming features...")
            data_scaled = preprocessor.transform(features)
            
            logging.info("Making prediction...")
            preds = model.predict(data_scaled)
            
            logging.info(f"Prediction successful: {preds}")
            return preds
            
        except FileNotFoundError as e:
            logging.error(f"Artifact not found: {str(e)}")
            raise CustomException(f"Model or preprocessor artifacts not found. Please run train_model.py first. Error: {str(e)}", sys)
        except Exception as e:
            logging.error(f"Prediction error: {str(e)}")
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education: str,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int):
        
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
    
    def get_data_as_data_frame(self):
        try:
            # ✅ CORRECT: Use the SAME column names as the training data
            custom_data_input_dict = {
                "gender": [self.gender],
                "race/ethnicity": [self.race_ethnicity],  # ← Changed from race_ethnicity
                "parental level of education": [self.parental_level_of_education],  # ← Changed from parental_level_of_education
                "lunch": [self.lunch],
                "test preparation course": [self.test_preparation_course],  # ← Changed from test_preparation_course
                "reading score": [self.reading_score],  # ← Changed from reading_score
                "writing score": [self.writing_score]   # ← Changed from writing_score
            }
            
            df = pd.DataFrame(custom_data_input_dict)
            logging.info(f"Created DataFrame with columns: {df.columns.tolist()}")
            return df
            
        except Exception as e:
            raise CustomException(e, sys)