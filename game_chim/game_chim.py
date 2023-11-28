import pygame, sys, random
from random import randint
pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption('Flappy Bird')
tdscreen = pygame.time.Clock()
#load ảnh nền và chỉnh kích thước ảnh
background=pygame.image.load('images/background.png').convert()
background=pygame.transform.scale(background,(500,600))
#load ảnh con chim non
conchim=pygame.image.load('images/bird.png').convert()
conchim=pygame.transform.scale(conchim,(45,40))
birdrect=conchim.get_rect(center=(40,300))
x_chim=40
y_chim=300
# load ảnh ống và ép kích thước
ong=pygame.image.load('images/tube.png').convert()
ongd=pygame.image.load('images/tube_op.png').convert()
vantoc=0
vong=16
giatoc=0.15
#tọa dộ ống
r_ong=50
x_ong1=600
x_ong2=805
x_ong3=1010
y_ong1=y_ong2=y_ong3=0
d_ong1=randint(100,350)
d_ong2=randint(100,350)
d_ong3=randint(100,350)
d_ong1d=450-d_ong1
d_ong2d=450-d_ong2
d_ong3d=450-d_ong3
y_ong1d=600-d_ong1d
y_ong2d=600-d_ong2d
y_ong3d=600-d_ong3d
#phong chữ 
diem=0  
font = pygame.font.SysFont('Arial Black',30)
score=font.render('Score: ' +str(diem),True,(255,119,51))
k1=k2=k3=True
run = True
while run:
    tdscreen.tick(70)
    screen.fill((204,255,238))
    screen.blit(background,(0,0))
    #ve chim
    if x_chim<x_ong1:
        screen.blit(conchim,(x_ong1,y_ong1d-50))
    elif x_chim<x_ong2:
         screen.blit(conchim,(x_ong2,y_ong2d-80))   
    elif  x_chim<x_ong3:
        screen.blit(conchim,(x_ong3,y_ong3d-70))

    # chim rơi
    vantoc+=giatoc
    birdrect.centery+=vantoc
   
    
    
    # vẽ ống
  
    ong1=pygame.transform.scale(ong,(r_ong,d_ong1))
    ong1r=ong1.get_rect(midtop=(x_ong1,y_ong1))
    veong1=screen.blit(ong1,ong1r)
 
    ong2=pygame.transform.scale(ong,(r_ong,d_ong2))
    ong2r=ong2.get_rect(midtop=(x_ong2,y_ong2))
    veong2=screen.blit(ong2,ong2r)

    ong3=pygame.transform.scale(ong,(r_ong,d_ong3))
    ong3r=ong3.get_rect(midtop=(x_ong3,y_ong3))
    veong3=screen.blit(ong3,ong3r)
    # ống dưới
    ong1d=pygame.transform.scale(ongd,(r_ong,d_ong1d))
    ong1rd=ong1d.get_rect(midtop=(x_ong1,y_ong1d))
    veong1d=screen.blit(ong1d,ong1rd)
 
    ong2d=pygame.transform.scale(ongd,(r_ong,d_ong2d))
    ong2rd=ong2d.get_rect(midtop=(x_ong2,y_ong2d))
    veong2d=screen.blit(ong2d,ong2rd)

    ong3d=pygame.transform.scale(ongd,(r_ong,d_ong3d))
    ong3rd=ong3d.get_rect(midtop=(x_ong3,y_ong3d))
    veong3d=screen.blit(ong3d,ong3rd)

   
    #ống chạy
    x_ong1-=vong
    x_ong2-=vong
    x_ong3-=vong
    # tính điểm
   
    #vẽ điểm
    score=font.render('Score: ' +str(diem),True,(255,119,51))
    screen.blit(score,(5,5)) 
    if x_ong1<-50 :
        x_ong1=410+155
        d_ong1=randint(100,350)
        d_ong1d=450-d_ong1
        y_ong1d=600-d_ong1d

        k1=True
    if x_ong2<-50 :
        x_ong2=410+155
        d_ong2=randint(100,350)
        d_ong2d=450-d_ong2
        y_ong2d=600-d_ong2d

        k2=True
    if x_ong3<-50 :
        x_ong3=410+155  
        d_ong3=randint(100,350)
        d_ong3d=450-d_ong3
        y_ong3d=600-d_ong3d
        k3=True 
    if x_chim>x_ong1 and k1== True: 
                    diem+=1
                    k1=False
    if x_chim>x_ong2 and k2== True: 
                    diem+=1
                    k2=False
    if x_chim>x_ong3 and k3== True: 
                    diem+=1
                    k3=False
    tube=[ong1r,ong2r,ong3r,ong1rd,ong2rd,ong3rd]
    for i in range(len(tube)):
        if (birdrect.colliderect(tube[i])):
            #vantoc=0
            #vong=0
            #giatoc=0
             xxx=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                vantoc=-1.8
                birdrect.centery-=50
    
            
            
                    
    pygame.display.flip()
pygame.quit()

