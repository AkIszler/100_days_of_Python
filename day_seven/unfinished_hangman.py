#this is not an official game, just a code outline, no images to make it work are created at this time. 
#I ran it with blank images to test, and this is more for functionality purposes
# may upload a proper game later when I have time to make out the images for the game.
#due to the lack of images this game is only in theory, using the same basic logic as the "prehm.py" file 
#prehm.py will be playable as a console application/game


import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load images
images = []
for i in range(0):
    image = pygame.image.load(f"hangman{i}.png")
    images.append(image)

# Fonts
LETTER_FONT = pygame.font.SysFont(None, 40)
WORD_FONT = pygame.font.SysFont(None, 60)
TITLE_FONT = pygame.font.SysFont(None, 70)

def draw(word, guessed_letters, tries):
    win.fill(WHITE)

    # Display title
    title_label = TITLE_FONT.render("HANGMAN", True, BLACK)
    win.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 20))

    # Display word
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    word_label = WORD_FONT.render(display_word, True, BLACK)
    win.blit(word_label, (400, 200))

    # Display guessed letters
    guessed_label = LETTER_FONT.render("Guessed letters: " + ", ".join(guessed_letters), True, BLACK)
    win.blit(guessed_label, (10, 400))

    # Display tries remaining
    tries_label = LETTER_FONT.render("Tries remaining: " + str(tries), True, BLACK)
    win.blit(tries_label, (10, 450))

    # Display hangman image
    win.blit(images[6-tries], (150, 100))

    pygame.display.update()

def hangman():
    word_list = ["apple", "banana", "orange", "mango", "strawberry"]  # Add more words as desired
    word = random.choice(word_list).lower()
    guessed_letters = []
    tries = 6

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_BACKSPACE:
                    if guessed_letters:
                        guessed_letters.pop()

                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    guess = chr(event.key)
                    if guess in guessed_letters:
                        continue
                    guessed_letters.append(guess)
                    if guess not in word:
                        tries -= 1

        draw(word, guessed_letters, tries)

        if tries == 0:
            pygame.time.delay(1000)
            run = False

        if all(letter in guessed_letters for letter in word):
            pygame.time.delay(1000)
            run = False

    pygame.quit()

hangman()
