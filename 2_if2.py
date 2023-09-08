"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def mine(Line1, Line2,):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    Status=100
    if isinstance(Line1, str) and isinstance(Line2, str):
        pass
    else:
        Status=0
    if  len(Line1)==len(Line2): 
         Status=1                    
    elif len(Line1) > len(Line2):
        Status=2       
    else:
        Status=0
    if Line2.endswith("learn") and len(Line1) != len(Line2):        
         Status=3    
    else:
         pass
    return Status
    
if __name__ == "__main__":
   Line1="I am go to do it"
   Line2="I want to learn"
   Status1=mine(Line1, Line2)
   print(Status1)


   
