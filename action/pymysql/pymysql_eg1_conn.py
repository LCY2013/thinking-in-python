# Python 3.7连接到MySQL数据库的模块推荐使用PyMySQL模块
# pip install pymysql
# docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DEBUG=yes -d mysql
# 一般流程
# 开始-创建connection-获取cursor-CRUD(查询并获取数据)-关闭cursor-关闭connection-结束
import pymysql

dbInfo = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'database': 'test'
}

sqls = ['select 1', 'select VERSION()']

results = []


class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['database']
        self.sqls = sqls

    def run(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db)
        # 游标建立的时候就会开启一个隐形的事务
        cursor = conn.cursor()
        try:
            for sql in self.sqls:
                cursor.execute(sql)
                # [((1,),), (('8.0.31',),)]
                # results.append(cursor.fetchall())
                # [(1,), ('8.0.31',)]
                results.append(cursor.fetchone())
            cursor.close()
            conn.commit()
        except:
            conn.rollback()
        conn.close()


if __name__ == '__main__':
    db = ConnDB(dbInfo, sqls)
    db.run()
    print(results)
