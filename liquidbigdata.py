  # -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:09:24 2020

@author: Heeje Cho

Module contains several methods for working with the database LiquidBigData
- lbd_connect
    inputs: username and password
    output: connection, cursor
    *this connects to LiquidBigData with credentials
- lbd_log_script
    inputs: connection, script_id, user_id, successful_bit, activity_message
    output: none
    *this updates the ScriptActivity table with ScriptId, UserId, Successful, ActivityTime and ActivityMessage
- lbd_lastrun
    inputs: connection, scriptid
    output: datetime (SQL datetime string of when script was last run)
"""

import pyodbc

def connect(username,password):

    config = {
        'server': 'bio-powerbi-bigdata.database.windows.net',
        'database': 'LiquidBigData',
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





def log_script(connection, script_id, user_id, successful_bit, activity_message):

    cursor = connection.cursor()
    
    query = f'''
                INSERT INTO [dbo].[ScriptActivity]
                           ([ScriptId]
                           ,[UserId]
                           ,[Successful]
                           ,[ActivityTime]
                           ,[ActivityMessage])
                     VALUES
                           (?
                           ,?
                           ,?
                           ,GETDATE()
                           ,?)
            '''

    cursor.execute(query,script_id,user_id,successful_bit,activity_message)
    connection.commit()

    return None





def lastrun(connection, script_id):

    cursor = connection.cursor()

    #this query returns the last run datetime of the script in PST (converted from UTC)
    query = f'''
                SELECT DATEADD(MINUTE,-420,MAX(ActivityTime)) FROM dbo.ScriptActivity WHERE ScriptId = \'{script_id}\' AND Successful = 1
            '''

    cursor.execute(query)

    for row in cursor.fetchall():
        lastrun = row
    
    lastrun = lastrun[0].strftime('%Y-%m-%d %X')
    
    return lastrun