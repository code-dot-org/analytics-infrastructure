# Baker's running to do list

Things I thought about while programming that I don't want to forget for later.

* turn code that opens and runs multi-statement sql files into a function/module for resuse elsewhere
* refactor execute-dir-of-files to use this ^^^, and also modularize for usage in other cronjobs.
* these ^^^ two functions are things we can (or sometimes we'll have to) continually hone for error checking, file processing etc.
* I started this ^^^ in the file redteamfuncs.py <-- theory being reusable functions we want to import can live there.



* unknown (to baker) if we have to roll our own here as I have done, or if there are other better, more standard ways
* UPDATE output(s) to report sucess/failure conditions more succinctly.  We don't need or want to see the results of every query.  redshift-connector must have some functions for reporting these conditions.


## The Tour

1. Big picture (diagram: computer, github, ECS, redshift, cloudwatch).  
	1. Multiple ways to execute code. local simulates ECS. ECS (via cloudformation?) has cronjob.  Can execute (single) python file on timer.  
	2. Github repo can be setup with "final" areas for things run automatically and testing areas for development.  
	3. initial thought/example: cron-daily executes all .sql files in folder called /daily.  
	4. question: how to setup execution priority/ordering/dependencies?  Can do with with ordered folder or file names (hack).  Could setup a .yml file, or even a spreadsheet or (gasp) redshift table for it.  This sophistication/simplicity of this is crucial to get right.
	5. SAVE THESE QUESTIONS UNTIL AFTER THE TOUR

2. Tools?
	* Sublime text + sublime merge?

2. Setup/config
	* create .env file (in src directory)
	* from config import Config -- use this. 
	* Test with **redshift-simple-connect-test.py**

3. **redshift-simple-file-test.py**
	* Execute single file hard coded.  Note similarity with ^^^.

4. **redshift-cmd-line-single-statement-file.py**
	* Next step: pass the file you want to run into the script.
	* This one is limited with assumption that file has only a single SQL statement.
	* The purpose of looking is to understand the command line modality

5. **redshift-cmd-line-multi-statement-file.py**
	* Same as prev, but now code will split file on ';' and attempt to execute each statement.
	* This is probably useful utility to have around in general and should be built out for robustness.

6. **redshift-cmd-line-dir-of-files.py**
	* Now you can pass the name of a directory containing .sql files via command line args.
	* This is also likely a useful utility and should be built out for robustness.


