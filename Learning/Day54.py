import asyncio

import requests
async def funcdownload():
    url = "https://images.pexels.com/photos/1624496/pexels-photo-1624496.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    response = requests.get(url)
    if response.status_code == 200:
        with open("ram.ico", "wb") as file:
            file.write(response.content)
        print("File downloaded successfully!")
    else:
        print("Failed to download the file.")
async def func2():
    url = "https://images.pexels.com/photos/8488611/pexels-photo-8488611.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
    response = requests.get(url)
    if response.status_code == 200:
        with open("ram2.ico", "wb") as file:
            file.write(response.content)
        print("File downloaded successfully!")
    else:
        print("Failed to download the file.")

async def main():#parallel run garaidinxa so fast download
    l=asyncio.gather(
        funcdownload(),
        func2()
    )