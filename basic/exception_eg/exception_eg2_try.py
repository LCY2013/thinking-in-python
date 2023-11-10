try:
    1 / 0
except Exception as e:
    try:
        1 / 0
    except Exception as f:
        pass
    print(e)
