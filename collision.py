import pygame,sys,time
pygame.init()
pygame.font.init()
RED=(255,64,64)
score = 0
score_increment = 10

def bouncing_rect():
    global x_speed,y_speed,other_speed
    moving_rect.x+=x_speed
    moving_rect.y+=y_speed

    if moving_rect.right>=screen_width or moving_rect.left<=0:
        x_speed*=-1
    if moving_rect.bottom>=screen_height or moving_rect.top<=0:
        y_speed*=-1

    other_rect.y+=other_speed
    if other_rect.top<=0 or other_rect.bottom>=screen_height:
        other_speed*=-1

    collision_tolerance=10
    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top-moving_rect.bottom)<collision_tolerance and y_speed>0:
            y_speed*=-1
        if abs(other_rect.bottom-moving_rect.top)<collision_tolerance and y_speed<0:
            y_speed*=-1
        if abs(other_rect.right-moving_rect.left)<collision_tolerance and x_speed<0:
            x_speed*=-1
        if abs(other_rect.left-moving_rect.right)<collision_tolerance and x_speed>0:
            x_speed*=-1
    pygame.draw.rect(screen,(255,255,255),moving_rect)
    pygame.draw.rect(screen,(0,238,0),other_rect)
    
def message_to_display(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [300, 300])

    
pygame.init()
pygame.font.init()

score = 0
score_increment = 10
clock=pygame.time.Clock()

screen_width,screen_height=800,800
screen=pygame.display.set_mode((screen_width,screen_height))

moving_rect=pygame.Rect(350,350,100,100)
x_speed,y_speed=5,4
other_rect=pygame.Rect(300,200,200,100)
other_speed=2

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    font = pygame.font.SysFont(None, 25)
    screen.fill((30,30,30))
    if moving_rect.colliderect(other_rect):
            score += score_increment
            if score==20:
                message_to_display("GAME OVER", RED)
                pygame.display.update()
                time.sleep(5)
                exit()

    bouncing_rect()
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
