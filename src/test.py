# import os
import redshift_connector
from config import Config

CONFIG = Config()

print(f'Hello, {CONFIG.REDSHIFT_USERNAME}!')
