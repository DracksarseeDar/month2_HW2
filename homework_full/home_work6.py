from datetime import datetime as dt

def checktime(func):
    def wrapper(*args,**kwargs):
        time = dt.now()
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f'Вызвана функция в {formatted_time}')
        result = func(*args,**kwargs)
        return result
    return wrapper

@checktime
def world_time():
    print('world time')

world_time()