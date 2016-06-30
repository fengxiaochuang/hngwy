# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib

from scrapy.exceptions import DropItem
from sqlalchemy import exc

from hngwy.model.Page import Page
from hngwy.run import DBSession


class HngwyPipeline(object):
    def process_item(self, item, spider):
        return item


class SaveCommonPipline(object):
    def process_item(self, item, spider):
        db = DBSession()
        md5 = hashlib.md5()
        md5.update(item['url'])
        urlmd5 = md5.hexdigest()
        page = Page(url=item["url"], urlmd5=urlmd5, title=item["title"], category=spider.conf.id, date=item["date"],
                    content=item["content"])
        db.add(page)
        try:
            db.commit()
        except exc.SQLAlchemyError, e:
            raise DropItem("SaveError: %s:%s [%s]" % (item['title'], item['url'], format(e)))
        finally:
            db.close()
