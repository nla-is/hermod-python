import hermod
import time


def handler(input_message):
    return {'timestamp': int(time.time() * 1000)}


if __name__ == '__main__':
    hermod.run(handler)
