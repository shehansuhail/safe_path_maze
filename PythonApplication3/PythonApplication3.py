import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Safe Path Maze")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player attributes
player_size = 20
player_x = 50
player_y = 50
player_speed = 5

# Finish point
finish_rect = pygame.Rect(500, 300, 50, 50)

# Risky zones
risky_zones = [
    pygame.Rect(100, 100, 100, 20),
    pygame.Rect(300, 200, 150, 20),
    pygame.Rect(200, 50, 20, 150),
]

# Safe paths
safe_paths = [
    pygame.Rect(50, 50, 500, 20),
    pygame.Rect(50, 50, 20, 300),
    pygame.Rect(50, 330, 500, 20),
    pygame.Rect(530, 50, 20, 300),
]

# Game loop
clock = pygame.time.Clock()

def draw_elements():
    screen.fill(WHITE)
    
    # Draw safe paths
    for path in safe_paths:
        pygame.draw.rect(screen, GREEN, path)
    
    # Draw risky zones
    for zone in risky_zones:
        pygame.draw.rect(screen, RED, zone)
    
    # Draw finish point
    pygame.draw.rect(screen, BLUE, finish_rect)
    
    # Draw player
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_size, player_size))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Create a rectangle for the player
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

    # Check collision with risky zones
    for zone in risky_zones:
        if player_rect.colliderect(zone):
            print("You stepped on a risky path! Game Over!")
            running = False

    # Check if player reaches the finish point
    if player_rect.colliderect(finish_rect):
        print("Congratulations! You reached the safe zone!")
        running = False

    # Draw everything
    draw_elements()
    pygame.display.flip()
    clock.tick(30)

# Quit pygame
pygame.quit()
sys.exit()

