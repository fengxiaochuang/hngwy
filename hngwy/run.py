# python
# -*- coding: utf-8 -*-

from sqlalchemy.sql.elements import and_
from hngwy.model.Category import Category
from hngwy.spiders.DefaultSpider import DefaultSpider
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

engine = create_engine('mysql+mysqldb://root:root@127.0.0.1:3306/hngwy?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
db = DBSession()


def run_spider():
    settings = Settings()
    settings.set("COOKIES_ENABLES", False)  # 禁止cookies追踪
    settings.set("ITEM_PIPELINES", {
    #     'pipelines.ImgPipline': 150,  # 保存图片到本地
    #     # 'pipelines.CoverImagesPipeline': 150, # 保存图片到七牛云
        'hngwy.pipelines.SaveCommonPipline': 200,  # 保存数据库
    #     # 'pipelines.FilterUrlPipline': 300,
    })

    settings.set("DOWNLOADER_MIDDLEWARES", {
        # 'downloaderMiddlewareSet.IngoreHttpRequestMiddleware': 1,  # redis去重
        # 'downloaderMiddlewareSet.CountDropMiddleware': 2,
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,  # 自动useragent
        # 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': None,  # header头很容易造成读取失败,不建议开启
        # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
        'hngwy.downloaderMiddlewareSet.SetUserAgentMiddleware': 400,  # 设置useragent
        # 'downloaderMiddlewareSet.SetHeaderMiddleware': 550,
        # 'downloaderMiddlewareSet.SetProxyMiddleware': 750,  # 设置代理
        # 'downloaderMiddlewareSet.SetUtf8Middleware': 1000,  # 最开始设置字符集过滤用的,不用开启
    })

    # settings.set("LOG_STDOUT ", False)
    # settings.set("CONCURRENT_REQUESTS", 20)
    settings.set("RETRY_ENABLED", True)  # 设置重试,如果开启默认重试3次
    settings.set("REDIRECT_ENABLED", False)  # 重定向类网站是否采集
    # settings.set("AJAXCRAWL_ENABLED", True)
    settings.set("DOWNLOAD_DELAY", 3)  # 延迟下载
    settings.set("DOWNLOAD_TIMEOUT", 15)  # 下载超时的阈值,超过15秒就关闭连接

    # configure_logging()
    # 初始化日志路径

    # 拼装爬虫
    process = CrawlerProcess(settings)
    rules = db.query(Category).filter(and_(Category.status > 0, Category.pid > 0)).all()

    for rule in rules:
        process.crawl(DefaultSpider, rule)
    #process.crawl(DefaultSpider, rules[0])
    process.start()


if __name__ == '__main__':
    run_spider()
