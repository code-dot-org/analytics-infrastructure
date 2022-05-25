import redshift_connector
from config import Config

CONFIG = Config()

conn = redshift_connector.connect(
     host=CONFIG.REDSHIFT_HOSTNAME,
     database='dashboard',
     user=CONFIG.REDSHIFT_USERNAME,
     password=CONFIG.REDSHIFT_PASSWORD


)

query = ("SELECT * "
         "FROM dashboard_production_pii.pd_survey_questions "
         "WHERE questions ILIKE '%taught%' "
         "LIMIT 100;")

result = conn.cursor().execute(query)
list = result.fetchall()
print(list)
