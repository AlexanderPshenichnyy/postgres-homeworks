"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os
import psycopg2

PATH_TO_CSV = 'north_data'


def db(table_name, path, csv_file):
	with psycopg2.connect(
			host='localhost',
			database='north',
			user='postgres',
			password=os.getenv('psql_pass')
	) as conn:
		conn.autocommit = True
		with conn.cursor() as cur:
			with open(f'{path}/{csv_file}', 'r', encoding='utf-8') as file:
				reader = csv.reader(file)
				next(reader)
				for i in reader:
					sql = f'insert into {table_name} values ({", ".join(["%s"] * len(i))})'
					cur.execute(sql, i)
					cur.execute(f'select * from {table_name}')
					new_table = cur.fetchall()
					for j in new_table:
						print(j)

	conn.close()


# queries = ['north_data/orders_data.csv'
# 'north_data/employees_data.csv',
# 'north_data/customers_data.csv']

db('customers', PATH_TO_CSV, 'customers_data.csv')
db('employees', PATH_TO_CSV, 'employees_data.csv')
db('orders', PATH_TO_CSV, 'orders_data.csv')
