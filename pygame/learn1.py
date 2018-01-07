# -*- coding: utf-8 -*-

import pygame,sys     #  一、引用

#  二、初始化
pygame.init()
screen = pygame.display.set_mode((600,400))  # 设置窗口，(600,400)为宽度高度(笛卡尔坐标系)
pygame.display.set_caption("from唐树森")


#  三、事件处理
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# 四、窗口刷新
    pygame.display.update()

###############以上是一个最小的游戏框架################
