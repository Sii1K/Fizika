import pygame


pygame.init()
win = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("Model of lab1.03V: collisions")
backround = pygame.image.load("Backround.png")


class Circle():
    def __init__(self, x, y, radius, mass, velocity):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass 
        self.velocity = velocity

    def move(self):
        if self.x < 37 and self.velocity < 0:
            self.velocity = -self.velocity
            print(self.x)
        elif self.x > 1163 and self.velocity > 0:
            self.velocity = -self.velocity
            print(self.x)
        else:
            self.x += int(self.velocity)


    def draw(self, check):
        style = pygame.font.SysFont("Times New Roman", 24)
        velocity = abs((self.velocity * 100 // 100 ))
        param = ["Parameters of second ball:", f"Mass: {self.mass}g", f"Velocity: {velocity}m/s"]
        count = 10
        if check == 1:
            for i in range(0, 3):
                text = style.render(param[i],1, (0, 0, 0))
                win.blit(text, (20, count))
                count += 24
        elif check == 2:
            for i in range(0, 3):
                text = style.render(param[i],1, (0, 0, 0))
                win.blit(text, (920, count))
                count += 24
        pygame.draw.circle(win, (0, 0, 255), (self.x, self.y), self.radius) 


ball1 = Circle(100, 317, 36, 400, 20)

ball2 = Circle(500, 317, 36, 600, 0)

isElastic = True


def draw():
    win.blit(backround, (0, 0))
    pygame.draw.rect(win, (169, 69, 19), (10, 20, 30, 50))
    ball1.draw(1)
    ball2.draw(2)
    pygame.display.update()


while True:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
    
    ball1.move()
    ball2.move()
    if isElastic:
        if ball1.x > ball2.x - 73:
            velocity = ball1.velocity
            ball1.velocity = ((ball1.mass - ball2.mass) * ball1.velocity + 2 * ball2.mass * ball2.velocity) / (ball1.mass + ball2.mass)
            ball2.velocity = ((ball2.mass - ball1.mass) * ball2.velocity + 2 * ball1.mass * velocity) / (ball1.mass + ball2.mass)
    else:
        if ball1.x > ball2.x - 73:
            velocity = ball1.velocity
            ball1.velocity = (ball1.mass * ball1.velocity + ball2.mass * ball2.velocity) / (ball1.mass + ball2.mass)
            ball2.velocity = (ball1.mass * velocity + ball2.mass * ball2.velocity) / (ball1.mass + ball2.mass)

    draw()

pygame.quit()