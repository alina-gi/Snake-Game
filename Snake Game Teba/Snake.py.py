import random
import pygame
import pygame

pygame.mixer.init()
pygame.mixer.music.load('background.MP3')
pygame.mixer.music.play()

pygame.init()


# Colors
white = (255, 255, 255)
red = (250, 250, 250)
black = (50, 0, 0)
snakegreen = (35, 45, 40)


Screen_Width = 900
Screen_Height = 600
gameWindow = pygame.display.set_mode((Screen_Width, Screen_Height))

bgimg = pygame.image.load("snake.jpg")
bgimg = pygame.transform.scale(bgimg,(Screen_Width, Screen_Height)).convert_alpha()
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Harrington', 35)




def text_screen(text, color, x, y):
    text_screen = font.render(text, True, color)
    gameWindow.blit(text_screen, [x, y])


def plot_snake(gameWindow, color, snake_list, snake_size):
    # print(snake_list)
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        text_screen("Welcome to Snakes", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameLoop()

        pygame.display.update()
        clock.tick(60)
# Game loop
def gameLoop():
    # Game Specific Variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 30
    fps = 50
    vilocity_x = 0
    vilocity_y = 0
    with open("hiscore.txt", "r")as f:
        hiscore = f.read()
    food_x = random.randint(20, Screen_Width/2)
    food_y = random.randint(20, Screen_Height/2)
    score = 0
    init_vilocity = 5
    snake_list = []
    snake_len = 1

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w")as f:
                    f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue",
                        black, 100,300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vilocity_x = init_vilocity
                        vilocity_y = 0
                    if event.key == pygame.K_LEFT:
                        vilocity_x = -init_vilocity
                        vilocity_y = 0
                    if event.key == pygame.K_UP:
                        vilocity_y = -init_vilocity
                        vilocity_x = 0
                    if event.key == pygame.K_DOWN:
                        vilocity_y = init_vilocity
                        vilocity_x = 0

            snake_x = snake_x + vilocity_x
            snake_y = snake_y + vilocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10
                # print("Score:", score*10)
                food_x = random.randint(20, Screen_Width/2)
                food_y = random.randint(20, Screen_Height/2)
                snake_len += 5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0,0))
            text_screen("Score: " + str(score)+ "   hiscore: "+ str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [
                food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)



            if len(snake_list) > snake_len:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > Screen_Width or snake_y < 0 or snake_y > Screen_Height:
                game_over = True

            # pygame.draw.rect(gameWindow, black,[snake_x, snake_y,snake_size,snake_size])
            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()