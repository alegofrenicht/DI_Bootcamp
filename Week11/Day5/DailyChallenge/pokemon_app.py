from flask import Flask, render_template
import data_manager

app = Flask(__name__)
data = data_manager


@app.route('/')
def types_page():
    html = render_template('main.html', pokemon_data=data.by_type())
    return html


@app.route('/type/<type_id>')
def pokemon_type(type_id):
    html = render_template('pokemon_type.html', pokemon_type=data.type_by_id(type_id), json_func=data.poke_by_id)
    return html


@app.route('/pokemons/all')
def all_pokemons():
    html = render_template('all_pokemons.html', pokemons=data.all_pokemons()['results'], json_func=data.poke_by_id)
    return html

@app.route('/pokemons/<pok_id>')
def pok_by_name(pok_id):
    html = render_template('pokemon.html', pokemon=data.poke_by_id(pok_id), id=pok_id)
    return html

app.run()
