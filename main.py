from flask import Flask
# from src.facebook import FacebookPy
from src.photoshop import PhotoshopPy
from src.instagram import InstagramPy

app = Flask(__name__)


@app.route('/')
def raiz():
    return 'Olá mundo!'


''' @app.route('/facebook')
def facebook():
    FacebookPy.post()
    return 'Postado no Facebook!'


@app.route('/twitter')
def twitter():
    FacebookPy.post()
    return 'Postado no Twitter!'


 '''


@app.route('/instagram')
def instagram():
    instagramPy = InstagramPy()
    instagramPy.post()
    return 'Postado no Instagram!'


@app.route('/photoshop')
def photoshop():
    photoshopy = PhotoshopPy()
    photoshopy.openApp()
    return 'Photoshop aberto!'


app.run(debug=True)
