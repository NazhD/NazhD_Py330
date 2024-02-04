# from flask import Flask, render_template
#
#
# app = Flask(__name__)
#
#
# menu = [
#     {"name": "Главная", "url": "index"},
#     {"name": "Добавить пост", "url": "addComment"},
#     {"name": "Регистрация", "url": "reg"}
# ]
#
#
# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template("index.html", title="Главная", menu=menu)
#
#
# @app.route('/addComment', methods=["POST", "GET"])
# def add_com():
#     return render_template("addComment.html", title="Добавить пост", menu=menu)
#
#
# @app.route('/reg', methods=["POST", "GET"])
# def reg():
#     return render_template("reg.html", title="Регистрация", menu=menu)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
