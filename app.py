from flask import Flask
# just importing views variable from views.py
from views import views

app = Flask(__name__)
# Instead you do this:
# that means we going to access all the route in the views.py by "/"
# app.register_blueprint(views, url_prefix="/")

app.register_blueprint(views, url_prefix="/views")

# You can do like below but, it is better to seperate!
# @app.route("/")
# def home():
#     return "this is the home page"

# So you dont need to running the script while coding
if __name__ == '__main__':
    app.run(debug=True, port=8000)

