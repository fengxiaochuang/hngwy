-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.5.40 - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  9.3.0.5071
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 导出  表 hngwy.category 结构
CREATE TABLE IF NOT EXISTS `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) DEFAULT NULL,
  `pid` int(11) NOT NULL DEFAULT '0' COMMENT '父级ID',
  `url` varchar(500) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '是否开启',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COMMENT='栏目及其链接表';

-- 正在导出表  hngwy.category 的数据：19 rows
DELETE FROM `category`;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` (`id`, `name`, `pid`, `url`, `status`) VALUES
	(1, '申论资料', 0, 'http://www.hngwy.org/category/34.html', 0),
	(2, '行测资料', 0, 'http://www.hngwy.org/category/35.html', 0),
	(3, '综合基础知识', 0, 'http://www.hngwy.org/category/36.html', 0),
	(4, '面试相关', 0, 'http://www.hngwy.org/category/37.html', 0),
	(5, '热点时评', 1, 'http://www.hngwy.org/category/47.html', 1),
	(6, '申论范文 ', 1, 'http://www.hngwy.org/category/48.html', 1),
	(7, '真题 ', 1, 'http://www.hngwy.org/category/67.html', 1),
	(8, '申论指导', 1, 'http://www.hngwy.org/category/90.html', 1),
	(9, '言语', 2, 'http://www.hngwy.org/category/49.html', 1),
	(10, '数量', 2, 'http://www.hngwy.org/category/50.html', 1),
	(11, '判断', 2, 'http://www.hngwy.org/category/51.html', 1),
	(12, '资料', 2, 'http://www.hngwy.org/category/52.html', 1),
	(13, '真题', 2, 'http://www.hngwy.org/category/68.html', 1),
	(14, '行测指导', 2, 'http://www.hngwy.org/category/135.html', 1),
	(15, '法律', 3, 'http://www.hngwy.org/category/54.html', 1),
	(16, '其它', 3, 'http://www.hngwy.org/category/56.html', 1),
	(17, '指导', 4, 'http://www.hngwy.org/category/57.html', 1),
	(18, '模拟题', 4, 'http://www.hngwy.org/category/58.html', 1),
	(19, '真题', 4, 'http://www.hngwy.org/category/59.html', 1);
/*!40000 ALTER TABLE `category` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
