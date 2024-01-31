from gateway_communicator import write
from config_to_communicator import licht_schalten, licht_dimmen, jalousie_fahren

from flask import Flask, jsonify, request
from urllib.parse import unquote

app = Flask(__name__)

SECRET_TOKEN = "HIER KOMMT IRGENDWANN WAS BESSERS HIN HOFFE ICH DICH ABER SUPER GEHEIM:15649849853453/"


@app.route('/api/whatever/<string:encoded_id>', methods=['GET'])
async def your_endpoint(encoded_id):
    if 'Authorization' not in request.headers or request.headers['Authorization'] != f'Bearer {SECRET_TOKEN}':
        return jsonify({"error": "Unauthorized"}), 401

    command_type = request.args.get('type')
    state = int(request.args.get('state'))
    decoded_id = unquote(encoded_id.replace('-', '/'))
    print(f"Received request about {command_type} for div_id {decoded_id} with state {state}")
    if '/' not in decoded_id:
        print("Name")
        if command_type == "licht_schalten":
            print("Licht schalten")
            # await licht_schalten(decoded_id, state)
        elif command_type == "licht_dimmen":
            print("Licht dimmen")
            # await licht_dimmen(decoded_id, state)
        elif command_type == "jalousie_fahren":
            print("Jalousie fahren")
            # await jalousie_fahren(decoded_id, state)
    else:
        print("Gruppenadresse")
        # await write(decoded_id, state)

    data = {"message": f"Successfully received request about {command_type} for div_id {decoded_id} with state {state}"}

    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':
    app.run(debug=True)
