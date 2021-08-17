import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="rkpdb101",
    user="ratikanta",
    password="chiku2010")

cur = conn.cursor()
cur.execute('''select * from rkp_company.employee;''')
for row in cur:
    print(row)

conn.commit()
conn.close()
