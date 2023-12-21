def func(user_input):
    try:
        number = float(import_word)
        if number > 0:
            if number.is_integer():
                return "Ви ввели позитивне ціле число"
            else:
                return "Ви ввели позитивне дробове число"
        elif number < 0:
            if number.is_integer():
                return "Ви ввели від'ємне ціле число"
            else:
                return "Ви ввели від'ємне дробове число"
        elif number == 0:
            return "Ви ввели нуль"
    except ValueError:
        return "Ви ввели не коректне число"



while True:
    import_word = input("Введіть якесь число, або одне із значень(щоб вийти): Вихід, Exit, Quit, E або Q: ")
    if import_word in ["Вихід" , "Exit" , "Quit" , "E" , "Q"]:
     break
    else:
        result = func(import_word)
        print(result if result else "Ви ввели не правильне число")








