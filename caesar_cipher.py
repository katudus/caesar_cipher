# Мини-проект: Шифр Цезаря
ENG_ALPHABET = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]
RUS_ALPHABET = [chr(i) for i in range(1040, 1104)]


def cezar(text, step):
    if text[0] in ENG_ALPHABET:
        alphabet = ENG_ALPHABET
        moch = 26
    else:
        alphabet = RUS_ALPHABET
        moch = 32
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                print(alphabet[(alphabet.index(text[i]) + step) % moch], end="")
            else:
                print(alphabet[(alphabet.index(text[i]) + step) % moch + moch], end="")
        else:
            print(text[i], end="")


print("Программа шифровки / дешифровки текста по методу Цезаря")

while True:
    whats_text = input("\nКакой текст нужно использовать сейчас?\n")
    while whats_text.isspace():
        whats_text = input("Введите текст.\n")
    if 'ё' in whats_text:
        whats_text.replace('ё', 'е')

    whats_step = input(
    "На сколько символовов мы сдвигаем буквы по алфавиту? Ответ напиши числом. Для шифрования положительное, для дешифрования отрицательное.\n"
    )
    while not (whats_step.isdigit() or whats_step[0] == '-' and whats_step[1:].isdigit()):
        whats_step = input("Что-то не то ты ввёл. Напиши число.\n")
    whats_step = int(whats_step)

    print("Результат:")
    cezar(whats_text, whats_step)
    
    if input("\nНажмите '+' чтобы завершить программу.\n") == '+':
        break
