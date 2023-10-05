from pygame import *

font.init()
font1 = font.SysFont('Arial', 45)

lose1 = font1.render(
    'PLAYER 1 HAD LOST!', True, (180, 0, 0)
)

lose2 = font1.render(
    'PLAYER 2 HAD LOST!', True, (180, 0, 0)
)

window = display.set_mode((700, 500))
display.set_caption('Ping Pong')

clock = time.Clock()
FPS = 60

win_height = 500
win_width = 700

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
    
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
    
    def update2(self):
        
        key_pressed = key.get_pressed()

        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed

background = transform.scale(
    image.load('background_table.png'),(700, 500)
    )

players = sprite.Group()

player1 = Player('platform.png', 90, 250, 4, 30, 120)
players.add(player1)

player2 = Player('platform.png', 610, 250, 4, 30, 120)
players.add(player2)

ball = GameSprite('ball.png', 350, 300, 0, 50, 50)

speed_x = 3
speed_y = 3

finish = False

game = True
while game:
    if not finish:

        window.blit(background, (0, 0))

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        player1.update()
        player2.update2()

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1

        if ball.rect.x <= 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x >= 700:
            finish = True
            window.blit(lose2, (200, 200))

        ball.reset()
        players.draw(window)

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()
