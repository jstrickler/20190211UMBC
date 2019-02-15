
import requests

response = requests.get('https://www.nasa.gov')

source = response.content
print(source.decode())

# print(requests.get('https://www.nasa.gov').content.decode())