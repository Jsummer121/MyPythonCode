import requests
import jsonpath
import pygal
 
# 1. 请求刺激战场整体数据
response = requests.get("http://pg.qq.com/zlkdatasys/data_zlk_zlzx.json")
 
# 2. 抽取想要数据 枪支性能
x = jsonpath.jsonpath(eval(response.text), "$..ldtw_f2")
akm_x = x[0][0]
akm_x = [int(akm_x['wl_45']), int(akm_x['sc_54']), int(akm_x['ss_d0']), int(akm_x['wdx_a7']), int(akm_x['zds_62'])]
 
# 3. 雷达图设计
# 调用Radar这个类，设置雷达图
radar_chart = pygal.Radar()
# 添加雷达图标题
radar_chart.title = "AKM-性能"
# 添加雷达图各顶点的含义
radar_chart.x_labels = ['威力', '射程', '射速', '稳定性', '子弹数']
radar_chart.add("AKM", akm_x)
# 保存图片
radar_chart.render_to_file("gun.svg")