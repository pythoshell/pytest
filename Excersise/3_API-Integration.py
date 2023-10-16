
"""
API testing is a critical aspect of software testing to ensure that an application's APIs work correctly.
Python provides various libraries and tools for API testing.
Here's a basic example using the requests library to perform common API testing operations:

We import the requests library to send HTTP requests.

We define the API endpoint (api_url) you want to test. Replace it with the URL of the API you want to test.

We send a GET request to retrieve data from the API and check the response status code. If the status code is 200,
we assume the request was successful and parse the JSON response.

We send a POST request to create data on the API and again check the response status code. If the status code is 201,
we assume the request was successful and parse the JSON response.

You can customize this code to match the specifics of the API you are testing, including endpoints, request parameters,
and expected response data.

It's important to note that API testing often involves more complex scenarios, such as handling authentication, headers,
testing different HTTP methods (e.g., PUT, DELETE), and conducting extensive test cases. To perform more comprehensive API testing, you might consider using dedicated API testing tools or libraries like unittest, pytest, or Postman.



"""


import requests

# Define the API endpoint
api_url = "https://jsonplaceholder.typicode.com/posts/1"  # Replace with your API URL

# Send a GET request to retrieve data
response = requests.get(api_url)

# Check the response status code
if response.status_code == 200:
    print("API request was successful!")
    data = response.json()  # Parse the JSON response
    print("Response Data:")
    print(data)
else:
    print(f"API request failed with status code {response.status_code}")

# Send a POST request to create data
new_post = {
    "title": "New Post",
    "body": "This is the body of the new post",
    "userId": 1
}
post_response = requests.post(api_url, json=new_post)

# Check the response status code
if post_response.status_code == 201:
    print("POST request was successful!")
    new_data = post_response.json()
    print("Created Post Data:")
    print(new_data)
else:
    print(f"POST request failed with status code {post_response.status_code}")
