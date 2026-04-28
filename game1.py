import pygame 
import random

pygame.init()


size=800 
size_snack=100
size_reward=20
screen= pygame.display.set_mode((size,size))
pygame.display.set_caption("Game")
font = pygame.font.SysFont('Arial',30,bold =True,italic=False)


clock = pygame.time.Clock()


size_rect=100


def mouvement(x,y,speed,direction):

    if direction == 'right':
         x=x+speed
         new_head=[x,y]
         
         
    elif direction =='left':
          x=x-speed
          new_head=[x,y]
           
    elif direction == 'up':
         y=y-speed
         
         new_head=[x,y]
           
         
    elif direction == 'down':
         y=y+speed
         
         new_head=[x,y]
    
   
    if x < -100:
         x=size
    elif x >=800:
         x=-100
    if y < -100:
         y=size
    elif y >=800:
        y=-100
    return x,y,new_head


  
def mv(x,y,speed):
        t=clock.tick(60)/500

        x=x-speed*t
        if x < -100:
            x=size
        
        return x

def reward(state):
     x_reward=0
     y_reward=0
     if state:
           x_reward=random.randint(20,size-20)
           y_reward=random.randint(20,size-20)
           state=False
     
     return x_reward,y_reward,state


def eat(snack,direction,speed):
    if direction == 'right':
        
         new_head=[snack[-1][0]-speed,snack[-1][1]]
         
         
    elif direction =='left':
           new_head=[snack[-1][0]+speed,snack[-1][1]]
    elif direction == 'up':
          new_head=[snack[-1][0],snack[-1][1]+speed]
         
        
         
    elif direction == 'down':
         new_head=[snack[-1][0],snack[-1][1]-speed]

    snack.append((new_head))
     
   
    
 
def main() :  
            
            x=0
            y=0
            score=0
            state=True
            speed=10
            running=True
            start=False
            direction='right'
            snack=[]
            for i in range(20):
                 snack=snack+[[x+i*size_rect,y]]
                           
            
            print(snack)
            while running :
                
                t=clock.tick(60)/1000

                for event in pygame.event.get():
                    if event.type == pygame.QUIT :
                        running = False 

 
                    if start == False :
                        text = font.render("Presser entrer Pour commancer",True,(255,255,255))

                        rect=text.get_rect(center=(400,400))
                        screen.blit(text,rect)
                        pygame.display.update()
    
                        if event.type == pygame.KEYDOWN :
                                if event.key == pygame.K_SPACE :
                                    start = True

                    else :
                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_UP and direction != 'down':
                                  direction = 'up'
                            elif event.key == pygame.K_DOWN and direction != 'up':
                                 direction = 'down'
                            elif event.key == pygame.K_RIGHT and direction != 'left':
                                 direction = 'right'
                            elif event.key == pygame.K_LEFT and direction != 'right':
                                 direction = 'left'



                        

        

                
                screen.fill((0,0,0))

                if start == False :
                        text = font.render("Presser entrer Pour commancer",True,(255,255,255))

                        rect=text.get_rect(center=(400,400))
                        screen.blit(text,rect)
                        pygame.display.update()
                else :
                        for segment in snack :
                             pygame.draw.circle(screen,(255,0,0),(segment[0],segment[1]),size_snack//4)
                        x,y,head=mouvement(x,y,2,direction)
                        snack.insert(0,head)
                        snack.pop()
                        
                        if state:
                            x_reward,y_reward,state=reward(state)
                                  
                        pygame.draw.circle(screen,(100,100,100),(x_reward,y_reward),size_reward)

                        if (x-x_reward)**2 +(y-y_reward)**2<size_reward**2 :
                             score +=1
                             speed+=1
                             eat(snack,direction,speed)
                             print(len(snack))
                             
                             state =True

                        


                        score_text=font.render("votre score est : "+str(score),True,(255, 255, 0))
                        reward_text=text.get_rect(center=(750,750))
                        screen.blit(score_text,reward_text)
                        
                        pygame.display.update()


                    


            pygame.quit()



if __name__ == '__main__':
     main()