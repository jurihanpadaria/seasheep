from flask import Flask, render_template

# Cria o site
app = Flask(__name__)

# Homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

# Acrescentando mais páginas
@app.route('/about')
def about():
    return render_template('about.html')

# Debugger - permite que erros sejam mostrados
if __name__ == '__main__':
    app.run(debug=True)