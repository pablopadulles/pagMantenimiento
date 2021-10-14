from flask import Flask, render_template, Response, jsonify, request, url_for, redirect, session


app = Flask(__name__)
configfile = os.environ.get('FLASK_CONFIG')
app.secret_key = b'p\xa6]\xda\xbe\xfd\xc4{b\xffk$\xfd\x13\xe8(\x1e\x14\x03p\x03P\x08B@\xec\xe0\xde\xa3S\x03k'

@app.route('/home')
@app.route('/home.html')
@app.route('/index.html')
@app.route('/', methods=["GET", "POST"])
@tryton.transaction()
def index():
    if request.method == "GET":
        return render_template('actualizando.html')


#AJAC cada ves q agrega un articulo a su carrito, tienen q agregarlo a "session"
if __name__ == '__main__':

    app.run(host='0.0.0.0', threaded=True)
