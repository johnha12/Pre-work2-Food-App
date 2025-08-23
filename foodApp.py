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
    if 'results' not in data and "message" in data:   # used and statement in case there's another error about no results
      print(data['message'])
      message = data['message']
      return render_template("no_results.html", message = message)
    
    min_results = min(3, len(data['results']))
    if min_results == 0:
      message = "No recipes found"
      return render_template("no_results.html", message = message)
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
def get_data2():
    # dummy variable to avoid api call limit
    data = {'results': [{'id': 659929, 'title': 'Shrimp and Cucumber Lettuce Wraps With Fresh Dill', 'image': 'https://img.spoonacular.com/recipes/659929-312x231.jpg', 'imageType': 'jpg', 'nutrition': {'nutrients': [{'name': 'Calories', 'amount': 30.0658, 'unit': 'kcal'}]}}, {'id': 632819, 'title': 'Asian Chickpea Lettuce Wraps', 'image': 'https://img.spoonacular.com/recipes/632819-312x231.jpg', 'imageType': 'jpg', 'nutrition': {'nutrients': [{'name': 'Calories', 'amount': 51.6565, 'unit': 'kcal'}]}}]}
    data = {'results': []}
    # data = {
    #         "status": "failure",
    #         "code": 402,
    #         "message": "Your daily points limit of 50 has been reached. Please upgrade your plan to continue using the API."
    #       }

    if 'results' not in data and "message" in data:
      print(data['message'])
      message = data['message']
      return render_template("no_results.html", message = message)
    
    min_results = min(3, len(data['results']))
    if min_results == 0:
      message = "No recipes found"
      return render_template("no_results.html", message = message)
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