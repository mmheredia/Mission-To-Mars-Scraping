from flask import Flask, render_template, redirect
from pymongo import MongoClient
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connectio
client = MongoClient("mongodb://localhost:27017")

data = client.scrape_mars.data

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = data.find_one() # Returns a dictionary

    # Return template and data
    return render_template("index.html", mars=mars_data)
   

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape_info():

    # Run the scrape function and save the results to a variable
    item = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    data.insert_one(item)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)