import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=400
height=400
screen = pygame.display.set_mode((width,height))
  
bg = pygame.image.load("background0.png").convert_alpha()
flwr = pygame.image.load("flower1.png").convert_alpha()
score_font=pygame.font.Font('freesansbold.ttf', 25)

class Flower:
    count=0
    def __init__(self,x,y): 
        self.rect= pygame.Rect(x,y,20,20)
        Flower.count=Flower.count+1

    def display(self):  
        screen.blit(flwr,self.rect)
               


screen.fill((0,0,0))
screen.blit(bg,[0,0])   
while True:       
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            f=Flower(x,y)
            f.display()  
    

    pygame.draw.rect(screen, [230,230,230], pygame.Rect(0,0,150,40))

    count_text=score_font.render("Count:"+str(Flower.count), False, (255,25,0))  
    screen.blit(count_text,[10,10])
    
    
    
    pygame.display.update() 
    clock.tick(30) 
    
    
    
    
    

 