"""
Now, let's scrape data from a sample webpage.
Suppose we want to scrape the titles of articles from a news website.
Here's an example using Python:


pip install requests
pip install beautifulsoup4

In this example:

We import the requests library to make an HTTP GET request to the webpage and BeautifulSoup for parsing the HTML content.
We specify the URL of the webpage you want to scrape.
We send an HTTP GET request to the URL using requests.get(url) and check if the request was successful (status code 200).
If the request is successful, we parse the HTML content using BeautifulSoup.
We find and extract the data we're interested in. In this example, we assume that article titles are enclosed in <h2> tags.
We print the extracted article titles.
Keep in mind that web scraping may have legal and ethical considerations,
so always make sure you have the right to scrape the data, and consider the website's terms of service and robots.txt file.
Additionally, websites can change their structure, so the code might need adjustments if the website structure changes.

"""

import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://example.com/news'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract specific data from the page
    article_titles = []

    # Assuming article titles are in <h2> tags
    for title in soup.find_all('h2'):
        article_titles.append(title.text)

    # Print the extracted article titles
    for index, title in enumerate(article_titles, start=1):
        print(f"{index}. {title}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
