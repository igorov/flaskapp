from flask import Flask, render_template, request, redirect, url_for
import os
import requests
import json

#template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
#template_dir = os.path.join(template_dir, 'src', 'templates')
template_dir = os.path.join(os.path.dirname(__file__), 'templates')

app = Flask(__name__, template_folder = template_dir)
api_cliente_url = os.environ.get('SERVICE_URL')

# Rutas de la aplicación
@app.route('/')
def home():
    try:
        response = requests.get(api_cliente_url)

        if response.status_code == 200:
            print(f'ruta:{template_dir}')
            data = response.json()
            return render_template('index.html', data = data)
            print("OK")
        else:
            print('error')
            return 'Error en la solicitud: {}'.format(response.status_code)
    except requests.exceptions.RequestException as e:
        # Manejar cualquier error de solicitud
        return 'Error en la solicitud: {}'.format(str(e))

@app.route('/cliente', methods = ['POST'])
def addCliente():
    headers = {'Content-Type': 'application/json'}

    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    email = request.form['email']
    

    if nombres and apellidos and email:
        data = {
            'nombres': nombres,
            'apellidos': apellidos,
            'email': email
        }
        json_data = json.dumps(data)

        response = requests.post(api_cliente_url, data=json_data, headers=headers)

        # Verificar el código de respuesta
        if response.status_code == 201:
            print('se creo correctamente')
        else:
            print('error al crear')
        return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    headers = {'Content-Type': 'application/json'}
    response = requests.delete(f'{api_cliente_url}/{id}', headers=headers)

    if response.status_code == 200:
            print('se elimino correctamente')
    else:
        print('error al eliminar')
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    headers = {'Content-Type': 'application/json'}

    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    email = request.form['email']

    data = {
        'nombres': nombres,
        'apellidos': apellidos,
        'email': email
    }
    json_data = json.dumps(data)

    response = requests.put(f'{api_cliente_url}/{id}', data=json_data, headers=headers)
    if response.status_code == 200:
            print('se elimino correctamente')
    else:
        print('error al eliminar')
    return redirect(url_for('home'))


if __name__ == '__main__':
    #app.run(debug = True, port = 4000)
    app.run(debug = True, host='0.0.0.0', port = 4000)