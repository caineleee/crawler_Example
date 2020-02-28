#coding=utf-8

from redis import StrictRedis, ConnectionPool

# 连接redis 数据库
redis = StrictRedis(host='localhost', port=6379, db=0)
# StrictRedis 等价于 ConnectionPool(host='localhost', port=6379, db=0)

# key 不存在就创建一个键值对, 否则就更新 value
# redis.set('name', 'Bob')

# 获取 key 的 value
# print(redis.get('name'))


# 判断一个key 是否存在
# print(redis.exists('name'))


# 删除一个key
# redis.delete('name')


# 判断 key 类型
# print(redis.type('name'))


# 通过正则获取所有符合类型的 key, 不过这里也不是什么普通正则规范, .* 貌似就不好使
# print(redis.keys('n*'))


# 获取随机的一个值
# print(redis.randomkey())


# key 重命名
# redis.rename('name','nikename')


# 获取当前数据库 key 的数量
# print(redis.dbsize())


# 设置 key 的过期时间 单位为秒
# redis.expire('name', 2)


# 获取 key 的过期时间. 单位为秒  -1 代表永不过期
# print(redis.ttl('name'))


# 移动key 到其他的数据库
# redis.move('name',2) # 2为数据库代号


# 删除当前选择数据库数据
# redis.flushdb()


# 删除所有数据库数据
# redis.flushall()


#  -------  string 相关 --------

# 给 key 赋予新 value 并返回原本 value
# print(redis.getset('name', 'Jerry'))


# 返回多个 key 的 value
# print(redis.mget(['name', 'nikename']))


# 如果 key 不存在就创建键值对, 否则保持不变
# redis.setnx('newname', 'James')


# 给 key 赋值, 并且设置过期时间. 单位为秒
# redis.setex('name', 1, 'James')


# 在 string value 中指定的位置插入文本内容, offset 为偏移量
# redis.setrange('name', 6, 'emmm... haha')


# 批量赋值
# data = {'name1':'Durant', 'name2':'James'}
# redis.mset(data)


# key 若存在 value 做加法, 如果 key 不存在则直接创建
# redis.incr('age', 1)
# redis.incr('age', 1)

# 与 incr 相反, 给 value 做减法, key 不存在则直接创建
# redis.decr('age',1)


# 在 value 的后面追加内容
# redis.append('name1', ' Hello')


# 返回 value 指定的 start index / end index 之间的内容. 只支持 string 类型
# print(redis.substr('name1',2, -2))  # getrange() 也效果对于字符串  等同



#  -------  List 相关 --------

# 在指定的 key 的list 末尾增加元素. 如果 key 不存在则直接创建
# redis.rpush('list', 1, 2, 3)


# 与 rpush 相反, 在表的开头插入元素
# redis.lpush('list', -1, 0)


# 返回列表长度
# print(redis.llen('list'))


# 返回指定 index 范围之间的 values
# print(redis.lrange('list',1,3))


# 根据 key 和 value 返回 value 在 list 中的 index
# print(redis.lindex('list', -1))   # 但是 value 如果是字符串貌似在这里不能取出来?


# 给列表中指定的 index 赋值
# redis.lset('list', 0, -1)



# 列表中指定 value 删除, 并指定删除个数
# redis.lrem('list', 2, -1) # 2为个数, -1 为指定value


# 删除列表中的第一个元素, 并将该value 返回
# print(redis.lpop('list'))


# 与 lpop 类型的删除, 但是如果列表为空则会阻塞等待
# print(redis.blpop('list'))


# 与 blpop 相反, 删除列表中的末尾元素, 如果为空则阻塞等待
# print(redis.brpop('list'))


# 将一个 List 的尾元素, 并将其添加到另外一个 list 的头部
# redis.rpoplpush('list', 'list2')


# ---------- 集合操作 -----------
# 集合中的元素都是不重复的

# 集合添加元素,如果 key 不存在则直接创建. 第一个参数为 key, 其余的为 value
# redis.sadd('tags', 'Book', 'Tea', 'Coffee')


# 返回集合的所有 value
# print(redis.smembers('tags'))


# 随机返回集合中的一个元素, 但不删除元素
# print(redis.srandmember('tags'))


# 集合删除指定元素
# redis.srem('tags', 'Book')


# 从一个集合中移除一个 value, 并将其加入另一个 集合. 如果该后者集合不存在则直接创建
# redis.smove('tags', 'tags2', 'Coffee')


# 随机删除集合中的一个 value, 并将其返回
# print(redis.spop('tags'))


# 返回集合的长度
# print(redis.scard('tags'))


# 判断 value 是否存在于为集合中
# print(redis.sismember('tags', 'Book'))


# 返回多个集合中, 共同存在的值
# print(redis.sinter(['tags','tags2']))


# 将多个集合中, 共同存在的 value 保存到一个指定的集合中
# redis.sinterstore('inttag', ['tags', 'tags2']) # 将List中集合共同存在的 value 写入第一个集合中


# 将多个集合所有元素返回
# print(redis.sunion(['tags', 'tags2']))


# 将多个集合所有元素合并成一个新的集合, 如果新的集合已经存在, 则将其原本数据覆盖
# redis.sunionstore('inttag', ['tags', 'tags2'])


# 返回多个集合的差集(互相不包含的 value)
# print(redis.sdiff(['tags', 'tags2']))


# 求差集并赋值给新集合
# redis.sdiffstore('inttag', ['tags', 'tags2'])



# --------- 有序集合 ---------
# 有序集合比集合多了一个分数字段, 可以对集合中的数据排序. 有序集合中的 score 用于排序


# key 不存在就直接创建, 否则新增 value.  100/ 98 为 score
# redis.zadd('grade', 100, 'Bob', 98, 'Mike')


# 删除指定 value
# redis.zrem('grade', 'Mike')


# 增加指定 value 的 score 数字.
# redis.zincrby('grade', 'Bob', 2)  # score number + 2


# 获取指定 value 的倒数排名
# print(redis.zrevrank('grade', 'Mike'))


# 根据 score 倒叙排序, 获取集合中 index 指定范围的 values
# print(redis.zrevrange('grade', 0, 3))


# 返回集合中指定 score 范围内的所有 values
# print(redis.zrangebyscore('grade', 42, 98))
# print(redis.zrangebyscore('grade', 42, 98, withscores=True))  # 返回结果带有 score


# 返回指定 score 区间范围内元素的数量
# print(redis.zcount('grade', 42, 98))


# 返回集合年内所有 value 的数量
# print(redis.zcard('grade'))


# 删除集合中排名在指定区间的 values
# redis.zremrangebyrank('grade', 3, 5)


# 删除集合中score 在指定区间的 values
# redis.zremrangebyscore('grade', 40, 97)


# --------- 散列表 --------
# 将 value 设置为一个 键值对类型

# 如果 key 存在则更新散列表 映射 key 的 value, 否则直接创建散列表
# redis.hset('price', 'cake', 3)


# 如果映射 key 不存在则在散列表中添加映射键值对. 否则不做更改
# redis.hsetnx('price', 'book', 4)


# 获取散列表中指定映射 key 的 value
# print(redis.hget('price', 'cake'))


# 获取散列表中多个指定映射 key 的 value
# print(redis.hmget('price', ['cake', 'book']))


# 向散列表中批量新增/更新映射数据
# redis.hmset('price', {'apple':2, 'orange':7})


# 给映射 value 做加法
# redis.hincrby('price', 'apple', 2)


# 判断映射 key 是否存在
# print(redis.hexists('price','banana'))


# 删除一个映射键值对
# redis.hdel('price', 'banana')


# 获取散列表长度
# print(redis.hlen('price'))


# 获取散列表中所有映射 key
# print(redis.hkeys('price'))


# 获取散列表中所有映射 value
# print(redis.hvals('price'))


# 获取散列表中所有映射键值对
# print(redis.hgetall('price'))






























