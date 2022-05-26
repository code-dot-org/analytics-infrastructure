import redshift_connector
from config import Config
import sys
import pandas
from redteamfuncs import run_and_display

CONFIG = Config()

conn = redshift_connector.connect(
     host=CONFIG.REDSHIFT_HOSTNAME,
     database='dashboard',
     user=CONFIG.REDSHIFT_USERNAME,
     password=CONFIG.REDSHIFT_PASSWORD


)

# def run_and_display(sql_cmd):

# 	r = conn.cursor().execute(sql_cmd)
	
# 	print("")
# 	print("")
# 	print("----------QUERY----------")
# 	print(sql_cmd)
# 	print("----------RESULTS----------")
	
# 	try:
# 		result: pandas.DataFrame = r.fetch_dataframe()
# 		print(result)
# 	except:
# 		print("no results to display")

# 	print("---------------------------")


# Check that arg was given
if(len(sys.argv)<2 or sys.argv[1].find('.sql') == -1):
     print("\nMissing argument or not a .sql file.")
     print("Provide a file with 1 or more SQL statements in it, delimited by semi-colons")
     print("USAGE: $ poetry run python redshift-cmd-line-multi-statement-file-test.py path/to/filename.sql\n")
     exit()


# open .sql file from command line and read it into a string variable
f = open(sys.argv[1])
sql_file = f.read() 
f.close()

print("Opened and read file: ", sys.argv[1])

# split out the different sql commands by ;
# for each command run and display the results
sql_commands = sql_file.split(';')
print(" -- with ",len(sql_commands)," commands")


for command in sql_commands:
    # This will skip and report errors
    # For example, if the tables do not yet exist, this will skip over
    # the DROP TABLE commands
	try:
		#run_and_display(command)
		run_and_display(conn, command)
	except: 
		print("Command skipped: ", command)
