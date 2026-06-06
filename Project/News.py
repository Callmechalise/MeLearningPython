import requests
api="c70df7dd35f74a4bba5bd41854b6ac6f"
url="https://newsapi.org/v2/top-headlines?country=np&apiKey=c70df7dd35f74a4bba5bd41854b6ac6f"
parameters={
    "country":"np",
    "category": "technology",
    "apikey":api
}
response=requests.get(url,params=parameters)


