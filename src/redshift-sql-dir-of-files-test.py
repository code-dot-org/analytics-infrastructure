import redshift_connector
from config import Config
import sys
import pandas
import glob

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


def open_sql_and_process(filename):

	# open filename .sql and read it into a string variable
	f = open(filename)
	sql_file = f.read() 
	f.close()
	print("Opened and read file: ", filename)



	# split out the different sql commands by ;
	sql_commands = sql_file.split(';')
	print(" -- with ",len(sql_commands)," commands")



	# for each command run and display the results
	for command in sql_commands:
    	# This will skip and report errors
    	# For example, if the tables do not yet exist, this will skip over
    	# the DROP TABLE commands
		try:
			run_and_display(command)
		except: 
			print("Command skipped: ", command)
	


# open dir of files
sqlfiles = []
dir = '../sql-files/' #todo read path from argv[1]

for file in glob.glob(dir+"*.sql"):
    sqlfiles.append(file)

print("found sql files in dir")
for f in sqlfiles:
	print("\t",f)
	
	# open each .sql file from list and process
	open_sql_and_process(f)
