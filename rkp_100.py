# import psycopg2
# conn = psycopg2.connect(
#     host="localhost",
#     database="rkpdb101",
#     user="ratikanta",
#     password="chiku2010")
#
# cur = conn.cursor()
# cur.execute('''select * from rkp_company.employee;''')
# for row in cur:
#     print(row)
#
# conn.commit()
# conn.close()
#
# # print("hello")
from sqlalchemy import  create_engine
engine = create_engine("postgresql+psycopg2://ratikanta:chiku2010@localhost/rkpdb101")
connection = engine.connect()

my_query = 'SELECT * FROM rkp_company.employee'
try:
    results = connection.execute(my_query).fetchall()
    print(results)
except:
    print("error")