import requests

api_key = "bafe0573b42b4cc096ebdd7dfb5dd261"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-07-15&sortBy=publishedAt&apiKey"
       "=bafe0573b42b4cc096ebdd7dfb5dd261")

request = requests.get(url)
content = request.text

