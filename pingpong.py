from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Ping Pong')

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width = 65, height = 65):
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

        if key_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed

background = transform.scale(
    image.load('background_table.png'),(700, 500)
    )

finish = False

game = True
while game:
    if not finish:

        window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()
