from flask import Flask, jsonify, request, render_template, Response
import json
import urllib, requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/reply', methods=['POST'])
def reply():
    data = json.loads(request.data)
    answer = "Yes, it is %s!\n" % data["keyword"]
    result = {
      "Content-Type": "application/json",
      "Answer":{"Text": answer}
    }
    # return answer
    return jsonify(result)

@app.route('/reply/<url>', methods=['GET'])
def get_cook(url):
    load_url = "https://cookpad.com/recipe/" + url
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")

    food_list = []
    new_list = []
    for element in soup.find_all(class_="ingredient_name"):
        food_list.append(element.text)
    for x in food_list:
        new_list.append(x.encode('UTF8'))
    return jsonify(result = food_list)

@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=False)