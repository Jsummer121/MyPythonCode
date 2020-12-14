import math
All_f = '90,80,80,90,80,80,80,80'
All_t = '0,0,0,0,-0.1,0,0,-0.1'
j = 0
All_F = []#每个人所用的力
All_T = []#每个人的发力时机
m_pai = 0.27#排球质量
v_ru = 1.980#小球接触鼓面的速度
G_gu = 35.28#鼓的重量
F_f = 0.5*m_pai#空气摩擦力
h = 0.01#小球从鼓面到达最低点的高度
sin_a = 11/170
cos_a = math.sqrt(170**2-11**2)/170

for i in range(0,len(All_f),3):
    a = int(All_f[i:i+2])
    All_F.append(a)


#90出现的位置
position_90 = [idx for idx,i in enumerate(All_F) if i == 90]


def lev_degree(F_up,F_xie):
    """
    小球离开鼓面时用来计算角度的函数。
    """
    V_up = math.sqrt(((0.5 * m_pai * v_ru ** 2) + (F_up - G_gu) * h) / 0.5 / m_pai)  # 小球离开鼓面的瞬间的向上的速度
    V_xie = math.sqrt(((0.5 * m_pai * 0 ** 2) + F_xie * h) / 0.5 / m_pai)  # 小球离开鼓面的瞬间的水平速度
    s_up = V_up * 0.1 + 0.5 * 0.1 ** 2 * ((m_pai*9.8+F_f) / m_pai)
    s_xie = V_xie * 0.1 + 0.5 * 0.1 ** 2 * (F_f / m_pai)
    hudu = math.tanh(s_up / s_xie)
    degree = math.degrees(hudu)  # 弧度转角度
    return degree

def on_degree(F_up, F_xie):
    """
        小球在鼓面时用来计算角度的函数。
    """
    V_up = math.sqrt(((0.5 * m_pai * v_ru ** 2) + (F_up - G_gu) * h) / 0.5 / m_pai)  # 小球离开鼓面的瞬间的向上的速度
    V_xie = math.sqrt(((0.5 * m_pai * 0 ** 2) + F_xie * h) / 0.5 / m_pai)  # 小球离开鼓面的瞬间的水平速度
    s_up = V_up * 0.1 + 0.5 * 0.1 ** 2 * ((F_up - G_gu) / m_pai)
    s_xie = V_xie * 0.1 + 0.5 * 0.1 ** 2 * (F_xie / m_pai)
    hudu = math.tanh(s_up / s_xie)
    degree = math.degrees(hudu)  # 弧度转角度
    return degree


if '-0.1' not in All_t:
     if  len(position_90) == 1:
         F_up = 80*11/170*8+10*sin_a
         F_xie = 10*cos_a
         print('{:.3f}'.format(lev_degree(F_up,F_xie)))
     else:
         deg = math.radians(45*(position_90[1]-position_90[0])/2) #角度转弧度，两个人所产生的夹角的1/2
         F_he = 2*90*math.cos(deg)
         F_up = 80*11/170*8+(F_he-80)*sin_a
         F_xie = (abs(F_he-80))*cos_a
         print('{:.3f}'.format(lev_degree(F_up, F_xie)))


else:
    #把字符串转数字列表
    for i in range(0,len(All_t)):
        b = All_t[i]
        if i == len(All_t)-1:
            c = float(All_t[j:])
            All_T.append(c)
    
        if b == ',':
            c = float(All_t[j:i])
            j = i+1
            All_T.append(c)


    #-0.1出现的位置
    position_1 = [idx for idx,i in enumerate(All_T) if i == -0.1]



    if 90 not in All_F:
        if len(position_1) == 1:
            #第4题
            F_up = 80 * sin_a
            F_xie = 80 * cos_a
            print('{:.3f}'.format(abs(on_degree(F_up, F_xie))))
        else:
            #第5,6题
            deg = math.radians(45 * (position_1[1] - position_1[0]) / 2)  # 角度转弧度，两个人所产生的夹角的1/2
            F_he = 2 * 80 * math.cos(deg)
            F_up = 80 * 11 / 170 * 8 + (F_he - 80) * sin_a
            F_xie = (abs(F_he - 80)) * cos_a
            print('{:.3f}'.format(on_degree(F_up, F_xie)))
    else:
        if position_90[0] == position_1[0]:
            F_up1 = 90*sin_a
            F_xie1 = 90*cos_a
            deg1 = on_degree(F_up1, F_xie1)
            F_up2 = 80 * 11 / 170 * 8 + 10 * sin_a
            F_xie2 = 10 * cos_a
            deg2 = lev_degree(F_up2, F_xie2)
            print('{:.3f}'.format(abs(deg1+ deg2)))
        else:
            deg = math.radians(45 * (position_90[1] - position_90[0]) / 2)  # 角度转弧度，两个人所产生的夹角的1/2
            F_he1 = 2 * 90 * math.cos(deg)
            F_up1 = 80 * 11 / 170 * 8 + (F_he1 - 80) * sin_a
            F_xie1 = (abs(F_he1 - 80)) * cos_a
            deg1 = on_degree(F_up1, F_xie1)
            deg = math.radians(45 * (position_1[1] - position_1[0]) / 2)  # 角度转弧度，两个人所产生的夹角的1/2
            F_he2 = 2 * 80 * math.cos(deg)
            F_up2 = 80 * 11 / 170 * 8 + (F_he2 - 80) * sin_a
            F_xie2 = (abs(F_he2 - 80)) * cos_a
            deg2 = lev_degree(F_up2, F_xie2)
            if position_1[0]+position_90[0]<4:
                print('{:.3f}'.format(abs((deg1 + deg2)*((4-position_1[0]+position_90[0])/4))))
            else:
                print('{:.3f}'.format(abs((deg1 - deg2))))

