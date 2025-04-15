import pyodbc

def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=pruebapython.database.windows.net;'
        'DATABASE=BetterService;'
        'UID=itgala95;'
        'PWD=Stratosphere1.;'
    )
    print("Conexión exitosa a la base de datos.")
 
    return conn

 

