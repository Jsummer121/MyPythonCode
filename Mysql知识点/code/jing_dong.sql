/*
 Navicat Premium Data Transfer

 Source Server         : 阿里云数据库
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : localhost:3306
 Source Schema         : jing_dong

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : 65001

 Date: 03/01/2021 21:05:52
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for customer
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `addr` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tel` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of customer
-- ----------------------------

-- ----------------------------
-- Table structure for goods
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cate_id` int UNSIGNED NOT NULL,
  `brand_id` int UNSIGNED NOT NULL,
  `price` decimal(10, 3) NOT NULL DEFAULT 0.000,
  `is_show` bit(1) NOT NULL DEFAULT b'1',
  `is_saleoff` bit(1) NOT NULL DEFAULT b'0',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `brand_id`(`brand_id`) USING BTREE,
  INDEX `cate_id`(`cate_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 27 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO `goods` VALUES (1, 'r510vc 15.6英寸笔记本', 1, 1, 3399.000, b'1', b'0');
INSERT INTO `goods` VALUES (2, 'y400n 14.0英寸笔记本电脑', 1, 2, 4999.000, b'1', b'0');
INSERT INTO `goods` VALUES (3, 'g150th 15.6英寸游戏本', 2, 3, 8499.000, b'1', b'0');
INSERT INTO `goods` VALUES (4, 'x550cc 15.6英寸笔记本', 1, 1, 2799.000, b'1', b'0');
INSERT INTO `goods` VALUES (5, 'x240 超极本', 3, 2, 4880.000, b'1', b'0');
INSERT INTO `goods` VALUES (6, 'u330p 13.3英寸超极本', 3, 2, 4299.000, b'1', b'0');
INSERT INTO `goods` VALUES (7, 'svp13226scb 触控超极本', 3, 4, 7999.000, b'1', b'0');
INSERT INTO `goods` VALUES (8, 'ipad mini 7.9英寸平板电脑', 4, 5, 1998.000, b'1', b'0');
INSERT INTO `goods` VALUES (9, 'ipad air 9.7英寸平板电脑', 4, 5, 3388.000, b'1', b'0');
INSERT INTO `goods` VALUES (10, 'ipad mini 配备 retina 显示屏', 4, 5, 2788.000, b'1', b'0');
INSERT INTO `goods` VALUES (11, 'ideacentre c340 20英寸一体电脑 ', 5, 2, 3499.000, b'1', b'0');
INSERT INTO `goods` VALUES (12, 'vostro 3800-r1206 台式电脑', 5, 6, 2899.000, b'1', b'0');
INSERT INTO `goods` VALUES (13, 'imac me086ch/a 21.5英寸一体电脑', 5, 5, 9188.000, b'1', b'0');
INSERT INTO `goods` VALUES (14, 'at7-7414lp 台式电脑 linux ）', 5, 7, 3699.000, b'1', b'0');
INSERT INTO `goods` VALUES (15, 'z220sff f4f06pa工作站', 6, 8, 4288.000, b'1', b'0');
INSERT INTO `goods` VALUES (16, 'poweredge ii服务器', 6, 6, 5388.000, b'1', b'0');
INSERT INTO `goods` VALUES (17, 'mac pro专业级台式电脑_new', 6, 5, 28888.000, b'1', b'0');
INSERT INTO `goods` VALUES (18, 'hmz-t3w 头戴显示设备', 7, 4, 6999.000, b'1', b'0');
INSERT INTO `goods` VALUES (20, 'x3250 m4机架式服务器', 6, 9, 6888.000, b'1', b'0');
INSERT INTO `goods` VALUES (26, '老王牌电脑', 7, 6, 4999.000, b'1', b'0');

-- ----------------------------
-- Table structure for goods_brands
-- ----------------------------
DROP TABLE IF EXISTS `goods_brands`;
CREATE TABLE `goods_brands`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of goods_brands
-- ----------------------------
INSERT INTO `goods_brands` VALUES (1, '华硕');
INSERT INTO `goods_brands` VALUES (2, '联想');
INSERT INTO `goods_brands` VALUES (3, '雷神');
INSERT INTO `goods_brands` VALUES (4, '索尼');
INSERT INTO `goods_brands` VALUES (5, '苹果');
INSERT INTO `goods_brands` VALUES (6, '戴尔');
INSERT INTO `goods_brands` VALUES (7, '宏碁');
INSERT INTO `goods_brands` VALUES (8, '惠普');
INSERT INTO `goods_brands` VALUES (9, 'ibm');
INSERT INTO `goods_brands` VALUES (16, '海尔');
INSERT INTO `goods_brands` VALUES (17, '清华同方');
INSERT INTO `goods_brands` VALUES (18, '神舟');

-- ----------------------------
-- Table structure for goods_cates
-- ----------------------------
DROP TABLE IF EXISTS `goods_cates`;
CREATE TABLE `goods_cates`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of goods_cates
-- ----------------------------
INSERT INTO `goods_cates` VALUES (1, '笔记本');
INSERT INTO `goods_cates` VALUES (2, '游戏本');
INSERT INTO `goods_cates` VALUES (3, '超级本');
INSERT INTO `goods_cates` VALUES (4, '平板电脑');
INSERT INTO `goods_cates` VALUES (5, '台式机');
INSERT INTO `goods_cates` VALUES (6, '服务器/工作站');
INSERT INTO `goods_cates` VALUES (7, '笔记本配件');
INSERT INTO `goods_cates` VALUES (8, '路由器');
INSERT INTO `goods_cates` VALUES (9, '交换机');
INSERT INTO `goods_cates` VALUES (10, '网卡');
INSERT INTO `goods_cates` VALUES (11, '其他');

-- ----------------------------
-- Table structure for order_detail
-- ----------------------------
DROP TABLE IF EXISTS `order_detail`;
CREATE TABLE `order_detail`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `order_id` int UNSIGNED NOT NULL,
  `goods_id` int UNSIGNED NOT NULL,
  `quantity` tinyint UNSIGNED NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `order_id`(`order_id`) USING BTREE,
  INDEX `goods_id`(`goods_id`) USING BTREE,
  CONSTRAINT `order_detail_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `order_detail_ibfk_2` FOREIGN KEY (`goods_id`) REFERENCES `goods` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of order_detail
-- ----------------------------

-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `order_date_time` datetime NOT NULL,
  `customer_id` int UNSIGNED NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `customer_id`(`customer_id`) USING BTREE,
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of orders
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
