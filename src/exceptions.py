import sys

def error_message_details(error , error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    error_message = f"Error occured in python script {} , at line number {} , with error message {}"
    .format(exc_tb.tb_frame.f_code.co_filename , exc_tb.tb_lineno , str(error))

    return error_message


class CustomException(Exception):
    def __init__(self, error_message , error_details:sys):
        super().__init__(error.message)
        self.error_message = error_message_details(error_message , error_details = error_details)

    def __str__(self):
        return self.error_message
        
