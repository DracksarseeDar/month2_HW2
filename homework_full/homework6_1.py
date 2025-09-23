from datetime import datetime as dt
from time import sleep


def checktime_before_after(func):
    def wrapper(*args,**kwargs):
        time_start = dt.now()
        print(f'Функция была вызвана в {time_start.strftime("%Y-%m-%d %H:%M:%S")}')
        result = func(*args,**kwargs)
        time_end = dt.now()
        print(f'Функция была закончена в {time_end.strftime("%Y-%m-%d %H:%M:%S")}')
        return result
    return wrapper

@checktime_before_after
def world_time():
    print('world time')
    sleep(2)

world_time()

































