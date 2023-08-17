from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text, 200


@app.route('/todos', methods=['POST'])
def add_new_todo():
    decoded = request.get_json()  # decodifica la peticion
    print("petition es igual: ", decoded)
# Agrego el diccionario a la lista todos:
    todos.append(decoded)
    print(todos)

    # Devolver la lista jsonificada:
    json_text = jsonify(todos)
    return json_text, 200





@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)

    longitud = len(todos)  # cantidad de elementos
    print("longitud: ", longitud)

    max_index = longitud - 1
    if position > max_index:
        return jsonify({"mensaje": "el numero es mayor a la cantidad de indices"})

    if longitud == 0:
        return jsonify({"mensaje": "la lista esta vacias y por eso max_ondex esta vacia"})

    #Ahora eliminamos elementos de la lista segun su indice
    todos.pop(position)

    json_text = jsonify(todos)
    return json_text, 200


# Estas dos líneas siempre seben estar al final de tu archivo app.py.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)