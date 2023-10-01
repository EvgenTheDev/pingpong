from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Ping Pong')

clock = time.Clock()
FPS = 60

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