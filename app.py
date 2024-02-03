import os
from flask import Flask, render_template, request
import requests,jsonify,json
from geopy.geocoders import Nominatim

# Set the current working directory to the directory containing this script
os.chdir(os.path.dirname(__file__))

app = Flask(__name__, template_folder="templates")

# function to get nutrition data

def get_nutritionix_data(query, min_calories=None, max_calories=None):
    base_url = "https://trackapi.nutritionix.com/v2/search/instant/?"
    api_key = "5bd2595b54d7e4e094bdb30ccba81e0d"  # Replace with your actual API key

    headers = {
        "x-app-id": '91623d55',
        "x-app-key": api_key,
    }

    params = {
        "query": query,
    }



    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        print("API Response:")

        for i in range(len(data['branded'])):
            # Your code here, referencing data['branded'][i]
            if data['branded'][i]["nf_calories"]  >= min_calories and data['branded'][i]["nf_calories"]  <= max_calories:
                data['branded'][i]["status"] = "Perfect Calorie Match"

            elif data['branded'][i]["nf_calories"]  < min_calories :
                data['branded'][i]["status"] = "Low Calories"
            
            elif data['branded'][i]["nf_calories"]  > max_calories :
                data['branded'][i]["status"] = "High Calories"
            else:
                data["status"] = "Calorie Range Not Provided"





        return data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")



# function to get location data
        
def get_location_data(latitude, longitude, radius, query):

    url = "https://map-places.p.rapidapi.com/nearbysearch/json"
    
    # Prepare the query string
    querystring = {
        "location": f"{latitude},{longitude}",
        "radius": radius,
        "keyword": query,
        "type": "restaurant"
    }
    # API keys for google map API
    headers = {
        "X-RapidAPI-Key": "b7da94db26msh35d4b1ae1800e20p14f60fjsn3f519b7f01ab",
        "X-RapidAPI-Host": "map-places.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    # data = json.dumps(response.json(), indent=4)
    data = response.json()

    for i in range(len(data['results'])):
        
        place_id = data['results'][i]['place_id']

        url = "https://map-places.p.rapidapi.com/details/json"

        querystring = {"place_id": place_id}

        headers = {
            "X-RapidAPI-Key": "b7da94db26msh35d4b1ae1800e20p14f60fjsn3f519b7f01ab",
            "X-RapidAPI-Host": "map-places.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        place_detail = response.json()

        data['results'][i]['place_detail'] = place_detail['result']




    # print(data)
    return data


# route

@app.route("/", methods=["GET", "POST"])
def index():
    result1 = None
    result2 = None

    if request.method == "POST":
        query = request.form.get("query")
        min_calories = request.form.get("min_calories")
        max_calories = request.form.get("max_calories")
        
        # max_value = x if x > y else y

        radius = int(request.form.get("radius")) if request.form.get("radius") else 2
        lat = float(request.form.get("lat")) if request.form.get("lat") else 43.6476
        long = float(request.form.get("long")) if request.form.get("long") else 79.3809

        print("lat ===>", lat)
        print("long ===>", long)
        print("r ===>", radius)

        # Check if min and max calories are provided and convert to integers
        if min_calories:
            min_calories = int(min_calories)
        if max_calories:
            max_calories = int(max_calories)

        result1 = get_nutritionix_data(query, min_calories, max_calories)

        result2 = get_location_data(lat, long, radius, query)

    return render_template("index.html", result1=result1, result2=result2)

@app.route("/nlp", methods=["GET", "POST"])
def nlp():
    result = None

    if request.method == "POST":
        query = request.form.get("query")
        
        # Retrieve form data for nf_calories
        min_calories = int(request.form.get("min_calories", 0))
        max_calories = int(request.form.get("max_calories", 0))

        # Retrieve form data for nf_cholesterol
        min_cholesterol = int(request.form.get("min_cholesterol", 0))
        max_cholesterol = int(request.form.get("max_cholesterol", 0))

        # Retrieve form data for nf_dietary_fiber
        min_dietary_fiber = int(request.form.get("min_dietary_fiber", 0))
        max_dietary_fiber = int(request.form.get("max_dietary_fiber", 0))

        # Retrieve form data for nf_protein
        min_protein = int(request.form.get("min_protein", 0))
        max_protein = int(request.form.get("max_protein", 0))

        # Retrieve form data for nf_saturated_fat
        min_saturated_fat = int(request.form.get("min_saturated_fat", 0))
        max_saturated_fat = int(request.form.get("max_saturated_fat", 0))

        # Retrieve form data for nf_saturated_fat
        min_fat = int(request.form.get("min_fat", 0))
        max_fat = int(request.form.get("max_fat", 0))

        # Retrieve form data for nf_sugars
        min_sugars = int(request.form.get("min_sugars", 0))
        max_sugars = int(request.form.get("max_sugars", 0))

        # Retrieve form data for nf_total_carbohydrate
        min_total_carbohydrate = int(request.form.get("min_total_carbohydrate", 0))
        max_total_carbohydrate = int(request.form.get("max_total_carbohydrate", 0))

        # max_value = x if x > y else y

        try:
            url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
            headers = {
                'Content-Type': 'application/json',
                'x-app-id': '91623d55',  
                'x-app-key': '5bd2595b54d7e4e094bdb30ccba81e0d' 
            }

            data = {
                "query": query
            }

            response = requests.post(url, headers=headers, json=data)
            # data = json.dumps(response.json(), indent=4)
            data = response.json()
            

            print(data)

            
            for i in range(len(data['foods'])):
                data['foods'][i]["status"] = []
                

                if data['foods'][i]["nf_calories"]  >= min_calories and data['foods'][i]["nf_calories"]  <= max_calories:
                    data['foods'][i]["status"].append("Perfect Calorie Match")

                elif data['foods'][i]["nf_calories"]  < min_calories :
                    data['foods'][i]["status"].append("Low Calories")
                
                elif data['foods'][i]["nf_calories"]  > max_calories :
                    data['foods'][i]["status"].append("High Calories")

                
                if data['foods'][i]["nf_cholesterol"]  >= min_cholesterol and data['foods'][i]["nf_cholesterol"]  <= max_cholesterol:
                    data['foods'][i]["status"].append("Perfect Cholestrol Match")

                elif data['foods'][i]["nf_cholesterol"]  < min_cholesterol :
                    data['foods'][i]["status"].append("Low Cholestrol")
                
                elif data['foods'][i]["nf_cholesterol"]  > max_cholesterol :
                    data['foods'][i]["status"].append("High Cholestrol")


                if data['foods'][i]["nf_dietary_fiber"]  >= min_dietary_fiber and data['foods'][i]["nf_dietary_fiber"]  <= max_dietary_fiber:
                    data['foods'][i]["status"].append("Perfect Cholestrol Match")

                elif data['foods'][i]["nf_dietary_fiber"]  < min_dietary_fiber :
                    data['foods'][i]["status"].append("Low Cholestrol")
                
                elif data['foods'][i]["nf_dietary_fiber"]  > max_dietary_fiber :
                    data['foods'][i]["status"].append("High Cholestrol")


                if data['foods'][i]["nf_protein"]  >= min_protein and data['foods'][i]["nf_protein"]  <= max_protein:
                    data['foods'][i]["status"].append("Perfect Cholestrol Match")

                elif data['foods'][i]["nf_protein"]  < min_protein :
                    data['foods'][i]["status"].append("Low Cholestrol")
                
                elif data['foods'][i]["nf_protein"]  > max_protein :
                    data['foods'][i]["status"].append("High Cholestrol")


                if data['foods'][i]["nf_saturated_fat"]  >= min_saturated_fat and data['foods'][i]["nf_saturated_fat"]  <= max_saturated_fat:
                    data['foods'][i]["status"].append("Perfect saturated fat Match")

                elif data['foods'][i]["nf_saturated_fat"]  < min_saturated_fat :
                    data['foods'][i]["status"].append("Low saturated fat")
                
                elif data['foods'][i]["nf_saturated_fat"]  > max_saturated_fat :
                    data['foods'][i]["status"].append("High saturated fat")


                if data['foods'][i]["nf_total_fat"]  >= min_fat and data['foods'][i]["nf_total_fat"]  <= max_fat:
                    data['foods'][i]["status"].append("Perfect Fat match")

                elif data['foods'][i]["nf_total_fat"]  < min_fat :
                    data['foods'][i]["status"].append("Low Fat")
                
                elif data['foods'][i]["nf_total_fat"]  > max_fat :
                    data['foods'][i]["status"].append("High Fat")


                if data['foods'][i]["nf_sugars"]  >= min_sugars and data['foods'][i]["nf_sugars"]  <= max_sugars:
                    data['foods'][i]["status"].append("Perfect sugars Match")

                elif data['foods'][i]["nf_sugars"]  < min_sugars :
                    data['foods'][i]["status"].append("Low sugars")
                
                elif data['foods'][i]["nf_sugars"]  > max_sugars :
                    data['foods'][i]["status"].append("High sugars")


                if data['foods'][i]["nf_total_carbohydrate"]  >= min_total_carbohydrate and data['foods'][i]["nf_total_carbohydrate"]  <= max_total_carbohydrate:
                    data['foods'][i]["status"].append("Perfect carbohydrate Match")

                elif data['foods'][i]["nf_total_carbohydrate"]  < min_total_carbohydrate :
                    data['foods'][i]["status"].append("Low carbohydrate")
                
                elif data['foods'][i]["nf_total_carbohydrate"]  > max_total_carbohydrate :
                    data['foods'][i]["status"].append("High carbohydrate")

            result = data





            #     # result = response.json()
            #     # print("Response:", result)
            # else:
            #     print("Error:", response.status_code, response.text)

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return render_template("nlp.html", result=result)


# @app.route("/getloc", methods=["GET", "POST"])
# def get_current_location():
#         # Initialize the geolocator
#         geolocator = Nominatim(user_agent="my_geocoder")

#         # Get the user's current location using their IP address
#         location = geolocator.geocode('')
        
#         # Print the latitude and longitude
#         if location:
#             print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
#         else:
#             print("Unable to determine current location.")

#         return 'hello'

# @app.route('/nearby_search', methods=['GET'])
# def nearby_search():
#     url = "https://map-places.p.rapidapi.com/nearbysearch/json"
    
#     # Extract location, radius, keyword, and type from the query parameters
#     # location = request.args.get('location')
#     # radius = request.args.get('radius', '1500')
#     # keyword = request.args.get('keyword', '')
#     # place_type = request.args.get('type', '')

#     location = "-33.8670522,151.1957362"
#     radius = "1000"
#     keyword = "biryani"
#     place_type = "restaurant"
    
#     # Prepare the query string
#     querystring = {
#         "location": location,
#         "radius": radius,
#         "keyword": keyword,
#         "type": place_type
#     }
    
#     headers = {
#         "X-RapidAPI-Key": "82c7fabb61msh3fb2dea601a5424p13f094jsn2ef2c1b4a8dd",
#         "X-RapidAPI-Host": "map-places.p.rapidapi.com"
#     }
    
#     response = requests.get(url, headers=headers, params=querystring)
#     data = json.dumps(response.json(), indent=4)
#     print(data)

#     return "hello"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
