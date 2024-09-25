import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line.strip() != '':
            all_data.append(line)
            line = file.readline()


file_names = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':

    # Линейный вызов
    start_1 = datetime.datetime.now()
    for file_name in file_names:
        read_info(file_name)
    end_1 = datetime.datetime.now()
    print(f'{end_1 - start_1} - время линейного вызова.')

    # Многопроцессный вызов
    start_2 = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_names)
    end_2 = datetime.datetime.now()
    print(f'{end_2 - start_2} - время многопроцессорного вызова.')
