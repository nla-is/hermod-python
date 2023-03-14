from datax import DataX

if __name__ == '__main__':
    dx = DataX()
    while True:
        stream, reference, message = dx.next()
        message['repeated'] = True
        message['repeatedFrom'] = stream
        dx.emit(message, reference)
