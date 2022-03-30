import redshift_connector
import sys

conn = redshift_connector.connect(
     host=sys.argv[0],
     database=sys.argv[1],
     user=sys.argv[2],
     password=sys.argv[3]
)

print('Hello world!')
