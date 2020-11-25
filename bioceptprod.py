  # -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:09:24 2020

@author: Heeje Cho

Module contains several methods for working with the database LiquidBigData
- bp_connect
    inputs: username and password
    output: connection, cursor
    *this connects to LiquidBigData with credentials
- bp_reports
    inputs: connection, query
    output: report (in pandas dataframe)
    *this updates the ScriptActivity table with ScriptId, UserId, Successful, ActivityTime and ActivityMessage
"""

import pyodbc
import pandas as pd

def connect(username,password):

    config = {
        'server': 'bioceptprod-sql.database.windows.net',
        'database': 'bioceptprod',
        'username': username,
        'password': password,
        'driver': '{SQL Server}'
    }
    
    connection_string =  'DRIVER=' + config['driver'] + \
                        ';SERVER=' + config['server'] + \
                        ';PORT=1433' + \
                        ';DATABASE=' + config['database'] + \
                        ';UID=' + config['username'] + \
                        ';PWD=' + config['password'] 
    
    connection = pyodbc.connect(connection_string)
    
    return connection





def reports(connection, query):

    report = pd.read_sql(query, connection)

    return report