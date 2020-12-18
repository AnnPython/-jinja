
from jinja2 import Template
import sqlite3

conn = sqlite3.connect('chinook.db')
c = conn.cursor()

sql = c.execute('SELECT FirstName, LastName, Address, Email FROM customers;')
cust = []
for i in sql:
    cust.append(i)
conn.close()


html = open('table.txt').read()

template = Template(html)
render = template.render(cust = cust)

f = open('custom.html', 'w',encoding='utf-8')
f.write(render)
f.close()

