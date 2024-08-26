import multiprocessing
import datetime


def read_info(name):

    all_data = []
    with open(name) as f:
        while True:
            a = f.readline()
            all_data.append(a)
            if not a:
                break

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start = datetime.datetime.now()
for i in filenames:
    read_info(i)
end = datetime.datetime.now()
print(end - start, '(линейный)')

# Многопроцессный
if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start, '(многопроцессный)')