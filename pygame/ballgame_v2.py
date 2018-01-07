# -*- coding: utf-8 -*-

import pygame,sys     #  一、引用

#  二、初始化
pygame.init()
size = width,height = 600,400
speed = [10,10]  #延笛卡尔坐标系正向(左、下)的速度
black = 0,0,0
screen = pygame.display.set_mode(size)  # 设置窗口，(600,400)为宽度高度
pygame.display.set_caption("ballgame_v2")
ball = pygame.image.load("PYG02-ball.gif")  # ball为surface对象
ballrect = ball.get_rect()                  # surface.get_rect()返回一个矩形对象

# ——————————————————ballgame_v2新增代码----------------------
fps = 300  # 每秒帧率参数
fclock = pygame.time.Clock()  #创建一个clock对象以控制时间


#  三、事件处理
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed[0],speed[1])#向左、下移动speed[0]、speed[1]个像素
    if ballrect.left < 0 or ballrect.right > width:  #遇到左右两侧，水平速度取反
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height: #遇到上下两侧，竖直速度取反
        speed[1] = -speed[1]
# 四、窗口刷新
    screen.fill(black)          # 填充背景色
    screen.blit(ball,ballrect)  # 将ball绘制在ballrect矩形内（因为事件处理部分只处理了ballrect）
    pygame.display.update()

# ——————————————————ballgame_v2新增代码----------------------
    fclock.tick(fps)            # 控制窗口刷新速度，每秒钟刷新fps次
