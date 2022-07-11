import glob

sqlfiles = []
dir = '../sql-files/'

for file in glob.glob(dir+"*.sql"):
    sqlfiles.append(file)

print("found sql files in dir")
for f in sqlfiles:
    print("\t",f)

'''
txtfiles = []
for file in glob.glob("../sql-files/*.sql"):
    txtfiles.append(file)

for f in txtfiles:
	print(f)
'''
