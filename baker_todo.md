# Baker's running to do list

Things I thought about while programming that I don't want to forget for later.

* turn code that opens and runs multi-statement sql files into a function/module for resuse elsewhere
* refactor execute-dir-of-files to use this ^^^, and also modularize for usage in other cronjobs.
* these ^^^ two functions are things we can (or sometimes we'll have to) continually hone for error checking, file processing etc.
* unknown (to baker) if we have to roll our own here as I have done, or if there are other better, more standard ways
* UPDATE output(s) to report sucess/failure conditions more succinctly.  We don't need or want to see the results of every query.  redshift-connector must have some functions for reporting these conditions.
