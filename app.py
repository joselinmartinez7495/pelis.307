from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categoria/<cat>')
def categoria(cat):
    categorias = ['infantil', 'romance', 'suspenso', 'terror']
    if cat in categorias:
        return render_template(f'{cat}.html')
    else:
        return render_template('error.html', categoria=cat), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', categoria=None), 404

if __name__ == '__main__':
    app.run(debug=True)
