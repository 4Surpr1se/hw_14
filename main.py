from flask import Flask, jsonify
import utils

app = Flask(__name__)


@app.route("/movie/<title>")  # Добавить поиск на главную, а не через url
def main_page(title):
    info = utils.movie_finder(title)
    info = utils.info_by_id(info)
    return jsonify(info)


@app.route("/movie/<int:year>/to/<int:year2>")
def year_to_year(year, year2):
    data = utils.year_to_year(year, year2)
    return jsonify(data)


@app.route("/rating/children")
def movie_for_children():
    data = utils.movie_for_children()
    return jsonify(data)


@app.route("/rating/family")
def movie_for_family():
    data = utils.movie_for_family()
    return jsonify(data)


@app.route("/rating/adult")
def movie_for_adult():
    data = utils.movie_for_adult()
    return jsonify(data)


@app.route("/genre/<genre>")
def movie_by_listed_in(genre):
    data = utils.movie_by_listed_in(genre)
    return jsonify(data)


if __name__ == '__main__':
    app.run()
