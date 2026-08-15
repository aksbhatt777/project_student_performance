import sys
from src.logger import logging

def error_msg_detail(error,error_detail:sys): #parameter expects sys module
    _,_,exc_tb=error_detail.exc_info() # errorType-class of exception, errorValue - actual exception instance, 
    #traceback - traceback object encapsulating the call stack at the point where the error occurred
    # eg : (ZeroDivisionError, "division by zero", <traceback object>)
    file_name=exc_tb.tb_frame.f_code.co_filename #string containing full or relative path to Python file
    error_msg="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error)) 

    return error_msg


class CustomException(Exception):
    def __init__(self, error_msg,error_detail:sys):
        super().__init__(error_msg)
        self.error_msg=error_msg_detail(error_msg,error_detail=error_detail)

    def __str__(self):
        return self.error_msg

    
## just to check 
# if __name__=="__main__":
#     try:
#         x=1/0
#     except Exception as e:
#         logging.info ("this is divide by zero error")
#         raise CustomException(e,sys)