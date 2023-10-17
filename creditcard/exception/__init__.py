import sys,os

def error_message_detail(error, error_detail: sys):
    """
    Detail message regarding the error
    Args:
        error: error
        error: error_details
    returns:
        error message
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    """
    Exception class
    Args:
        Exception: Takes the custom exception
    Return:
        Returns the Exception details
    """

    def __init__(self,error_message, error_detail:sys):
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message