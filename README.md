# hngwy
河南公务员考试网

### 目标
- 爬虫获取相应栏目的试题
- 将相应的试题转换成word文档

### 实现
- 采用scrapy简单的抓取到试题内容
- 用dom + regex 过滤相应的垃圾信息
- 在数据库根据月份筛选整合的内容
- 拼接内容为html
- html生成word

###### 坑
- html生成word真的是好艰辛的过程,几个小时没搞定就放弃了
- 采用的是exe二进制外挂程序调用转换
- 需要下载安装pandoc
- 万恶的乱码问题
