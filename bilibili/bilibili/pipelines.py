# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql


class BilibiliPipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(host="127.0.0.1",
                                  port=3306,
                                  user="root",
                                  password="root",
                                  database="bilibili")
        self.cursor = self.db.cursor()
        print("连接成功！")

    def process_item(self, item, spider):

        sql = """INSERT INTO video(`title`, `author`, `like_count`, `coin_count`,
                                    `collect_count`, `view_count`, 
                                    `dm_count`, `bv`, `dm`)
         VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"""

        values = ( item["title"], item["author"], item["like_count"], item["coin_count"],
                item["collect_count"], item["view_count"], item["dm_count"], item["bv"], item["dm"])


        try:
            self.cursor.execute(sql, values)
            self.db.commit()
        except Exception as e:
            print("插入数据出错")
            print(e)
            self.db = pymysql.connect(host="47.106.76.161",
                                      port=3306,
                                      user="root",
                                      password="root",
                                      database="bilibili")
            self.cursor.execute(sql, values)
            self.db.commit()

        return item

    def close_spider(self, spider):
        self.db.close()




