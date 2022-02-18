from flask import Flask, render_template, request
from handler import *

app = Flask(__name__, static_folder="assets", template_folder="templates")

msg = """
      <div
        class="row row-cols-1 text-center justify-content-center align-items-center"
      >
        <h1 style="font-family: Poppins, sans-serif">Covid in {}</h1>
        <br>
        <div class="col">
          <h1 class="text-center" style="font-family: Poppins, sans-serif">
            {}
          </h1>
          <p style="font-family: Poppins, sans-serif">Total Cases</p>
        </div>
      </div>
      <div class="row text-end justify-content-center align-items-center">
        <div class="col-5 text-center align-self-start">
          <h1 style="font-family: Poppins, sans-serif">{}</h1>
          <p style="font-family: Poppins, sans-serif">Total Deaths</p>
        </div>
        <div class="col-5 text-center align-self-start">
          <h1 style="font-family: Poppins, sans-serif">{}</h1>
          <p style="font-family: Poppins, sans-serif">Recovered</p>
        </div>
      </div>
"""


@app.route('/', methods=["GET", "POST"])
def index():
    global_data = world_data()
    top_country, country_list = get_top_five()

    if request.method == "GET":
        return render_template("index.html", global_data=global_data,
                               top_country=top_country,
                               country_list=country_list)
    elif request.method == "POST":
        text = request.form['country_search']
        country_list_data = get_data(text)

        html = msg.format(text.title(),
                          country_list_data["total_infected"],
                          country_list_data["total_deaths"],
                          country_list_data["recovred"])

        return render_template("index.html", global_data=global_data,
                               top_country=top_country,
                               country_list=country_list, html=html)


if __name__ == '__main__':
    app.run(debug=True)
