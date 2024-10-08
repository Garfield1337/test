#Имопртируем библиотеку math
import math

#Создал функцию, которая сначала пробует преобразовать значение input из str в float
#Если у нее это не получается сделать, то она просит ввести новое значение и запускает цикл заново
def check(x):
    while x != float:
        try:
            return float(x)
        except:
            x = input('Введите числовое значение!\n')

#Здесь создал цикл, который позволяет вычислить сторону сразу для нескольких треугольников.
#Изначально значение переменной option равняется y
#После мы запускаем цикл, который действует, пока значение переменной option равняется y или t
#Затем она проверяет для каждого варианта отдельно
#В случае, если значение переменной равняется y, проводятся вычисления с выводом результатов на экран с последущим появлением опции выбора "дальнейших действий"
#В случае, если значение переменной равняется t, выводится лист, на котором отображены все прошлые результаты вычислений, а также количество вычислений,
# с последующим появлением опции выбора "дальнейших действий"
#В случае, если пользователь выберет n, то цикл завершается
#В случае, если пользователем ввел значение, не предусмотренное кодом, его просят выбрать значение из предложенных раннее.
input('Давайте рассчитаем значение длины стороны треугольника по теореме косинусов!\n'
      'Нажмите Enter, чтобы продолжить...')
#Понадобится нам позже
list_otvetov = list()
#Ставим для переменной option значение y
option = 'y'
#Запускаем цикл, который будет повторяться, пока значение option равняется y или t
while option == 'y' or option == 't':

#В случае, если значение option равняется t, выводим количество ответов и прошлые ответы
    if option == 't':
        print(f'\nПрошлых ответов: {otvet_number}\n'
              f'Прошлые ответы: {list_otvetov}\n')
#В случае, если значение option равняется y, приступаем к ряду операций по присваиванию
# для переменных значений, введенных пользователем, и подсчету
    if option == 'y':

        side_one = input('Введите значение длинны первой стороны:\n')
#Присваиваем для переменной значение из return
        side_one = check(side_one)

        side_two = input('Введите значение длинны второй стороны:\n')
# Присваиваем для переменной значение из return
        side_two = check(side_two)

        degree = input('Введите значение градуса угла между ними:\n')
# Присваиваем для переменной значение из return
        degree = check(degree)

#Переводим градусы в радианы
        degree = math.radians(degree)
#Добавляем переменные в формулу, используем функции из библиотеки math, чтобы вычислить корень и значение косинуса,
# также с помощью функции round округляем значение переменной до 2 знаков после запятой
        c = round(math.sqrt(side_one ** 2 + side_two ** 2 - 2 * side_one * side_two * math.cos(degree)), 2)
        print(f'\nЗначение длинны третьей стороны: {c}\n')

#Тут блок, ответственный за создание листа ответов и подсчета количества ответов: с помощью оператора .append добавляем значение переменной c к листу list_otvetov и
#с помощью функции .len смотрим количество элементов в списке
        list_otvetov.append(c)
        otvet_number = len(list_otvetov)

#По окончании операций при значениях переменной option y или t, присваиваем новое значение для переменной option
    option = input('Введите: "Y", чтобы определить значение длины при других значениях.\n'
            'Введите: "N", чтобы завершить выполнение программы.\n'
            'Введите "T", чтобы просмотреть историю ответов.\n')
#Использовал функцию .lower, чтобы сделать код нечувствительным к регистру
    option = option.lower()

#В случе, если переменная option не имеет в себе значений, учавствующих в цикле, то мы запускаем новый цикл, заставляющий пользователя сделать ПРАВИЛЬНЫЙ выбор.
#Когда пользователь сделает правильный выбор, цикл выше начинается заново
    while option not in ['y', 'n', 't']:
        option = input('Выберите из предложенного!\n'
            'Введите: "Y", чтобы определить значение длины при других значениях.\n'
            'Введите: "N", чтобы завершить выполнение программы.\n'
            'Введите "T", чтобы просмотреть историю ответов.\n')
#Цикл завершается, если значение переменной option равняется n
if option == 'n':
    input('Вы уверены? Было же так весело...\n')
    quit()