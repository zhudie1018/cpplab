# 本地静态服务器（可选）。
# 页面本身是纯静态的，直接双击 cpp-lab.html 或用任意静态服务器都能跑；
# 这个脚本只是给你一个方便的本地入口：python cpp_lab_server.py
#
# 它不保存任何 API Key —— AI 出题用的是页面「⚙ 设置」里你自己填的 Key，
# 存在你浏览器本地，不会经过这个服务器。
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get("CPP_LAB_PORT", "8765"))


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)


if __name__ == "__main__":
    print("C++ 练习台： http://127.0.0.1:%d/cpp-lab.html" % PORT)
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
