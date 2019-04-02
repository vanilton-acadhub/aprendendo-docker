from flask import Flask
app = Flask(__name__) # Inicializa o Flask e define o objeto de aplicativo

# Definimos uma rota, sempre que essa url for utilizada vamos executar o método hello_world()
@app.route('/')
def hello_world():
    return 'Hello World!\n'
    
if __name__ == '__main__':
    # Utilizamos 0.0.0.0 para permitir o acesso partindo do host ou de outros contêineres
    app.run(debug=True, host='0.0.0.0')