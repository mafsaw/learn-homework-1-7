"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
sum1 = 0  #total number of Iphone sales
sum2 =0  #total number of Xiomi sales
sum3 = 0  #total number of Samsung Galaxy sales
sum_oll = 0  # total number of sales of all phones 
av1 = 0     #average number of sales of Iphone
av2 = 0     #average number of sales of Samsung Galaxsy
av3 = 0     #average number of sales of Xiaomi
av_oll = 0  #average number of sales of all phones

product =  {'iPhone 12':[363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186],
'Xiaomi Mi11':[317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316],'Samsung Galaxy':
[343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}

def count(phone): #function of calculating the total sales volume of each type of phone
    i = 0
    x = 0
    y = 0
    sum = 0
    for i in range(12):
         x = product[phone][y]
      
         i = i+1
         y = y+1
         sum = sum+x
    return sum
sum = "iPhone 12" 
sum1 = count(sum)
sum = 'Xiaomi Mi11'
sum2 = count(sum)
sum = 'Samsung Galaxy'
sum3 = count(sum)
print ("total number of Iphone sales")
print (sum1)
print ("total number of Xiomi sales")
print (sum2)
print ("total number of Samsung Galaxy sales")
print (sum3)
sum_oll=sum1+sum2+sum3
print ("total number of sales of all phones")
print (sum_oll) 
av1 = round(sum1 / 12)   
print("average number of sales of Iphone")
print (av1)
av2 = round(sum2/12)
print ("average number of sales of Samsung Galaxsy")
print (av2)
av3 = round(sum3/12)    
print ("average number of sales of Xiaomi")
print (av3)
av_oll = round(sum_oll/12)
print ("average number of sales of all phones")
print (av_oll)


    
if __name__ == "__main__":
    main()
