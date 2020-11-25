  # -*- coding: utf-8 -*-
"""
Created on Tuesday Nov 24 14:56:00 2020

@author: Heeje Cho

Module contains class MSSQL_Hook for connecting to and operating with MsSQL databases.

"""

import sqlalchemy as sa
import pandas as pd
import urllib

class MsSQLHook:

    def __init__(self,server,database,username,password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.driver = '{ODBC Driver 17 for SQL Server}'
        self.port = '1433'

        #conection string
        self.connection_string = 'DRIVER=' + '{SQL Server}' + \
                        ';SERVER=' + server + \
                        ';PORT=1433' + \
                        ';DATABASE=' + database + \
                        ';UID=' + username + \
                        ';PWD=' + password
        self.params = urllib.parse.quote_plus(self.connection_string)
        self.engine = sa.create_engine("mssql+pyodbc:///?odbc_connect=%s" % self.params)

    def sql_to_df(self, query):
        if ".sql" in query:
            sql_command = open(query, mode = 'r', encoding='utf-8-sig').read()
        else:
            sql_command = query

        df = pd.read_sql(sql_command, con = self.engine)

        return df