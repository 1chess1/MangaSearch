from Presentation.app import app
from bottle import run

if __name__ == "__main__":
    run(app, host='localhost', port=8080, debug=True, reloader=True)
