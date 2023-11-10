import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
FPS = 60
SCORE_LIMIT = 5
MAX_ROUNDS = 3

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Create the paddles and ball
player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)

# Set initial speed of the ball
ball_speed = [5, 5]

# Scores
player_score = 0
opponent_score = 0

# Rounds
current_round = 0

# Font for rendering text
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= 5
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += 5

    # Ball movement
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collisions with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Ball collisions with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed[0] = -ball_speed[0]

    # Opponent AI
    if opponent_paddle.centery < ball.centery and opponent_paddle.bottom < HEIGHT:
        opponent_paddle.y += 5
    elif opponent_paddle.centery > ball.centery and opponent_paddle.top > 0:
        opponent_paddle.y -= 5

    # Scoring
    if ball.left <= 0:
        opponent_score += 1
        if opponent_score >= SCORE_LIMIT:
            current_round += 1
            if current_round >= MAX_ROUNDS:
                winner_text = font.render("Opponent Wins! Game Over!", True, WHITE)
                screen.blit(winner_text, (WIDTH // 4, HEIGHT // 2))
                pygame.display.flip()
                pygame.time.wait(3000)  # Wait for 2 seconds
                pygame.quit()
                sys.exit()
            else:
                round_text = font.render(f"Round {current_round}: Opponent Wins!", True, WHITE)
                screen.blit(round_text, (WIDTH // 4, HEIGHT // 2))
                pygame.display.flip()
                pygame.time.wait(3000)  # Wait for 2 seconds
                player_score = 0
                opponent_score = 0
                ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)
    elif ball.right >= WIDTH:
        player_score += 1
        if player_score >= SCORE_LIMIT:
            current_round += 1
            if current_round >= MAX_ROUNDS:
                winner_text = font.render("Player Wins! Game Over!", True, WHITE)
                screen.blit(winner_text, (WIDTH // 4, HEIGHT // 2))
                pygame.display.flip()
                pygame.time.wait(2000)  # Wait for 2 seconds
                pygame.quit()
                sys.exit()
            else:
                round_text = font.render(f"Round {current_round}: Player Wins!", True, WHITE)
                screen.blit(round_text, (WIDTH // 4, HEIGHT // 2))
                pygame.display.flip()
                pygame.time.wait(2000)  # Wait for 2 seconds
                player_score = 0
                opponent_score = 0
                ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Display scores
    player_score_text = font.render(f"Player: {player_score}", True, WHITE)
    opponent_score_text = font.render(f"Opponent: {opponent_score}", True, WHITE)
    screen.blit(player_score_text, (20, 20))
    screen.blit(opponent_score_text, (WIDTH - 160, 20))

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    clock.tick(FPS)

    # Check for restart outside of the event loop
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        # Restart the game when 'R' key is pressed
        player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        opponent_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)
        ball_speed = [5, 5]
        player_score = 0
        opponent_score = 0
        current_round = 0
