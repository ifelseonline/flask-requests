from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)

r = requests.get('https://gist.githubusercontent.com/the-akira/4f2244540d61f8a9d3ec73b280af5f9b/raw/78d015d9d61024dc80c2e6c3c66d455b6b32ed3c/pokedex.json')
dados = r.text

pokemons = json.loads(dados)

@app.route('/')
def index():
    return render_template(
        'index.html',
        titulo='Pokédex',
        pokemons=pokemons
    )

@app.route('/poke/<int:id>')
def pokemon(id):
    poke = pokemons[id]
    return render_template(
        'pokemon.html',
        pokemon=poke,
        id=id
    )

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/store', methods=['POST'])
def store():
    nome = request.form['nome']
    img = request.form['img']

    pokemons.append([nome, img])
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    del pokemons[id]
    return redirect('/')

if __name__ == '__main__':
    app.run()