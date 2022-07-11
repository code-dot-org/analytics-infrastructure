# given a redshift connection and a single sql command, attempt to execute the command
# conn -- a properly instantiated redshift-connector connection
# sql_cmd -- a single SQL statement/commeand to execute
def run_and_display_cmd(conn, sql_cmd):

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



def run_and_display(conn, filename):

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
			run_and_display_cmd(conn, command)
		except: 
			print("Command skipped: ", command)