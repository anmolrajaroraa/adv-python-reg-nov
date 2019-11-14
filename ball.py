import pygame, random
pygame.init()

white = 255,255,255
red = 255,0,0
green = 0,255,0

x = 0
y = 0
moveX = 1
moveY = 1

# x2 = 10
# y2 = 10
# moveX2 = 2
# moveY2 = 2

clock = pygame.time.Clock()
fps = 1

gameScreen = pygame.display.set_mode((500,250))

def ball():
    print(green)
    global x,y,moveX,moveY
    pygame.draw.circle(gameScreen, red, (x,y), 50)
    x += moveX
    y += moveY
    if x > 450:
        moveX = -1
    elif x < 50:
        moveX = 1
    elif y > 200:
        moveY = -1
    elif y < 50:
        moveY = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    gameScreen.fill(white)

    for i in range(1,11):
        ball()

    # pygame.draw.circle(gameScreen, red, (x,y), 50)
    # x += moveX
    # y += moveY

    # pygame.draw.circle(gameScreen, green, (x2,y2), 50)
    # x2 += moveX2
    # y2 += moveY2
    
    # if x > 450:
    #     moveX = -1
    # elif x < 50:
    #     moveX = 1
    # elif y > 200:
    #     moveY = -1
    # elif y < 50:
    #     moveY = 1

    # if x2 > 450:
    #     moveX2 = -2
    # elif x2 < 50:
    #     moveX2 = 2
    # elif y2 > 200:
    #     moveY2 = -2
    # elif y2 < 50:
    #     moveY2 = 2
    # print("Going to run for loop again")
    # for i in range(1,11):
    #     print(i)
    #     circle = pygame.draw.circle(gameScreen, red, (x,y), 50)
    #     x += moveX
    #     y += moveY
    #     if x > 450:
    #         moveX = -1
    #     elif x < 50:
    #         moveX = 1
    #     elif y > 200:
    #         moveY = -1
    #     elif y < 50:
    #         moveY = 1
        
    # x = random.randint(50,450)
    # y = random.randint(50,200)
    pygame.display.update()
    clock.tick(fps)