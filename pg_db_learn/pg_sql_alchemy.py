from sqlalchemy import  create_engine

engine = create_engine("postgresql+psycopg2://ratikanta:chiku2010@localhost/rkpdb101")
connection = engine.connect()

my_query = 'SELECT * FROM rkp_company.employee'
results = connection.execute(my_query).fetchall()
print(results)
print("error")