from brain_games.cli import welcome_user
import random
import prompt

def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = random.randint(1, 1000)
        right_answer = 'yes' if not number % 2 else 'no'
        print(f'Question: {number}')
        player_answer = prompt.string('Your answer: ')

        if player_answer == right_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()