# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 11:14:45 2023

@author: Sai khiarnar
"""

from sqlalchemy import create_engine
import pandas as pd

data= pd.read_csv('C:/Users/ABC/Documents/Business_analytics_python/DATA/User_Data.csv')

#create the relational database
engine = create_engine('sqlite:///:memory:')
data.to_sql('data_table',engine)
res1 = pd.read_sql_query('SELECT * FROM data_table', engine)
print(res1)

res2 = pd.read_sql_query('SELECT Gender,Age,EstimatedSalary FROM data_table', engine)
print(res2)

#inserting data into relational tables
from sqlalchemy import create_engine
from pandas.io import sql
import pandas as pd

data1= pd.read_csv('C:/Users/ABC/Documents/Business_analytics_python/DATA/User_Data.csv')
#store the data in relational table
engine= create_engine("sqlite:///:memory:")
data.to_sql('data_table',engine)

#insert another row
sql.execute('INSERT INTO data_table VALUES(?,?,?,?,?,?)',engine,params=[(399,15078964,'Female',45,34569,0)])
#read from relational table
res4 = pd.read_sql_query('SELECT * FROM data_table', engine)
print(res4)

#delete value from relational database
from sqlalchemy import create_engine
from pandas.io import sql
import pandas as pd

data1= pd.read_csv('C:/Users/ABC/Documents/Business_analytics_python/DATA/User_Data.csv')
#store the data in relational table
engine= create_engine("sqlite:///:memory:")
data.to_sql('data_table',engine)

#insert another row
sql.execute('DELETE from data_table where Age =(?)',engine,params=[19])
#read from relational table
res4 = pd.read_sql_query('SELECT * FROM data_table', engine)
print(res4)







