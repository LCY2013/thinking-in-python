def func(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


func(124, 'magic', hello='world', me='ff')
