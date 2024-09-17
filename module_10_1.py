from threading import Thread
from time import sleep
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершена запись в файл {file_name}')


# Работа функций
start_time1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time1 = datetime.now()
print(f'Работа функций: {end_time1 - start_time1}')

# Работа потоков
start_time2 = datetime.now()
the_first = Thread(target=write_words, args=(10, 'example5.txt'))
the_second = Thread(target=write_words, args=(30, 'example6.txt'))
the_third = Thread(target=write_words, args=(200, 'example7.txt'))
the_fourth = Thread(target=write_words, args=(100, 'example8.txt'))

the_first.start()
the_second.start()
the_third.start()
the_fourth.start()

the_first.join()
the_second.join()
the_third.join()
the_fourth.join()
end_time2 = datetime.now()
print(f'Работа потоков: {end_time2 - start_time2}')
