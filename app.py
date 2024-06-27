import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import validators

# Creating an object of ToastNotifier Class
n = ToastNotifier()


# Function to get data from url
def getdata(url):
    # Validate the URL before making the request
    if not validators.url(url):
        print("Invalid URL. Please provide a valid URL.")
        return None

    # Improve Interaction with Servers
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Attempt to fetch the URL content up to three times.
    retries = 3

    # Allows for connection pooling
    session = requests.Session()

    for _ in range(retries):
        try:
            r = session.get(url, headers=headers, timeout=10)
            r.raise_for_status()
            return r.text
        except requests.exceptions.RequestException as e:
            print(f"Request error occurred: {e}")
    print("Failed to retrieve data after multiple retries")
    return None


# Pass URL into getdata function and convert data into HTML
htmldata = getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/")

soup = BeautifulSoup(htmldata, 'html.parser')

print(soup.prettify())

"""
1. bs4: A Python library for pulling data out of HTML and XML files
2. win10toast: Helps in creating desktop notifications
3. requests: Allows you to send HTTP/1.1 requests extremely easily
"""
