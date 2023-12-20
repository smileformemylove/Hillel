import random

def secrt_num():
    return random.randint(1, 10)

def game():
    tryis = 3
    secret_number = secrt_num()
    print("Спробуйте вгадати число від 1 до 10. У вас є 3 спроби.")

    for attempt in range(tryis):
        user_num = int(input(f"Спроба {attempt + 1}: Введіть число: "))

        if user_num == secret_number:
            print(f"Ви вгадали загадане число, це була: {secret_number}")
            return

        if attempt < tryis -1:
            if user_num < secret_number:
              print("Загадане більше число")
            else:
               print("Загадане меньше число")
    print(f"На жаль загадане число було {secret_number}. У вас закінчились спроби")

game()








