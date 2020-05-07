from flask import Flask, render_template, request, redirect
app = Flask(__name__)

pokemons = [
    ['Bulbasaur', 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png'],
    ['Charmander', 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png'],
    ['Squirtle', 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/007.png'],
    ['Pikachu', 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png']
]

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
        pokemon=poke
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

if __name__ == '__main__':
    app.run()