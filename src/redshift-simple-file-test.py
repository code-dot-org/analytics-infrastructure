import redshift_connector
from config import Config
import sys
import pandas

CONFIG = Config()

conn = redshift_connector.connect(
     host=CONFIG.REDSHIFT_HOSTNAME,
     database='dashboard',
     user=CONFIG.REDSHIFT_USERNAME,
     password=CONFIG.REDSHIFT_PASSWORD


)

# open an .sql file and read it into a string variable
# assumption: simple_sql.sql has a single SQL command
f = open("../sql-files/single-command.sql")
query = f.read() 
f.close()

# execute the command and fetch all results as a plain string
result = conn.cursor().execute(query)
list = result.fetchall()

print("----------QUERY----------")
print(query)
print("----------RESULTS----------")
print(list)
