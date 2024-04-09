# 1.Приложение телемастерская для автоматизированного контроля
# работ по ремонту бытовой техники. БД должна содержать таблицу
# Ремонт телевизоров, имеющую следующую структуру записи:
# Марки телевизора, Завод-изготовитель, Цена, Дата ремонта,
# Документ, Мастер, Сумма оплаты.
import sqlite3 as sq
from Info_insert import info

with sq.connect("Tv_workshop.db") as con:
    cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS tv_repair( 
tv_brand varchar(10),
factory varchar NOT NULL,
price decimal(9),
repair_date varchar NOT NULL,
doc integer PRIMARY KEY NOT NULL,
master varchar NOT NULL,
sum_price decimal(10) NOT NULL
)""")
cur.executemany("""insert into tv_repair values(?, ?, ?, ?, ?, ?, ?) """, info)

# cur.execute("""select * from tv_repair WHERE sum_price < 1000""")
# frs = cur.fetchall()
# cur.execute("""select * from tv_repair WHERE master = 'David Kelson'""")
# srs = cur.fetchall()
# cur.execute("""select * from tv_repair WHERE doc = 1 and 4""")
# trs = cur.fetchall()
#
# print(frs, srs, trs, sep="\n")
#
# cur.execute("""update tv_repair set sum_price = 8000 where tv_brand like 'LG'""")
# cur.execute("""select * from tv_repair""")
# fru = cur.fetchall()
# cur.execute("""update tv_repair set master = 'Coul Fovir' where doc like 9""")
# cur.execute("""select * from tv_repair""")
# sru = cur.fetchall()
# cur.execute("""update tv_repair set factory = 'NEEF' where price > 1000""")
# cur.execute("""select * from tv_repair""")
# tru = cur.fetchall()
#
# print(fru, sru, tru, sep="\n")
#
# cur.execute("""delete from tv_repair WHERE doc = 3 and 6 and 9""")
# cur.execute("""select * from tv_repair""")
# frd = cur.fetchall()
# print(frd)
# cur.execute("""delete from tv_repair WHERE tv_brand = 'XIAOMI'""")
# cur.execute("""select * from tv_repair""")
# srd = cur.fetchall()
# print(srd)
# cur.execute("""delete from tv_repair WHERE price between 15000.00 and 25000.00""")
# cur.execute("""select * from tv_repair""")
# trd = cur.fetchall()
# print(trd)

