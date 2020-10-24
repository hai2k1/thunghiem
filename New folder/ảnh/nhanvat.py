import pygame
from random import randint
pygame.init()
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game test")
clock = pygame.time.Clock()
down1 = pygame.image.load('nhanvat/down1.png')
down2 = pygame.image.load('nhanvat/down2.png')
down3 = pygame.image.load('nhanvat/down3.png')
down4 = pygame.image.load('nhanvat/down4.png')
up1 = pygame.image.load('nhanvat/up1.png')
up2 = pygame.image.load('nhanvat/up2.png')
up3 = pygame.image.load('nhanvat/up3.png')
up4 = pygame.image.load('nhanvat/up4.png')
lef1 = pygame.image.load('nhanvat/left1.png')
lef2 = pygame.image.load('nhanvat/left2.png')
lef3 = pygame.image.load('nhanvat/left3.png')
lef4 = pygame.image.load('nhanvat/left4.png')
right1 = pygame.image.load('nhanvat/right1.png')
right2 = pygame.image.load('nhanvat/right2.png')
right3 = pygame.image.load('nhanvat/right3.png')
right4 = pygame.image.load('nhanvat/right4.png')
house1 = pygame.image.load('map/house.png')
house2 = pygame.image.load('map/house1.png')
hoa = pygame.image.load('map/hoaqua.png')
shop = pygame.image.load('map/shop.png')
vongxuyen1 = pygame.image.load('map/vongxuyen1.png')
vongxuyen2 = pygame.image.load('map/vongxuyen2.png')
vongxuyen3 = pygame.image.load('map/vongxuyen3.png')
street = pygame.image.load('map/nengach.png')
changex = 200
changey = 200
location = 0
upl = 0
dow = 0
up = 0
lefl = 0
lef = 0
right = 0
rightl = 0
def iteam(iteamx,x,y):
    screen.blit(iteamx,(x,y))
def houses(housex,x,y):
    screen.blit(housex,(x,y))
def nhanvat(nhanvatx,x,y):
    screen.blit(nhanvatx,(x,y))
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             done = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            changey += 1
            dow = 1
            up = 2
            lef = 2
            right = 2
            location = location +1
        if event.key == pygame.K_UP:
            changey -= 1
            up = 1
            dow = 2
            lef = 2
            right = 2
            upl = upl + 1
        if event.key == pygame.K_LEFT:
            changex -= 1
            lef = 1
            right = 2
            up = 2
            dow = 2
            lefl = lefl + 1
        if event.key == pygame.K_RIGHT:
            changex += 1
            right = 1
            lef = 2
            up = 2
            dow = 2   
            rightl = rightl + 1
    screen.fill(BLACK)
    #gạch
    gachx = 0
    gachy = 0
    while gachx < 760:
        iteam(street, gachx, gachy)
        gachx = gachx + 30
        if gachx >=740:
            gachy = gachy + 30
            gachx = 0
        elif gachy >=540:
            break


    #nhà
    i = 0
    while i < 300:
        i = i + 70
        houses(house1,i,0)
    j=0
    while j < 300:
        j = j +70
        houses(house2,j,100)
    #vòng xuyến
    for k in range(1,2):
        if k<=1:
            iteam(vongxuyen1,200,200)
            k = k +1 
        if 1<k<=2:
            iteam(vongxuyen2,200,200)
            k = k - 1

    #nhân vật
    if 0<dow <= 1 and location > 4:
        nhanvat(down4,changex,changey)
    if 0<location<=1 and dow <= 1:
        nhanvat(down1,changex,changey)
    if 1<location<=2 and dow <= 1:
        nhanvat(down2,changex,changey)
    if 2<location<=3 and dow <= 1:
        nhanvat(down3,changex,changey)
    if 3<location<=4 and dow <= 1:
        nhanvat(down4,changex,changey)
    if location > 4 and dow <= 1:
        location = 1
    if 0<up <= 1 :
        nhanvat(up1,changex,changey)
    if 0<upl<=1 and up <= 1 :
        nhanvat(up1,changex,changey)
    if 1 < upl <= 2 and up<= 1:
        nhanvat(up2,changex,changey)
    if 2 < upl <= 3 and up<=1:
        nhanvat(up3,changex,changey)
    if 3 < upl <= 4 and up<=1:
        nhanvat(up4,changex,changey)
    if upl > 4 and  up<=1:
        upl = 1
    if 0<lef <= 1 and lefl >4:
        nhanvat(lef1,changex,changey)    
    if 0 <lefl <= 1 and lef <=1:
        nhanvat(lef1,changex,changey)
    if 1 <lefl <= 2 and lef <=1:
        nhanvat(lef2,changex,changey)
    if 2 <lefl <= 3 and lef <=1:
        nhanvat(lef3,changex,changey)
    if 3 <lefl <= 4 and lef <=1:
        nhanvat(lef4,changex,changey)
    if lefl > 4 and lef <= 1:
        lefl = 1
    if 0<right <= 1 and rightl > 4:
        nhanvat(right2,changex,changey)    
    if 0 <rightl <= 1 and right <=1:
        nhanvat(right1,changex,changey)
    if 1 <rightl <= 2 and right <=1:
        nhanvat(right2,changex,changey)
    if 2 <rightl <= 3 and right <=1:
        nhanvat(right3,changex,changey)
    if 3 <rightl <= 4 and right <=1:
        nhanvat(right4,changex,changey)
    if rightl > 4 and right <= 1:
        rightl = 1
    # npc:
    npc = 1
    changex_npc = 200
    changey_npc = 300
    if npc <= 1:
        nhanvat(lef1,changex_npc,changey_npc)
    if 0>changey - changey_npc >-30  and 0> changex - changex_npc >-30:
        print("hello chào bạn")
    # cuahang:
    changex_cuahang = 230
    changey_cuahang = 240
    iteam(shop,changex_cuahang,changey_cuahang)
    # hanghoa
    changex_hanghoa = 230
    changey_hanghoa = 320
    iteam(hoa,changex_hanghoa,changey_hanghoa)
    #khung hình
    clock.tick(30)
    pygame.display.update()
pygame.quit()
