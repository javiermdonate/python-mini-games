import random


def rock_paper_scissors():
    actions = ['rock', 'paper', 'scissors']
    winning = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper',
    }

    playing = True

    while playing:
        user_action = input(f'Choose one of the following options: {actions}\n').lower()
        bot_action = random.choice(actions)

        if user_action in actions:
            print(f'You chose {user_action} and the computer chose {bot_action}')

            if bot_action == winning[user_action]:
                print(f'You win! {user_action} beats {bot_action}.')
            elif user_action == bot_action:
                print(f'It\'s a tie! Both chose {user_action}.')
            else:
                print(f'You lose! {bot_action} beats {user_action}.')

            while True:
                play_again = input('Do you want to play again? (yes or no)\n').lower()

                if play_again in ['yes', 'no']:
                    if play_again == 'no':
                        print('See you next time!')
                        playing = False
                        break
                    else:
                        break
                else:
                    print('I didn\'t understand that. Please type yes or no.')
        else:
            print('Invalid input. Please choose rock, paper or scissors.')


def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input('Guess a number between 1 and 100\n'))
        except ValueError:
            print('That is not a valid number.')
            continue

        if guess > secret_number:
            print(f'{guess} is higher than the secret number.')
            attempts += 1
        elif guess < secret_number:
            print(f'{guess} is lower than the secret number.')
            attempts += 1
        else:
            attempts += 1
            print(f'Congratulations! {guess} was the correct number. You took {attempts} attempts.')
            break


def menu():
    while True:
        choice = input('''What do you want to do?
1. Play Rock Paper Scissors
2. Play Guess the Number
3. Exit
''')

        if choice in ['1', '2', '3']:
            if choice == '1':
                rock_paper_scissors()
            elif choice == '2':
                guess_the_number()
            else:
                print('Goodbye!')
                break
        else:
            print('Please choose 1, 2 or 3.')


menu()