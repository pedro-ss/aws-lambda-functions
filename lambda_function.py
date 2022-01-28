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
    This function creates a contact in MySQL RDS instance
    """
    with conn.cursor() as cur:
        cur.execute("create table if not exists CONTACT"
            "(id INT AUTO_INCREMENT PRIMARY KEY,"+
            "contact_name VARCHAR(100) DEFAULT 'null',"+
            "contact_email VARCHAR(100) DEFAULT 'null',"+  
            "contact_phone VARCHAR(14) DEFAULT 'null',"+
            "contact_birth DATE);")
        cur.execute(f"insert into CONTACT (contact_name,contact_email,contact_phone,contact_birth)"+
        f"values('{data['name']}','{data['email']}','{data['phone']}','{data['birth']}')")
        conn.commit()
        logger.info("SUCCESS: Contact created")
    conn.commit()

    return "Added a contact in RDS MySQL table"