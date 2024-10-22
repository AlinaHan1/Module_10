import multiprocessing
import datetime

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            else:
                all_data.append(line)

file_name = [f'./file{number}.txt' for number in range(1, 5)]
start = datetime.datetime.now()
for name in file_name:
    read_info(name)
end = datetime.datetime.now()
print(end - start)

if __name__ == '__main__':
    pass

