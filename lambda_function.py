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
def handler(event, context):
    data = []
    """
    This function creates a contact in MySQL RDS instance
    """
    with conn.cursor() as cur:
        cur.execute("SELECT id,contact_name,contact_email,contact_phone,contact_birth FROM CONTACT;")
        result = list(cur.fetchall())
        conn.commit()
        logger.info("SUCCESS: selecting Contacts")
        for row in result:
            data.append(json.dumps({
                'id':row[0],
                'name':row[1],
                'email':row[2],
                'phone':row[3],
                'birth':str(row[4])
            }))

    conn.commit()
    logger.info(data)
    return data