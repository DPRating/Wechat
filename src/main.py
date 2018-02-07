

# filename: main.py
import web
from handle import Handle
from initialize import Initialize

urls = (
    '/', 'Handle',
)

if __name__ == '__main__':
    Initialize()
    app = web.application(urls, globals())
    app.run()
