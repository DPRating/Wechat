

# filename: main.py
import web
from log import CreateLog
from handle import Handle

urls = (
    '/', 'Handle',
)

if __name__ == '__main__':
    CreateLog()
    app = web.application(urls, globals())
    app.run()
