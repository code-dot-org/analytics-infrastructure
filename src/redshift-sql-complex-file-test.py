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

def run_and_display(sql_cmd):

	r = conn.cursor().execute(sql_cmd)
	
	print("")
	print("")
	print("----------QUERY----------")
	print(sql_cmd)
	print("----------RESULTS----------")
	
	try:
		result: pandas.DataFrame = r.fetch_dataframe()
		print(result)
	except:
		print("no results to display")

	print("---------------------------")


# open .sql file from command line and read it into a string variable
f = open(sys.argv[1])
sql_file = f.read() 
f.close()

print("Opened and read file: ", sys.argv[1])
print(" -- with ",len(sql_commands)," commands")

# split out the different sql commands by ;
# for each command run and display the results

sql_commands = sql_file.split(';')
for command in sql_commands:
    # This will skip and report errors
    # For example, if the tables do not yet exist, this will skip over
    # the DROP TABLE commands
	try:
		run_and_display(command)
	except: 
		print("Command skipped: ", command)


