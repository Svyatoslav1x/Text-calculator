import os
from word2numberi18n import w2n
from colorama import Fore

def converter(expr: str) -> str:
    '''
    Это функция конвертер, конвертирует строку, в строку для использования функцией eval()
    Т.е. группируем слова и конвертируем их в цифры с помощью библиотеки w2ni18n,
    конвертируем слова в операции и т.д.  
    '''
    # Конвертируем все кроме цифр
    expr = expr.replace('минус', '-').replace('плюс', '+').replace('делить на', '/').replace('умножить на', '*').split()
    # Задаем переменные для работы последующего кода
    non_num = '+/-*'
    res = "" # Здесь храним результирующую строку для `eval()`
    i = 0
    tmp_num = "" # Будет хранить в себе число в виде слов для перевода в цифру 

    # Запускаем цикл, чтобы пройтись по `expr`: list
    while i < len(expr):
        if expr[i] in non_num: # Проверяем, что данная переменная не число
            res += expr[i] # Обновляем `res`
        else:
            tmp_num = expr[i] # Создаем временную строку
            if (i < (len(expr) - 1)) and expr[i + 1] not in non_num: # Условие для начала группировки в `tmp_num`
                while (i < (len(expr) - 1)) and (expr[i + 1] not in non_num):
                    tmp_num += expr[i + 1] # Обновляем `tmp_num`
                    i += 1
                i += 1
            try:
                res += str(w2n.word_to_num(tmp_num)) # Ловим ошибки
            except:
                print("Please enter a valid number word!")
        i += 1
    return res # Возращаем результат работы `converter`

def main() -> None:
    '''
    Основная функция программы
    '''
    os.environ['w2n.lang'] = 'ru' # Задаем русский язык для работы библиотеки `w2ni18`
    # Ввод математического выражения
    expression = converter(input("Введите текстовое математическое выражение: ")) # Обрабатываем введенное математическое выражение
    print(Fore.GREEN + f"Результат: {eval(expression)}") # Получаем результат с помощью `eval()` и выводим его


if __name__ == "__main__":
    main()