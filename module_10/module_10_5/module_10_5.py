from datetime import datetime
from  multiprocessing import Pool, cpu_count

def read_info(name):
    all_data = []
    with open(name, "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if line == "":
                break
            all_data.append(line)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = datetime.now()
    for filename in filenames:
        read_info(filename)
    end_time = datetime.now()
    print(f"{end_time - start_time} (линейный)")

    start_time = datetime.now()
    with Pool(cpu_count()) as pool:
        pool.map(read_info, filenames)
    end_time = datetime.now()
    print(f"{end_time - start_time} (многопроцессный)")