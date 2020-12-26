# -*- coding: utf-8 -*-
import os
import os.path

# 操作系统类型
print(os.name)

# 详细的系统信息(仅Unix系)
print(os.uname())

# 环境变量
print(os.environ)
assert os.environ['PATH'] == os.environ.get('PATH')
assert os.environ.get('notakey', 'df') == 'df'

# 查看当前目录的绝对路径
print(os.path.abspath('.'))

# 在父目录下创建子目录，并返回子目录绝对路径(父目录不支持相对路径)
# 会根据操作系统的选择路径分隔符
assert os.path.join('/Users/huzihao/PycharmProjects/pythonProject/oop/myio',
                    'kid') == '/Users/huzihao/PycharmProjects/pythonProject/oop/myio/kid'

# 创建目录（存在则抛出FEE）
os.mkdir('./dir')

# 删除目录(不存在则抛出FNFE)
os.rmdir('./dir')

# 拆分成两部分，最后一部分为最后的目录或文件
assert os.path.split('hello/file.txt') == ('hello', 'file.txt')

# 获得文件扩展名
assert os.path.splitext('hello/file.py') == ('hello/file', '.py')

try:
    # 文件重命名
    os.rename('test.txt', 'test.py')

    # 删除文件
    os.remove('test.py')
except FileNotFoundError:
    pass

# 当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 当前目录下的所有.py
print([x for x in os.listdir('.') if
       os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
