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

##########
# 1. open sql file specified as command line arg.
# 2. read results into a pandas dataframe for printing results
############

# open .sql file specified on command line and read it into a string variable
f = open(sys.argv[1])
query = f.read() 
f.close()

# execute query and read into a pandas dataframe
r = conn.cursor().execute(query)
result: pandas.DataFrame = r.fetch_dataframe()


print("----------QUERY----------")
print(query)
print("----------RESULTS----------")
print(result)
