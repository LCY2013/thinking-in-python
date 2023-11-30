def decorate(func):
    print('running in modlue')

    def inner():
        return func()

    return inner
