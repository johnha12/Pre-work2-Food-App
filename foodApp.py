from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
  if request.method =="POST":
    ingrediant = request.form["food"]
    new_url = "https://api.spoonacular.com/recipes/complexSearch?apiKey=40fc548487854a7db79b65f0d14bc1c1&query="+ingrediant+"&sort=calories&sortDirection=asc&number=3"
    return redirect(new_url)
  
  # if request.method == "GET":
  #   # ingrediant = request.form["food"]
  #   # return redirect(url_for("https://api.spoonacular.com/recipes/complexSearch?apiKey=40fc548487854a7db79b65f0d14bc1c1&query="+ingrediant+"&sort=calories&sortDirection=asc&number=3"))
  #   return render_template("testing.html")

  else: return render_template("index.html")

@app.route("/search", methods=["POST", "GET"])
def search():
  if request.method =="POST":
    ingrediant = request.form["food"]
    # new_url = "https://api.spoonacular.com/recipes/complexSearch?apiKey=40fc548487854a7db79b65f0d14bc1c1&query="+ingrediant+"&sort=calories&sortDirection=asc&number=3"
    return redirect(url_for())
  


# @app.route("/<food>")
# def ingrediant(food):
#   return redirect(url_for("https://api.spoonacular.com/recipes/complexSearch?apiKey=40fc548487854a7db79b65f0d14bc1c1&query="+ingrediant+"&sort=calories&sortDirection=asc&number=3"))


if __name__ == "__main__":
  app.run(debug=True)