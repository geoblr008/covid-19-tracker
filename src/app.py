from flask import Flask, render_template
from handler import *

app = Flask(__name__, static_folder="assets", template_folder="templates")


@app.route('/')
def hello():
    global_data = world_data()
    top_country, country_list = get_top_five()
    print(top_country)
    return render_template("index.html", global_data=global_data, top_country=top_country, country_list = country_list)


if __name__ == '__main__':
    app.run(debug=True)
