"""util.py: utility functions for project."""
 
import datetime


def get_timestamp():
    """
    get time in format I like

    """
    
    dt = datetime.datetime.now()
    timestamp = dt.strftime("%Y-%m-%d, %X")
    return timestamp