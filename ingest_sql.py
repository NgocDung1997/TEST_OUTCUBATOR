import mysql.connector
from mysql.connector import Error
import configparser
import os
import pandas as pd
from sqlalchemy import create_engine
from dowload_source import dowload_from_url

dowload_from_url()
#Read properties
config = configparser.ConfigParser()
config.read('D:\\test\\TEST_OUTCUBATOR\\db_connector.properties')
DB_HOST = config.get('DATABASE', 'DB_HOST')
DB_SCHEMA = config.get('DATABASE', 'DB_SCHEMA')
DB_PORT = config.get('DATABASE', 'DB_PORT')
DB_USER = config.get('DATABASE', 'DB_USER')
DB_PWD = config.get('DATABASE', 'DB_PWD')


audit_directory = "D:\\test\\TEST_OUTCUBATOR\\audit"
try:
    engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_SCHEMA}")
    #Check connect to MySQL
    connection = mysql.connector.connect(host=DB_HOST,
                                         database=DB_SCHEMA,
                                         port=DB_PORT,
                                         user=DB_USER,
                                         password=DB_PWD)

    if connection.is_connected():
        print("Connect success")

    for filename in os.listdir(audit_directory):
            if filename.endswith(".csv"):
                csv_path = os.path.join(audit_directory, filename)
                df = pd.read_csv(csv_path)
                
                #Divvy_Trips_2019_Q3.csv -> trips
                #Divvy_Trips_2019_Q4.csv -> station
                if filename == 'Divvy_Trips_2019_Q3.csv':
                    filename = 'trips'
                if filename == 'Divvy_Trips_2019_Q4.csv':
                    filename = 'station'   
                print("Insert table "+filename)         
                df.to_sql(name=filename,con=engine, if_exists='replace', index=False)   
                print("Insert table "+filename+" success !!!!") 
except Error as e:
    print(e)
    