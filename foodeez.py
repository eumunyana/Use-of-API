from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)

GOOGLE_API_KEY = AIzaSyC5HW5kTuyvRwKuji1IsT3z8BiYnVjQlPc

@app.route('/')
def index():
    return render_template('foodeez.html')

@app.route('/search', methods=['GET'])
def search_restaurants():
    location = request.args.get('location')
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=chinese+restaurant+in+{location}&key=AIzaSyC5HW5kTuyvRwKuji1IsT3z8BiYnVjQlPc"
    
    response = requests.get(url)
    data = response.json()

    restaurants = []
    for place in data.get('results', []):
        restaurants.append({
            'name': place['name'],
            'address': place['formatted_address'],
            'rating': place.get('rating', 'N/A')
        })

    return jsonify(restaurants)

if __name__ == '__main__':
   app.run(debug=True)
   print(response.text)
