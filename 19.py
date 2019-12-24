#使用pymysql连接mysql数据库
import  pymysql


def pyconn():
    # 打开数据库连接
    conn = pymysql.connect(host="localhost", user="root", password="Woyaojiayou123!",
                           database="scanWords", port=3306)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select version()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    # 输出查询的数据：
    print("Database Version: %s" % data)
    # 关闭数据库连接
    conn.close()


if __name__ == "__main__":
    pyconn()

