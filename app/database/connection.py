
import pyodbc

class ConnectionManager:
    def __init__(self):


        server = 'localhost'  # or '127.0.0.1'
        port = '1433'
        database = 'master'  # Default database
        username = 'sa'
        password = 'PASSword8'  # Your password
        driver = '{ODBC Driver 18 for SQL Server}'  # Most common
        taskdb = 'somedb'
        # Connection string
        conn_str = f'DRIVER={driver};SERVER={server},{port};DATABASE={database};UID={username};PWD={password};Encrypt=no;TrustServerCertificate=yes'


        self.congif = conn_str
        self.connection = None

        self.connect()

        

    def connect(self):
        if not self.connection:
            # You MUST call the function with your config string here
            self.connection = pyodbc.connect(self.congif) 

        return self.connection
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
        print("Connection closed.")
        






    