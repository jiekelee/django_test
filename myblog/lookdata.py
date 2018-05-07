import sqlite3


conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

result = c.execute('select * from myCloud_filemodel')
for r in result:
	print(r)
conn.commit()
conn.close()