import os
from dotenv import load_dotenv, find_dotenv

class Config:

    REDSHIFT_USERNAME = ""
    REDSHIFT_PASSWORD = ""
    REDSHIFT_HOSTNAME = ""

    def __init__(self):

    config_vars = [
        "REDSHIFT_USERNAME",
        "REDSHIFT_PASSWORD",
        "REDSHIFT_HOSTNAME"
    ]

    for i, config_var in enumerate(config_vars):
        # check to see if this was passed in as an environment variable first
        value = os.getenv(config_var)

        # fall back to .env file if not
        if(value is None):
            load_dotenv(find_dotenv())
            value = os.environ.get(config_var)

        # still couldn't find it, fail
        if(value is None):
            raise Exception(f'{config_var} not found in environment or .env')

        # self.REDSHIFT_USERNAME = user
        setattr(self, config_var, value)
