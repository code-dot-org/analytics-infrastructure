import os
from dotenv import load_dotenv, find_dotenv

class Config:
  REDSHIFT_USER = ""
  REDSHIFT_PW = ""
  DOMAIN = ""

  def __init__(self):
    # check to see if this was passed in as an environment variable first
    user = os.getenv("REDSHIFT_USER")

    # fall back to .env file
    if(user is None):
      load_dotenv(find_dotenv())
      user = os.environ.get("REDSHIFT_USER")

    # couldn't find a REDSHIFT_USER, fail
    if(user is None):
      raise Exception("REDSHIFT_USER not found")

    self.REDSHIFT_USER = user