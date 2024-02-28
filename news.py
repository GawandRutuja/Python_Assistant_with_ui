import requests
#ss is the secret file for the News AOI Key
from ss import *

# Define the base URL for the News API 
base_url="https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey="

# Combine the base URL with the API key from the 'ss' module
api_address=base_url+key

# Make a request to the News API and parse the response as JSON
json_data=requests.get(api_address).json()

# Create an empty list to store news articles
ar=[]

# Define a function 'news' to extract and format news articles
def news():
    for i in range(3):
        ar.append("Number"+str(i+1) + ": " +json_data["articles"][i]["title"]+ ".")

    return ar

# Call the 'news' function and store the result in 'ar'
ar=news()

# Print the list of news articles
#print(ar)
