# import libraries
import pygame
import time
import random


#speed that the snake will move at
snake_speed = 15

# X (horizontal window size)
window_x = 720
# Y (vertical window size)
window_y = 480

# defining RGB color format that will be used for the game
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initializing pygame
pygame.init()

# Initialise game window
# set the title of the game window
pygame.display.set_caption('Adrian\'s Snake Game!')
# create the display window with the specified dimensions and assign it the game window variable
game_window = pygame.display.set_mode((window_x, window_y))

#FPS (Frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [360, 450]

# defining first block of snake body
# the snakes body
snake_body = [ 
    [360, 450],
    ]

# fruit position 
fruit_position = [
    # set the range of the position randomly within the bounds of the window for x 
    random.randrange(1, (window_x//10)) * 10,
    # set the range of the position randomly within the bounds of the window for y
    random.randrange(1,(window_y//10)) * 10]

# fruit spawn set to true
fruit_spawn = True

# setting default snake direction 
# towards UP
direction = 'UP'
change_to = direction

# Initial score
score = 0

# displaying Score function
def show_score(choice, color, font, size):
                                        
    # creating font object score_font 
    score_font = pygame.font.SysFont(font, size)
    
    # create the display surface object score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the text surface object
    score_rect = score_surface.get_rect()
    
    # Display text
    game_window.blit(score_surface, score_rect)

def plug(choice, color, font, size):
                                        
    # creating font object plug_font 
    plug_font = pygame.font.SysFont(font, size)
    
    # create the display surface object score_surface
    plug_surface = plug_font.render("Adrian Abreu", True, color)
    
    # create a rectangular object for the text surface object
    plug_rect = plug_surface.get_rect()
    # Position the text surface at the bottom-right corner of the game_window
    plug_rect.bottomright = (game_window.get_width(), game_window.get_height())
    # Ensure the text does not go out of bounds
    plug_rect.right = game_window.get_width()
    
    # Display text
    game_window.blit(plug_surface, plug_rect)

#game over function
def game_over():
    
    # creating font object my_font
    my_font = pygame.font.SysFont('monospace', 50)
    
    # creating a text surface on which text will be drawn
    game_over_surface = my_font.render('Your score is: ' + str(score), True, white)
    
    # create a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()
    
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/ 4)
    
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    # update the contents of the entire display
    pygame.display.flip()
    
    # after 2 seconds we will quit the program
    time.sleep(2)
    
    # deactivating pygame library
    pygame.quit()
    
    # quit the program
    quit()

# Main Function
# constantly running the game loop
while True:
    
    # handling key events
    # if any key is pressed
    for event in pygame.event.get():
        # if a key is pressed down do the following
        if event.type == pygame.KEYDOWN:
            # if the key is the up arrow key 
            if event.key == pygame.K_UP:
                # change the direction to 'UP'
                change_to = 'UP'
            # if the key is the down arrow key
            if event.key == pygame.K_DOWN:
                # change the direction to 'DOWN'
                change_to = 'DOWN'
                # if the key is the left arrow key
            if event.key == pygame.K_LEFT:
                # change the direction to 'LEFT'
                change_to = 'LEFT'
                # if the key is the right arrow key
            if event.key == pygame.K_RIGHT:
                # change the direction to 'RIGHT'
                change_to = 'RIGHT'
    
    # if two keys pressed simultaneously we don't want snake to move into two directions simultaneously
    # if direction is up and not down go up
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    # if direction is down and not up go down
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    # if direction is left and not right go left
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    # if direction is right and not left go right
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
        
    # Moving the snake
    
    # if the direction is up decrease the y coordinate by 10
    if direction == 'UP':
        snake_position[1] -= 10
    # if the direction is down increase the y coordinate by 10
    if direction == 'DOWN':
        snake_position[1] += 10
    # if the direction is left decrease the x coordinate by 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    # if the direction is right increase the x coordinate by 10
    if direction == 'RIGHT':
        snake_position[0] += 10
    
    # Snake body growing mechanism 
    # if fruits and snakes collide then scores will be 
    # incremented by 10
    #insert from 0 to current snake position a body part
    snake_body.insert(0, list(snake_position))
    #if the X and Y of snake position and fruit position are the same
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
    # add 1 to the score
        score += 1
    # set fruit spawn to false
        fruit_spawn = False
    # otherwise pop (remove) snake body
    else:
        snake_body.pop()
    # if fruit has not spawned
    if not fruit_spawn:
        #set the range of the position randomly within the bounds of the window for x and y
        fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
    
    #fruit spawn bool set to true
    fruit_spawn = True
    #makes the window black again
    game_window.fill(black)
    
    #for each position in the snake body list
    for pos in snake_body:
        # draw a green rectangle for each part of the snake body
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    # draw a red rectangle for the fruit
    pygame.draw.rect(game_window, red, pygame.Rect(
        # the x position of the fruit and the y position of the fruit and the width and height of the rectangle
        fruit_position[0], fruit_position[1], 10, 10))
    
    # Game Over conditions
    # if the snake is out of bounds on the x or y axis
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        # end the game
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        # end the game
        game_over()
    
    # checking if the snake has hit itself from one to whatever the end is
    for block in snake_body[1:]:
        # if the head of the snake is in the same position as any part of its body
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            # end the game
            game_over()
    # displaying score continuously in a white arial font of size 20
    show_score(1, white, 'arial', 20)
    
    plug(1, white, 'arial', 20)
    
    # Refresh game screen 
    pygame.display.update()

    # Frame Per Second /Refresh Rate adjacent to the speed of the snake
    fps.tick(snake_speed)