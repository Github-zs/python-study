import pymysql as p
import configparser
import os

root_path = os.path.dirname(os.path.abspath('..'))
conf = configparser.ConfigParser()
# 读取配置文件要写绝对路径
# 字符串拼接  s1.join(s2) (s1, '' ,s2) s1 + s2
config_path = os.path.join(root_path, 'confiig.ini')
conf.read(config_path, encoding='utf-8')

# host默认为localhost  port默认为3306
# conn = p.connect(user="root", passwd="123456", db="dbname")
# config = conf.items('Mysql')
# conn = p.connect(user=config[3][1], passwd=config[4][1], db=config[5][1])
user = conf.get('Mysql', 'user')
passwd = conf.get('Mysql', 'password')
db = conf.get('Mysql', 'database')

conn = p.connect(user=user, passwd=passwd, db=db)
print(conn)

c = conn.cursor()

getone = "select * from quapi_data_document where id = '1c63d653c76449839ca6c7e412c4ac04'"
c.execute(getone)
document = c.fetchone()
print(document)

print(document[17])