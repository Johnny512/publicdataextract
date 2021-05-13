#import MySql library and sqlaclchemy
import pymysql, warnings

from sqlalchemy import create_engine

# Global variables used in each function
db_name = 'ECI'

conn_string = f'mysql+pymysql://jcastillo:SuperSecretPassword@austx-galera-node-02.chtrse.com:3306/{db_name}'

def mariadb_write(table, df):
    """
    Writes a dataframe to Maria DB Database. Database library must be imported from calling script.
    """

    engine = create_engine(conn_string, echo=False)

    try:
        with engine.connect() as connection:

            df.to_sql(table, con=connection)

            return f'Table: "{table}" written to db "{db_name}"'

    except:
        
        return f'Table: "{table}" already exists.'  

def create_db(db_name):
    """
    Creates a database if not already exists, catches any warnings and executes statement or handles exception.
    """
    
    try:

        engine = create_engine(conn_string, echo=False)

        with engine.connect() as connection:
        
            with warnings.catch_warnings():
                
                # This converts any warning into an exception
                warnings.simplefilter('error')

                connection.execute(f'CREATE DATABASE IF NOT EXISTS {db_name};')

                return f'Database: {db_name} created successfully'
        
    except:

        return f'Database: "{db_name}" already exists'

def table_exists(table):
    """
    https://stackoverflow.com/questions/40652938/flask-sqlalchemy-check-if-table-exists-in-database?rq=1
    """
    try:
        conn_string_table = f'{conn_string}'

        engine = create_engine(conn_string_table, echo=False)
    
        ret = engine.dialect.has_table(engine, table)
    
        return ret

    except Exception as e:

        return e

    engine.close()