from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    print('Master node is running on port 80')
    app.run(host='127.0.0.1', port=80)
