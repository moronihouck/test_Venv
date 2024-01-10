import requests

# JSONPlaceholder的一个示例URL，用于获取假的用户数据
url = 'https://jsonplaceholder.typicode.com/users'

# 发送GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 解析JSON响应
    users = response.json()

    # 打印每个用户的信息
    for user in users:
        print(f'Name: {user["name"]}, Email: {user["email"]}')
else:
    print('Failed to retrieve d')
    