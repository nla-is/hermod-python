import hermod


def handler(input_message):
    input_message['repeated'] = True
    return input_message


if __name__ == '__main__':
    hermod.run(handler)
