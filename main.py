import os 
import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestionConfig,DataIngestion

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()