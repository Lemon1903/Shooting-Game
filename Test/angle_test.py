import pygame, sys, math, numpy

DIMENSIONS = (600, 600)
window = pygame.display.set_mode(DIMENSIONS, pygame.RESIZABLE)
window.fill((20, 20, 20))
pygame.display.set_caption("Pygame template")
clock = pygame.time.Clock()

player = pygame.Rect((270, 270), (50, 50))
player_center = pygame.Vector2(player.center)

while True:

    window.fill((20,20,20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Relative position of mouse
    mouse_pos = pygame.mouse.get_pos()
    delta = mouse_pos - player_center

    # Calculate the angle 
    angle_to_mouse = math.atan2(delta.y, delta.x)
    print(angle_to_mouse)
    looking_vector = pygame.Vector2(100*math.cos(angle_to_mouse), 100*math.sin(angle_to_mouse))

    # Player rect
    pygame.draw.rect(window, (50, 50, 255), player)
    # Line to mouse
    pygame.draw.line(window, (255,50,50), player.center, mouse_pos)
    # Line in direction to looking_vector
    pygame.draw.line(window, (50,255,50), player.center, player_center + looking_vector)

    pygame.display.update()
    clock.tick(60)