import sys
import json
import logging
import rds_config
import pymysql as mysql

#rds settings
rds_host  = rds_config.rds_endpoint
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# connecting to rds
try:
    conn = mysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except mysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

# Handler method
def handler(data, context):
    """
    This function updates a contact in MySQL RDS instance
    """
    contact = json.loads(data)
    with conn.cursor() as cur:
        cur.execute(f"UPDATE  CONTACT SET "+
        f"contact_name = '{contact['name']}',"+
        f"contact_email = '{contact['email']}',"+
        f"contact_phone = '{contact['phone']}',"+
        f"contact_birth = '{contact['birth']}' WHERE id = '{contact['id']}';")
        conn.commit()
        logger.info("SUCCESS: Contact updated")
    conn.commit()

    return "Updating a contact in RDS MySQL table"

handler()