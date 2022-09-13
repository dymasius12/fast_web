from flask import Flask

app = Flask(__name__)

# So you dont need to running the script while coding
if __name__ == '__main__':
    app.run(debug=True, port=8000)

