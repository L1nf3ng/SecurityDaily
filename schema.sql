SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for authors
-- ----------------------------
DROP TABLE IF EXISTS `authors`;
CREATE TABLE `authors`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '作者id',
  `name` varchar(255) NOT NULL COMMENT '作者姓名',
  `link` varchar(255) NOT NULL COMMENT '链接',
  `create_time` datetime(0) NOT NULL COMMENT '本记录创建日期',
  `extra` varchar(255)  NULL DEFAULT NULL COMMENT '保留字段，用于后期功能扩展',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `u_link`(`link`) USING BTREE COMMENT '之所以不用name，因为一个id可能在多个平台注册，由此每个平台保存一条记录，检索名称时就可看到他在哪些平台有账户'
) ENGINE = InnoDB AUTO_INCREMENT = 1  ROW_FORMAT = Dynamic;


-- ----------------------------
-- Table structure for posts
-- ----------------------------
DROP TABLE IF EXISTS `posts`;
CREATE TABLE `posts`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '文章id',
  `title` varchar(255) NOT NULL COMMENT '博客标题',
  `link` varchar(255) NOT NULL COMMENT '文章链接',
  `tag` varchar(60) NULL DEFAULT NULL COMMENT '分类标签',
  `datetime` datetime(0) NOT NULL COMMENT '爬取日期',
  `origin` varchar(60)NOT NULL COMMENT '来源平台',
  `author_id` int(11) NOT NULL COMMENT '外键，作者id号',
  `extra` tinyblob NULL COMMENT '扩展字段，例如：可能用作缩略图',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `u_post`(`link`, `datetime`) USING BTREE COMMENT '依靠文章链接、发表日期做唯一性约束',
  INDEX `author_id`(`author_id`) USING BTREE,
  CONSTRAINT `posts_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `authors` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 1 ROW_FORMAT = Dynamic;
