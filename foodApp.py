from flask import Flask, redirect, url_for, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
  if request.method =="POST":
    ingrediant = request.form["food"]
    new_url = "https://api.spoonacular.com/recipes/complexSearch?apiKey=40fc548487854a7db79b65f0d14bc1c1&query="+ingrediant+"&sort=calories&sortDirection=asc&number=3"
    data = requests.get(new_url).json()

    min_results = min(3, len(data['results']))
    if min_results == 0:
      return render_template("no_results.html")
    if min_results >= 1:
      title1 = data['results'][0]["title"]
      image1 = data['results'][0]["image"]
      nutrition1 = data['results'][0]["nutrition"]
    if min_results == 1:
      return render_template("search.html", title1 = title1, image1 = image1, nutrition1 = nutrition1)

    if min_results >= 2:
      title2 = data['results'][1]["title"]
      image2 = data['results'][1]["image"]
      nutrition2 = data['results'][1]["nutrition"]
    if min_results == 2:
      return render_template("search.html", title1 = title1, image1 = image1, nutrition1 = nutrition1, title2 = title2, image2 = image2, nutrition2 = nutrition2)

    if min_results >= 3:
      title3 = data['results'][2]["title"]
      image3 = data['results'][2]["image"]
      nutrition3 = data['results'][2]["nutrition"]

    return render_template("search.html", title1 = title1, image1 = image1, nutrition1 = nutrition1, title2 = title2, image2 = image2, nutrition2 = nutrition2, title3 = title3, image3 = image3, nutrition3 = nutrition3)
    
  else: return render_template("index.html")
  
@app.route('/testing')
def get_data():
    # dummy variable to avoid api call limit
    data = {'results': [{'id': 659929, 'title': 'Shrimp and Cucumber Lettuce Wraps With Fresh Dill', 'image': 'https://img.spoonacular.com/recipes/659929-312x231.jpg', 'imageType': 'jpg', 'nutrition': {'nutrients': [{'name': 'Calories', 'amount': 30.0658, 'unit': 'kcal'}]}}, {'id': 632819, 'title': 'Asian Chickpea Lettuce Wraps', 'image': 'https://img.spoonacular.com/recipes/632819-312x231.jpg', 'imageType': 'jpg', 'nutrition': {'nutrients': [{'name': 'Calories', 'amount': 51.6565, 'unit': 'kcal'}]}}, {'id': 632795, 'title': 'Asian Barbecue Chicken Lettuce Wraps', 'image': 'https://img.spoonacular.com/recipes/632795-312x231.jpg', 'imageType': 'jpg', 'nutrition': {'nutrients': [{'name': 'Calories', 'amount': 60.3717, 'unit': 'kcal'}]}}], 'offset': 0, 'number': 3, 'totalResults': 112}

    data2 = []
    for i in range(3):
      data2.append([data['results'][i]["title"], data['results'][i]["image"], data['results'][i]["nutrition"]])

    title1 = data['results'][0]["title"]
    image1 = data['results'][0]["image"]
    nutrition1 = data['results'][0]["nutrition"]

    title2 = data['results'][1]["title"]
    image2 = data['results'][1]["image"]
    nutrition2 = data['results'][1]["nutrition"]

    title3 = data['results'][2]["title"]
    image3 = data['results'][2]["image"]
    nutrition3 = data['results'][2]["nutrition"]

    return render_template("search.html", title1 = title1, image1 = image1, nutrition1 = nutrition1, title2 = title2, image2 = image2, nutrition2 = nutrition2, title3 = title3, image3 = image3, nutrition3 = nutrition3)
  
@app.route('/testing2')
def get_data2():
    # dummy variable to avoid api call limit
    data = {'results': [{'id': 659929, 'title': 'Shrimp and Cucumber Lettuce Wraps With Fresh Dill', 'image': 'https://img.spoonacular.com/recipes/659929-312x231.jpg', 'imageType': 'jpg', 'nutrition': {'nutrients': [{'name': 'Calories', 'amount': 30.0658, 'unit': 'kcal'}]}}, {'id': 632819, 'title': 'Asian Chickpea Lettuce Wraps', 'image': 'https://img.spoonacular.com/recipes/632819-312x231.jpg', 'imageType': 'jpg', 'nutrition': {'nutrients': [{'name': 'Calories', 'amount': 51.6565, 'unit': 'kcal'}]}}]}
    data = {'results': []}

    min_results = min(3, len(data['results']))
    if min_results == 0:
      return render_template("no_results.html")
    if min_results >= 1:
      title1 = data['results'][0]["title"]
      image1 = data['results'][0]["image"]
      nutrition1 = data['results'][0]["nutrition"]
    if min_results == 1:
      return render_template("search.html", title1 = title1, image1 = image1, nutrition1 = nutrition1)

    if min_results >= 2:
      title2 = data['results'][1]["title"]
      image2 = data['results'][1]["image"]
      nutrition2 = data['results'][1]["nutrition"]
    if min_results == 2:
      return render_template("search.html", title1 = title1, image1 = image1, nutrition1 = nutrition1, title2 = title2, image2 = image2, nutrition2 = nutrition2)

    if min_results >= 3:
      title3 = data['results'][2]["title"]
      image3 = data['results'][2]["image"]
      nutrition3 = data['results'][2]["nutrition"]

    return render_template("search.html", title1 = title1, image1 = image1, nutrition1 = nutrition1, title2 = title2, image2 = image2, nutrition2 = nutrition2, title3 = title3, image3 = image3, nutrition3 = nutrition3)

if __name__ == "__main__":
  app.run(debug=True)