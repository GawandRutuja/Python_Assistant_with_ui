import requests

# Define the URL to fetch a random joke from the official joke API
url="https://official-joke-api.appspot.com/random_joke"

# Make a request to the API and parse the response as JSON
json_data=requests.get(url).json()

# Create an empty list to store the setup and punchline of the joke
arr=["",""]

# Assign the setup and punchline from the API response to the list 'arr'
arr[0]=json_data["setup"]
arr[1]=json_data["punchline"]

# Define a function 'joke' to return the list containing the setup and punchline
def joke():
    return arr

# Call the 'joke' function and print the result
# print(joke())
