from datax import DataX
import time

if __name__ == '__main__':
    dx = DataX()
    while True:
        message = {'timestamp': int(time.time() * 1000)}
        dx.emit(message)
        time.sleep(0.05)
