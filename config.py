import os
from dotenv import load_dotenv, find_dotenv

class Config:
  REDSHIFT_USER = ""
  REDSHIFT_PW = ""
  DOMAIN = ""

  def __init__(self):
    user = os.getenv("REDSHIFT_USER")

    if(user is None):
      load_dotenv(find_dotenv())
      user = os.environ.get("REDSHIFT_USER")

    if(user is None):
      raise Exception("REDSHIFT_USER not found")

    self.REDSHIFT_USER = user