import json

my_list = [1, 2, 3, 4, 5]

# url = 'https://example.com/api'
data = {'my_list': json.dumps(my_list)}
# response = requests.post(url, data=data)
print(data)
