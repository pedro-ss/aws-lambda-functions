# aws-lambda-functions
A lambda functions collection to Advanced Network Topics class

CRUD Lambda functions writen in Python connecting in a RDS (MySQL) database.

Comando usado para criar a instância do MySQL:

aws rds create-db-instance --db-name servlessdb --engine MySQL \
--db-instance-identifier MySQLForServlessArch --backup-retention-period 3 \
--db-instance-class db.t2.micro --allocated-storage 5 --no-publicly-accessible \
--master-username aws_aluno --master-user-password aws_aluno

funções criadas através do console da AWS

para empacotar:

pip install --target ./package <dependencies>

cd package/

zip -r ../lambda_function.zip .

cd ..

zip -g lambda_function.zip rds_config.py lambda_function.py

fazer upload de função no console da AWS.