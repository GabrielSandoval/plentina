from sqlalchemy import create_engine
import pandas as pd

DATABASE_URL = 'mysql://plentina:plentina-db-password@plentina-db.cbbxmhkhubl8.us-east-1.rds.amazonaws.com/plentina'
engine = create_engine(DATABASE_URL)
connection = engine.connect()

transactions = pd.read_csv("data/transactions_train.csv")
transactions.to_sql('transactions', connection, method="multi", chunksize=1000, if_exists="replace")

query = """
        SELECT * from transactions limit 10;
        """
pd.read_sql(query, connection)

