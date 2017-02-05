"""
file        :   util.py
date        :   2014-0223
module      :   common
classes     :   
desription  :   common uitlity tools and functions
"""
 
import datetime


"""
get time in format I like

"""
def get_timestamp():
    
    dt = datetime.datetime.now()
    timestamp = dt.strftime("%Y-%m%d, %X")
    return timestamp