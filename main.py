import requests
from send_email import send_email

topic = "tesla"

api_key = "bafe0573b42b4cc096ebdd7dfb5dd261"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&from=2024-07-15&" \
      "sortBy=publishedAt&" \
      "apiKey=bafe0573b42b4cc096ebdd7dfb5dd261&" \
      "language=en"

request = requests.get(url)

content = request.json()

body =""
for article in content["articles"][:20]:
    body = ("Subject: Today's news" + "\n"
            + (body + article["title"] + "\n"
            + str(article["description"]) + "\n"
            + article["url"] + 2*"\n"))

body = body.encode("utf-8")
send_email(message=body)