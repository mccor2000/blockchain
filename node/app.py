import json

from flask import Flask, request

from lib.transaction import Transaction

app = Flask(__name__)


@app.route('/validate', methods=['POST'])
def validate():
    tx_content = request.get_json()
    tx = Transaction(**tx_content)

    result = Transaction.validate(tx)
    # TODO
    # + validate tx
    # + write tx to share volume

    return json({'result': result})


if __name__ == '__main__':
    print('Node is running..')
    app.run(host='127.0.0.1', port=5000)
