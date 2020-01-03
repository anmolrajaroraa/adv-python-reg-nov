import pygame, random, math
pygame.init()

white = 255,255,255
red = 255,0,0
green = 0,255,0
width = 1000
height = 500

clock = pygame.time.Clock()
fps = 100

gameScreen = pygame.display.set_mode((width,height))

def collision(ball1,ball2):
    distance = math.sqrt( ((ball2.x - ball1.x) ** 2) + ((ball2.y - ball1.y) ** 2))
    if distance < ball1.radius + ball2.radius:
        ball1.moveX *= -1
        ball1.moveY *= -1
        ball2.moveX *= -1
        ball2.moveY *= -1

class Ball:
    def __init__( self ):
        self.x = random.randint(0,width)
        self.y = random.randint(0,height)
        self.moveX = random.randint(1,10)
        self.moveY = random.randint(1,10)
        self.radius = random.randint(10,50)
        self.color = random.randint(0,255),random.randint(0,255),random.randint(0,255)

    def updateBall( self ):
        self.x += self.moveX
        self.y += self.moveY
        if self.y > height - self.radius:
            self.moveY = random.randint(-10,-1)
        elif self.y < 0 + self.radius:
            self.moveY = random.randint(1,10)
        elif self.x > width - self.radius:
            self.moveX = random.randint(-10,-1)
        elif self.x < 0 + self.radius:
            self.moveX = random.randint(1,10)

# ball = Ball()
# ball2 = Ball()
# ball2.x = 100
# ball2.y = 100
# ball2.radius = 25

balls = []
for i in range(400):
    ball = Ball()
    balls.append(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    gameScreen.fill(white)
    
    # pygame.draw.circle(gameScreen, red, (ball.x, ball.y), ball.radius)
    # ball.updateBall()

    # pygame.draw.circle(gameScreen, green, (ball2.x, ball2.y), ball2.radius)
    # ball2.updateBall()

    # for ball in balls:
    #     pygame.draw.circle(gameScreen, ball.color, (ball.x, ball.y), ball.radius)
    #     ball.updateBall()

    for i in range(len(balls)):
        currentBall = balls[i]
        pygame.draw.circle(gameScreen, currentBall.color, (currentBall.x, currentBall.y), currentBall.radius)
        currentBall.updateBall()
        targetBalls = [ball for ball in balls if ball != currentBall]
        # for ball in targetBalls:
        #     collision(currentBall, ball)
        # print(targetBalls)
    # print()
    # print()

    pygame.display.update()
    clock.tick(fps)

    #rect = pygame.Rect((ball.x, ball.y, ball.radius, ball.radius))#collide
    #distance = math.sqrt( (ball2.x - ball1.x) ** 2 + (ball2.y - ball1.y) ** 2)