import connexion
from flask import Flask, render_template

app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

@app.route('/')
def home():
    """
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) # consider changing to original
