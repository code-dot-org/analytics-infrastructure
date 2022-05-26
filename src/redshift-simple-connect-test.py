import redshift_connector
from config import Config

CONFIG = Config()

conn = redshift_connector.connect(
     host=CONFIG.REDSHIFT_HOSTNAME,
     database='dashboard',
     user=CONFIG.REDSHIFT_USERNAME,
     password=CONFIG.REDSHIFT_PASSWORD


)

result = conn.cursor().execute("SELECT * FROM dashboard_production_pii.pd_survey_questions WHERE questions ILIKE '%taught%' LIMIT 10;")
list = result.fetchall()
print(list)