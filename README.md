# TEST_OUTCUBATOR
# Install library
pip install -r .\environment.txt
# Add file db_connector.properties (MySQL and MongoDB configure)
[DATABASE]
DB_HOST= host
DB_SCHEMA= database
DB_PORT = port
DB_USER= user name
DB_PWD= password

[NOSQL]
NOSQL_HOST=host
NOSQL_PORT = port
# 1. ETL pipeline
# SQL
python .\ingest_sql.py     
# NoSQL
python .\ingest_nosql.py 

# 2.SQL query
run sql_test.sql in MySQL