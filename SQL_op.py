#coding=utf-8
__author__ = 'chexiaoyu'

import MySQLdb
import crawl

class Sql_op:

    def __init__(self):
        self.conn = MySQLdb.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'hive',
            passwd = 'hive',
            db = 'test_cxy',
        )
        self.cursor = None

    def connect(self):
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()


    def tb_create(self):
        sql = "create table population_code" \
              "(" \
              "id int(11) unsigned not null auto_increment primary key," \
              "population int," \
              "code varchar(10) not null" \
              ")" \
              "auto_increment = 10000000"
        self.cursor.execute(sql)

    def tb_insert(self,stories,sql):
        # sql = "insert into population_code(code,city) values('1','1')"
        # print self.cursor.execute(sql)
        #print self.cursor.rowcount
        for item in stories:
            self.cursor.execute(sql,item)
            self.conn.commit()

    def tb_list(self):
        sql = "select * from China_GDP"
        self.cursor.execute(sql)

    def merge(self,stories1,stories2):





if __name__ == "__main__":
    op = Sql_op()
    cr = crawl.Crawl()
    op.connect()
    #op.tb_create()
    cr.get_GDP()
    #print cr.stories_cities

    #sql = "insert into city_code(city,code) values(%s,%s)"
    #op.tb_insert(cr.stories_cities,sql)

    sql = "insert into population_code_time(population,code,time_year) values(%s,%s,%s)"
    op.tb_insert(cr.stories_population,sql)
    #op.tb_list()
    op.close()


# try:
#     cursor = conn.cursor()
#     #cursor.execute(tb_create())
#     #cursor.execute("alter table China_GDP auto_increment = 100000000000")
#     cursor.execute(tb_insert())
#     cursor.close()
#     conn.close()
# except MySQLdb.Error, e:
#     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

