import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
BALL_RADIUS = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
FPS = 60

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the clock
clock = pygame.time.Clock()

class Ball:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.vx = 5
        self.vy = 5

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.y < 0 or self.y > HEIGHT - BALL_RADIUS:
            self.vy *= -1

    def reset(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.vx = 5
        self.vy = 5

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def move_up(self):
        if self.y > 0:
            self.y -= self.speed

    def move_down(self):
        if self.y < HEIGHT - PADDLE_HEIGHT:
            self.y += self.speed

def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

def main():
    ball = Ball()
    paddle1 = Paddle(10, HEIGHT / 2 - PADDLE_HEIGHT / 2)
    paddle2 = Paddle(WIDTH - 20, HEIGHT / 2 - PADDLE_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move_up()
        if keys[pygame.K_s]:
            paddle1.move_down()
        if keys[pygame.K_UP]:
            paddle2.move_up()
        if keys[pygame.K_DOWN]:
            paddle2.move_down()

        ball.move()

        # Collision with paddles
        if (ball.x > paddle1.x and ball.x < paddle1.x + PADDLE_WIDTH and
            ball.y > paddle1.y and ball.y < paddle1.y + PADDLE_HEIGHT):
            ball.vx *= -1
        elif (ball.x > paddle2.x and ball.x < paddle2.x + PADDLE_WIDTH and
              ball.y > paddle2.y and ball.y < paddle2.y + PADDLE_HEIGHT):
            ball.vx *= -1

        # Collision with walls
        if ball.x < 0:
            print("Player 2 wins!")
            pygame.quit()
            sys.exit()
        elif ball.x > WIDTH - BALL_RADIUS:
            print("Player 1 wins!")
            pygame.quit()
            sys.exit()

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (paddle1.x, paddle1.y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, WHITE, (paddle2.x, paddle2.y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.ellipse(screen, WHITE, (ball.x, ball.y, BALL_RADIUS, BALL_RADIUS))

        draw_text(f"Player 1: {ball.x}", 10, 10)
        draw_text(f"Player 2: {WIDTH - ball.x - BALL_RADIUS}", WIDTH - 150, 10)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
