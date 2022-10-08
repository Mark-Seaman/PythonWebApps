from requests import get

response = get('https://shrinking-world.com')
print('Google', response)
print(response.text)
