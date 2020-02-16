#coding=utf-8

# Fibonacci(斐波那契数列)

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1



# 编写一个迭代类 实现 fibonacci 数列. 可以有效的减少内存占用

class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()




# 使用 yield 实现 fibonacci 数列. 可以有效的简化迭代类的代码实现.

def fab_yield(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        a, b = b, a + b
        # n = n + 1

if __name__ == '__main__':
    # fab(5)
    # for n in Fab(5): print(n)
    for n in fab_yield(5): print(n)

