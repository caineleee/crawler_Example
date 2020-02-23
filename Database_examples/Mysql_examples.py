#coding=utf-8
import pymysql

host = 'localhost'
user = 'root'
password = ''
port = 3306
db = 'spiders'

# 连接 Mysql
db = pymysql.connect(host=host, user=user, password=password, port=port)

# 查询数据库软件版本 执行数据库命令
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)


# 创建数据库
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET UTF8MB4")

# 关闭 数据库
db.close()

# 链接Mysql 并指定数据库
db = pymysql.connect(host=host, user=user, password=password, port=port, db=db)
cursor = db.cursor()

# 创建表
create_table_sql = 'xxxxxxx'
cursor.execute(create_table_sql)

id = '20120001'
name = 'Bob'
age = '20'

# 使用 insert 语句插入数据
insert_data_sql = 'INSERT INTO Students(id, name, age) values(%s, %s, %s)'
try:
	# execute 可以直接将 SQL 中的 python 占位符通过第二个参数(元组), 传入进去函数
	cursor.execute(insert_data_sql, (id, name, age))
	db.commit()
except Exception as e:
	print(e)
	db.rollback()


data = {
	'id': '20120000',
	'name': 'Bob tow',
	'age':'24'
}

Table = 'Students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

# 动态插入数据. 如果数据有变化可以只修改数据, 而不修改 sql 语句
SQL = 'INSERT INTO {Table}({keys}) VALUES({values})'.format(Table=Table, keys=keys, values=values)
try:
	cursor.execute(SQL, tuple(data.values()))
	print('Insert successful!')
	db.commit()
except Exception as e:
	print(e)
	db.rollback()
db.close()


# 更新数据
SQL = 'UPDATE Students SET age = %s WHERE name = %s'
try:
	cursor.execute(SQL, (22, 'Bob tow'))
	db.commit()
except Exception as e:
	print(e)
	db.rollback()
db.close()


# 插入数据去重  如果数据存在则更新数据

SQL = 'INSERT INTO {Table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE '.format(Table=Table, keys=keys, values=values)
Update = ','.join([' {key}= %s'.format(key=key) for key in data])
SQL += Update
try:
	if cursor.execute(SQL, tuple(data.values())*2 ):
		db.commit()
		print('Insert Successful!')
except Exception as e:
	print(e)
	db.rollback()
db.close()


# 删除数据
conditon = 'age > 20'
SQL = 'DELETE FROM Students WHERE {conditon}'.format(conditon=conditon)
try:
	cursor.execute(SQL)
	db.commit()
except Exception as e:
	print(e)
	db.rollback()
db.close()


# 数据查询
table = 'Students'
condition = 'age >= 20'
SQL = 'SELECT * FROM {table} WHERE {condition}'.format(table=table, condition=condition)

try:
	cursor.execute(SQL)
	print('Row Count:', cursor.rowcount)
	one = cursor.fetchone()
	print("One :", one)
	result = cursor.fetchall()
	print('Result:',result)
	for row in result:
		print(row)
except Exception as e:
	print(e)
	db.rollback()
db.close()







