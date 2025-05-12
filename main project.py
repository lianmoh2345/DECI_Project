import time  # For adding delays between text outputs
import random  # For generating random outcomes


# Print a message and pause for 1 second for better reading pace.
def print_pause(message):
    print(message)
    time.sleep(1)


def display_intro():
    print_pause('Welcome, adventurer!')
    print_pause('You find yourself at the edge of a mysterious forest.')
    print_pause('Legends say a treasure lies hidden deep within...')


# Prompt the player to choose a path and validate their input.
def choose_path():
    while True:
        prompt = ('Do you go into the left path or the right path? '
                  '(left/right) \n> ')
        choice = input(prompt).strip().lower()
        if choice in ('left', 'right'):
            return choice
        print('Invalid choice. Please type left or right.')


# Generate a random character encounter based on the chosen path.
def encounter_character(path):
    characters = {
        'left': ['a friendly elf', 'a sneaky goblin'],
        'right': ['a wise wizard', 'a hungry troll']
    }

    # Randomly select a character from the chosen path
    character = random.choice(characters[path])
    print_pause(f'You meet {character}.')

    # Determine the outcome (40% positive, 30% neutral, 30% negative)
    outcome = random.randint(1, 10)
    if outcome <= 4:
        print_pause('They help you find some gold!')
        return 10
    if outcome <= 7:
        print_pause('They ignore you and walk away.')
        return 0
    print_pause('They attack you! You lose health and drop some gold.')
    return -5


# Update and display the player's score.
def update_score(total_score, change):
    total_score += change
    print_pause(f'Score change: {change:+}. Total score: {total_score}.')
    return total_score


# Check if the game should end based on score or turn count.
def check_game_over(total_score, turns, max_turns=5):
    if total_score < 0:
        print_pause('Your score fell below zero. You have failed your quest.')
        return True
    if turns >= max_turns:
        print_pause('You have reached the maximum number of turns.')
        return True
    return False


def main():
    # Initialize game state
    total_score = 0
    turns = 0
    display_intro()

    # Main game loop
    while True:

        path = choose_path()
        change = encounter_character(path)
        total_score = update_score(total_score, change)
        turns += 1

        if check_game_over(total_score, turns):
            break

        # Ask player if they want to continue
        while True:
            prompt = 'Do you want to continue? (yes/no) \n> '
            cont = input(prompt).strip().lower()
            if cont in ('yes', 'no'):
                break
            print('Invalid input. Please type yes or no.')
        if cont == 'no':
            print_pause('You decide to end your adventure. Farewell!')
            break

    # Display final score
    print_pause(f'Final score: {total_score}. Thanks for playing!')

    # Ask if player wants to play again
    while True:
        replay = input('Play again? (yes/no) \n> ').strip().lower()
        if replay in ('yes', 'no'):
            break
        print('Invalid input. Please type yes or no.')

    if replay == 'yes':
        print_pause('Restarting game...')
        main()  # Recursive call to restart the game
    else:
        print_pause('Goodbye!')


if __name__ == '__main__':
    main()
