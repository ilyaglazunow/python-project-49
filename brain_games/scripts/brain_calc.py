from brain_games.cli import welcome_user
import random
import prompt


def main():
    name = welcome_user()
    print('What is the result of the expression')
    counter = 0
    while counter < 3:
        num_1 = random.randint(1, 100)
        num_2 = random.randint(1, 100)
        question = f"{num_1} {random.choice(['*', '+'])} {num_2}"
        right_answer = eval(question)
        print(f'Question: {question}')
        player_answer = int(prompt.string('Your answer: '))

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