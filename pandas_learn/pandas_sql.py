from sqlalchemy import  create_engine
import pandas as pd

engine = create_engine("postgresql+psycopg2://ratikanta:chiku2010@localhost/dsdb")
connection = engine.connect()
# df = pd.read_csv(r"/Users/ratikantapanda/mydata/datasets/cars.csv",sep=';')
# df.to_sql(con=engine,
#           name='cars',
#           schema='datascience',
#           #if_exists='append',
#           index=False)

# df2=pd.read_sql_table(con=engine, table_name='cars',schema='datascience')
# print(df2)

df2=pd.read_sql('''select * from datascience.cars''',con=engine)
print(df2)