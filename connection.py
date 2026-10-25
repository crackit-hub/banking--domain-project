import pandas as pd

import mysql.connector
from sqlalchemy import create_engine

conn=mysql.connector.connect(host="localhost",
                             user="root",
                             password="root",
                             database="banking_case")
engine=create_engine("mysql+mysqlconnector://root:root@localhost/banking_case", echo=False)

query= 'SELECT * FROM customer'
df=pd.read_sql(query,conn)
print(df)