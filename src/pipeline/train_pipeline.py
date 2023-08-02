from src.data_transformation import DataTransformation
from src.exception import CustomException
from src.components import data_ingestion
import sys

class TrainPipeline:
    def __init__(self)->None:
        self.data_ingestion=data_ingestion()
        
        self.data_transformation=DataTransformation()
        


def run_pipeline(self):
    try:
        train_path, test_path=self.data_ingestion.initiate_data_ingestion()
        
        (
            train_arr,
            test_arr,
            preprocessor_file_path,
        )=self.data_transformation.initiate_data_transformation(
            train_path=train_path, test_path=test_path
        )
        
        r2_square=self.model_trainer.initiate_model_trainer(
            train_array=train_arr,
            test_array=test_arr,
            preprocessor_path=preprocessor_file_path
        )
        print("Training Completed. Trained model score: ", r2_square)
        
        
    except Exception as e:
        raise CustomException(e,sys)