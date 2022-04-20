from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/show", methods=["GET", "POST"])
def index():
    return render_template("web.html")


@app.route("/register", methods=["GET", "POST"])
def reg():
    print(request.form)
    file = request.form.get("pic")
    return "生成成功"


if __name__ == '__main__':
    app.run()
