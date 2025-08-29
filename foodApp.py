from flask import Flask, redirect, url_for, render_template, request
import requests, json

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
  if request.method =="POST":
    ingrediant = request.form["food"]
    write_json(ingrediant)
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

@app.route('/searches')
def display_searches():
    with open("searches.json", 'r+') as file:
        # Load existing data into a dictionary
        file_data = json.load(file)
        
        # Append new data to the 'searches' list in 
        data = file_data["searches"]
    return render_template("past_searches.html", data = data)
  

@app.route('/testing')
def get_data2():
    search = "toast"
    write_json(search)
    return render_template("no_results.html", message = "Just testing Json write up")

# Function to append new data to JSON file
def write_json(new_data, filename='searches.json'):
    with open(filename, 'r+') as file:
        # Load existing data into a dictionary
        file_data = json.load(file)
        
        # Append new data to the 'searches' list in 
        file_data["searches"].append(new_data)
        
        # Move the cursor to the beginning of the file
        file.seek(0)
        
        # Write the updated data back to the file
        json.dump(file_data, file, indent=4)


if __name__ == "__main__":
  app.run(debug=True)