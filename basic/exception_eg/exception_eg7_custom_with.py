class Open:
    def __enter__(self):
        print("open")
        return self

    def __exit__(self, exc_type, exc_value, exc_trace):
        print("close")

    def __call__(self):
        pass


with Open() as f:
    pass

# 上下文协议
