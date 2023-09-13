"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {'привет':'Привет','как дела': 'Хорошо', 'что делаешь': 'Программирую', 'нравится программировать': 'Да', 'это сложно': 'Нет'}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    ost_while = 0
    while ost_while == 0:
          quest1 = input ("Введите Ваш вопрос   "  )
          question = quest1.lower ()
          if question.endswith("?"):
             question = question [:-1]
          question = question .strip()
          if question in questions_and_answers:
             answer = questions_and_answers [question]
             print (answer)
          else:
            print ("Не понял вопрос")
          if question == "стоп":             # Stop while.
             ost_while = 1

    
 
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
