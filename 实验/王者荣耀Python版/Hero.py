# -*- coding: utf-8 -*-
# @Auther:Summer
# 该类为英雄类，后期可以使用元类按照orm的方式调入数据库


class Hero:
	"""
	Hero类包含：
		英雄名称
		英雄血量
		英雄技能 + 普通攻击
	"""
	name = ""
	blod = 0
	harm = 200  # 技能伤害


class YaSe(Hero):
	"""
		英雄名称：亚瑟
		血量：2000
	"""
	name = "亚瑟"
	blod = 2000


class AnQiLa(Hero):
	"""
		英雄名称：安其拉
		血量：1200
	"""
	name = "安其拉"
	blod = 1200
	harm = 400