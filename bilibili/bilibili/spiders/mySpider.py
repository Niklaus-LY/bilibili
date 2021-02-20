import re
import time
import scrapy
from bilibili_api import video

from ..items import BilibiliItem


class MyspiderSpider(scrapy.Spider):
    """从排行榜的100个视频开始，聚焦爬虫，根据热度和点赞等来爬取"""


    name = "bilibili"
    title_set = set()
    start_urls = ["https://www.bilibili.com/v/popular/rank/all"]

    def parse(self, response):
        urls = response.xpath("//ul[@class='rank-list']//li//div[@class='info']/a/@href").getall()
        for url in urls:
            yield scrapy.Request(url="https:" + url, callback=self.parse_video, priority=500)

    def parse_video(self, response):
        like_count = response.xpath("//div[@class='ops']/span[@class='like']//text()").get().strip()
        coin_count = response.xpath("//div[@class='ops']/span[@class='coin']//text()").get().strip()
        collect_count = response.xpath("//div[@class='ops']/span[@class='collect']//text()").get().strip()

        if like_count[-1] == "万" and coin_count[-1] == "万" and collect_count[-1] == "万":
            # 增量爬取

            view_count = response.xpath("//div[@class='video-data']/span[@class='view']/text()").get()
            dm_count = response.xpath("//div[@class='video-data']/span[@class='dm']/text()").get()

            title = response.xpath("//h1[@class='video-title']/@title").get()
            author = response.xpath("//div[@id='v_upinfo']//div[@class='name']/a/text()").get()
            like_count = float(like_count[:-1])
            coin_count = float(coin_count[:-1])
            collect_count = float(collect_count[:-1])
            view_count = float(view_count.split("万")[0]) if "万" in view_count else float(view_count.split("播放")[0])/10000
            dm_count = float(dm_count.split("万")[0])  if "万" in dm_count else float(dm_count.split("弹幕")[0]) / 10000
            bv = [i for i in response.url.split("/") if i.startswith("BV")][0]

            danmakus = video.get_danmaku(bvid=bv)
            dm_list = []
            for d in danmakus:
                if str(d).split(",")[-1]:
                    dm_list.append(str(d).split(",")[-1].strip())
            dm = "  ".join(dm_list)

            if title[:8] not in self.title_set:
                self.title_set.add(title[:8])
                item = BilibiliItem()
                item["title"] = title
                item["author"] = author
                item["like_count"] = like_count
                item["coin_count"] = coin_count
                item["collect_count"] = collect_count
                item["view_count"] = view_count
                item["dm_count"] = dm_count
                item["bv"] = bv
                item["dm"] = dm

                yield item

                rec_list = response.xpath("//div[@class='rec-list']//div[@class='info']/a/@href").getall()
                for u in rec_list:
                    time.sleep(0.2)
                    yield scrapy.Request(url="https://www.bilibili.com" + u, callback=self.parse_video, priority=200)




