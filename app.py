from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    escolha = request.form.get('escolha', None)

    if not escolha:
        return render_template('index.html', erro="Você precisa fazer uma escolha!")

    if escolha == 'cat':
        return render_cat()
    elif escolha == 'fox':
        return render_fox()
    elif escolha == 'dog':
        return render_dog()
    else:
        return render_duck()


@app.route('/cat', methods=['GET', 'POST'])
def render_cat():
    API_ENDPOINT = 'https://api.thecatapi.com/v1/images/search'
    if request.method == 'GET':
        return render_template('cat.html')

    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        dados = response.json()
        url_imagem = dados[0]['url']
        return render_template('cat.html', url_img=url_imagem)
    else:
        print(response.status_code)
        return render_template('cat.html', erro="Erro no sistema! O gato sumiu!")


@app.route('/fox', methods=['GET', 'POST'])
def render_fox():
    API_ENDPOINT = 'https://randomfox.ca/floof/'
    if request.method == 'GET':
        return render_template('fox.html')

    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        dados = response.json()
        url_imagem = dados['image']
        return render_template('fox.html', url_img=url_imagem)
    else:
        print(response.status_code)
        return render_template('fox.html', erro="Erro no sistema! A raposa sumiu!")


@app.route('/dog', methods=['GET', 'POST'])
def render_dog():
    API_ENDPOINT = 'https://random.dog/woof.json'
    if request.method == 'GET':
        return render_template('dog.html')

    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        dados = response.json()
        url_imagem = dados['url']
        return render_template('dog.html', url_img=url_imagem)
    else:
        print(response.status_code)
        return render_template('dog.html', erro="Erro no sistema! O cachorro sumiu!")


@app.route('/duck', methods=['GET', 'POST'])
def render_duck():
    API_ENDPOINT = 'https://random-d.uk/api/random'
    if request.method == 'GET':
        return render_template('duck.html')

    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        dados = response.json()
        url_imagem = dados['url']
        return render_template('duck.html', url_img=url_imagem)
    else:
        print(response.status_code)
        return render_template('duck.html', erro="Erro no sistema! O pato sumiu!")


if __name__ == '__main__':
    app.run(debug=True)
