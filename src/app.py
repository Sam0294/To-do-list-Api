from flask import Flask, jsonify, request
import json



app = Flask(__name__)

@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'

todos =[{ "label": "My first task", "done": False }]

@app.route('/todos', methods=['GET'])
def hello():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    decoded_object = json.loads(request.data)
    todos.append(decoded_object)
    return str(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    limit = len(todos)
    if limit -1  < position:
        return "error"
    else:
        todos.pop(position - 1)
        return str(todos)


# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)