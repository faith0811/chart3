# chart3/run.py
import app

if __name__ == '__main__':
    app.socketio.run(app.app, host = '0.0.0.0')
