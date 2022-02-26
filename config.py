import logging


class Config:
    """
    Configuration parameters for the application.
    """
    param = {
        "LOG_DIR": "Logs",
        "LOG_FILE": "logs.log",
        "DEBUG_LEVEL": logging.INFO,
        "RESOURCES_DIR": "Resources",
        "OUTPUT_DIR": "Output",
        "INT_FIELDS": [],
        "LIMIT_RECORDS": 10
    }
