import pyodbc, warnings

#print(pyodbc.drivers())
#Global connection string
conn_string = 'DRIVER={ODBC Driver 11 for SQL Server}; SERVER=CTMRNETAL508BRG; DATABASE=master; trusted_connection=yes;'


def create_db(db_name):

    """
    Creates a MSSQL Database if not already exists, catches any warnings and executes statement or handles exception.
    """

    try:

        with pyodbc.connect(conn_string, autocommit=True) as connection:

            with warnings.catch_warnings():
            
                warnings.simplefilter('error')

                cursor = connection.cursor()

                result = cursor.execute(f'CREATE DATABASE {db_name}')

                return f'Database: {db_name} created successfully \n{result}'

    except Exception as other:

        #return f'Database: "{db_name}" already exists'
        return f'{other}'

#print(create_db('hifld'))

def table_exists(db_name, table):

    """
    Checks for the existance of a table in given MSSQL Database. Uses pyodbc.
    """

    conn_string_local = f'DRIVER={{ODBC Driver 11 for SQL Server}}; SERVER=CTMRNETAL508BRG; DATABASE={db_name}; trusted_connection=yes;'

    try:
        with pyodbc.connect(conn_string_local, autocommit=True) as connection:

            with warnings.catch_warnings():

                warnings.simplefilter('error')

                cursor = connection.cursor()

                if cursor.tables(table = f'{table}', tableType = 'TABLE').fetchone():

                    return True

                else:

                    return False

    except Exception:
        return 'DB connection failed'

#print(table_exists('energy', "biodiesel_plants"))