"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    #hay = input ("Как дела?")
    try:
       print("Как дела?")
       hay = input ()
    
    
       while hay.lower() != "хорошо":
          try:
              print("Как дела?")
              hay = input ()
          except KeyboardInterrupt:
             print ("Пока")
             break
       else:
        print ("Я очень рад")
    except KeyboardInterrupt:
           print ("Пока")


if __name__ == "__main__":
       hello_user()
