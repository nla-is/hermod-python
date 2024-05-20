import hermod


def handler(**kwargs) -> dict:
    kwargs['repeated'] = True
    return kwargs


if __name__ == '__main__':
    hermod.run(handler)
