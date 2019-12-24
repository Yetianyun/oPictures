#将数据写入数据库
#使用pymysql连接mysql数据库
import pymysql
import configparser

def pyconn():
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    section = 'mysql'
    conf = {
        'host': config.get(section, 'host'),
        'port': config.getint(section, 'port'),
        'user': config.get(section, 'user'),
        'passwd': config.get(section, 'password'),
        'db': config.get(section, 'database'),
        'charset': config.get(section, 'charset')
    }
    conn = pymysql.connect(**conf)

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select version()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    # 输出查询的数据：
    print("Database Version: %s" % data)
    # 关闭数据库连接e
    conn.close()
    return conn


if __name__ == "__main__":
    pyconn()



