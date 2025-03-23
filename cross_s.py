from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "")
    return f"""
        <h1>Merhaba {name}</h1>
        <form method="get">
            İsim: <input type="text" name="name">
            <input type="submit" value="Gönder">
        </form>
    """

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() in ("true", "1", "t")
    app.run(debug=debug_mode)
