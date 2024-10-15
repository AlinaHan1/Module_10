from threading import Thread  # Для работы с потоками
from datetime import datetime  # Для учета времени работы
from time import sleep  # Для задержки на 0.1 секунду

# ОБЪЯВИТЬ ФУНКЦИЮ ДЛЯ ЗАПИСИ СЛОВ В СООТВЕТСТВУЮЩИЙ ФАЙЛ
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

# ВЗЯТИЕ ТЕКУЩЕГО ВРЕМЕНИ/ ЗАПУСК ФУНУКЦИИ С АРГУМЕНТАМИ ИЗ ЗАДАЧИ/ ВЗЯТИЕ ТЕКУЩЕГО ВРЕМЕНИ/ ВЫВОД РАЗНИЦЫ
start_time = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = datetime.now()
res_time = end_time - start_time
print(f'Время работы функции: {res_time}')
# СОЗДАНИЕ ПОТОКОВ
thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_four = Thread(target=write_words, args=(100, 'example8.txt'))
# ВЗЯТИЕ ТЕКУЩЕГО ВРЕМЕНИ/ ЗАПУСК ПОТОКОВ С АРГУМЕНТАМИ ИЗ ЗАДАЧИ
start_time = datetime.now()
thr_first.start()
thr_second.start()
thr_third.start()
thr_four.start()
# ОКОНЧАНИЕ ПОТОКОВ/ ВЗЯТИЕ ТЕКУЩЕГО ВРЕМЕНИ/ ВЫВОД РАЗНИЦЫ
thr_first.join()
thr_second.join()
thr_third.join()
thr_four.join()
end_time = datetime.now()
res_time = end_time - start_time
print(f'Время работы потока: {res_time}')
