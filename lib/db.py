import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text

from lib.constants import DATABASE_URL

def create_db_connection():
    engine = create_engine(DATABASE_URL)
    return engine.connect()

def insert_transaction(conn, data):
    statement = text(
        """
        INSERT INTO transactions(
            step, type, amount,
            nameOrig, oldbalanceOrig, newbalanceOrig,
            nameDest, oldbalanceDest, newbalanceDest
        ) VALUES(
            :step, :type, :amount,
            :nameOrig, oldbalanceOrig, newbalanceOrig,
            :nameDest, oldbalanceDest, newbalanceDest
        )
        """
    )
    conn.execute(statement, data)

def query_transactions(conn, filters):
    statement = text(
        """ SELECT * from transactions
        WHERE step = :step
        AND nameOrig = :nameOrig
        """
    )
    return conn.execute(statement, filters)
