"""Helper Module for Cron Module"""

import time

def get_time() -> str:
    """Gets the current time and returns it as a String

            Hr:Min:Sec   D/M/Y   
    Example: '19:18:15 (03/03/24)'
    
    """
    return time.strftime("%X (%d/%m/%y)")
