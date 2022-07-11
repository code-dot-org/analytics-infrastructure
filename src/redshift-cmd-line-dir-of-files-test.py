import redshift_connector
from config import Config
import sys
import pandas
import glob
import os

############### HELPER FUNCTIONS #######################
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

##############################################################	

CONFIG = Config()

conn = redshift_connector.connect(
     host=CONFIG.REDSHIFT_HOSTNAME,
     database='dashboard',
     user=CONFIG.REDSHIFT_USERNAME,
     password=CONFIG.REDSHIFT_PASSWORD


)

# Check that arg was given
if(len(sys.argv)<2 or os.path.isdir(sys.argv[1]) is False ):
     print("\nMissing argument OR arg given is NOT a directory")
     print("Provide path to a directory with 1 or more .sql files in it.")
     print("Every SQL statement in every .sql file in the provided directory will be exectued.")
     print("\nUSAGE: $ poetry run python redshift-cmd-line-multi-statement-file-test.py path/to/dir/of/sql/files/  (w/trailing slash\n")
     exit()

# open dir of files
sqlfiles = []
dir = sys.argv[1]

for file in glob.glob(dir+"*.sql"):
    sqlfiles.append(file)

print("found sql files in dir")
for f in sqlfiles:
	print("\t",f)
	
	# open each .sql file from list and process
	open_sql_and_process(f)
