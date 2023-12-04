from flask import Flask
from view import views
app = Flask(__name__)
 
app.register_blueprint(views,url_prefix="/" )
app.secret_key = "secret key"
if __name__ == '__main__':
    app.run(debug = True, port = 8000)