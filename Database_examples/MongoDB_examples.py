#coding=utf-8

import pymongo

host = 'localhost'
port = 27017

# 连接 mongodb
client = pymongo.MongoClient(host=host, port=port)

# 或者之间传入 mongo 链接字符串
# clinet = pymongo.MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client.test  # 等价于 db = client['test']

# 指定 collection

collection = db.students


student = {
	'id': '20120000',
	'name': 'Bob tow',
	'age':'24'
}

# 插入单挑数据
result = collection.insert_one(student)
print(result.insert_id)

# 插入多条数据
students = [
{
	'id': '20120001',
	'name': 'Jordan',
	'age':'24'
},
{
	'id': '20120002',
	'name': 'Mike',
	'age':'24'
}
]

result = collection.insert_many(students)
print(result.insert_ids)


# 单条数据查询 根据数据内容查询
result = collection.find_one({'name':'Mike'})
print(result)


# 根据 ObjectId 查询
from bson.objectid import ObjectId

result = collection.find_one({'_id': ObjectId('5e5213deaa742ea8f45a45de')})
print(result)


# 多条数据查询
result = collection.find({'age':'24'})
for record in result:
	print(record)

# $lt:小于     $gt:大于    $ltq:小于等于    $gte:大于等于   $ne:不等于    $in:范围内    $nin:不在范围内
result = collection.find({'age':{'$gt': '20'}})
for record in result:
	print((record))



# 正则匹配查询
result = collection.find({'name': {'$regex': '^M.*'}})
for record in result:
	print((record))


# 计数
count = collection.find({'age':{'$gt': '20'}}).count()  # count() 方法为已过时的方法, 虽然还可以使用但是最好使用新的方法 count_documents()
print(count)
count = collection.count_documents({'age':{'$gt': '20'}})
print(count)

# 排序  升序为 pymongo.ASCENDING  降序为 pymongo.DESCENDING
result = collection.find({'age':{'$gt': '20'}}).sort('name',pymongo.ASCENDING)
for i in result:
	print(i)


# 偏移 代表偏移几个位置
result = collection.find({'age':{'$gt': '20'}}).skip(2)
for i in result:
	print(i)


# 指定返回数据个数
result = collection.find().limit(2)
print([i for i in result])


# 更新数据
condition = {'name':'Bob tow'}
student = collection.find_one(condition)
student['age'] = '21'
student['name'] = 'Ricky'
# # '$set' 表示如果数据中有 student 字典之外的字段则不会更新. 只更新 student 字典包含的字段
result = collection.update_one(condition,{'$set': student})
print(result.matched_count, result.modified_count)


# 数据删除
condition = {'name':'Bob tow'}
result = collection.delete_one(condition)
print(result.delete_count)








