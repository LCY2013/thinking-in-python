from flask import Flask, Request
# from flask.globals import _request_ctx_stack
from flask.globals import request_ctx

app = Flask(__name__)


@app.route('/')
def index():
    # 获取ctx对象
    # ctx = _request_ctx_stack.top
    ctx = request_ctx
    # Request 上下文管理
    print(ctx)
    print(ctx.request.method)  # GET
    return 'index'


if __name__ == '__main__':
    app.run()
