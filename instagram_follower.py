# -*- coding: utf-8 -*-
"""Instagram_follower.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KMN2hH2Alu96f6s8QZFhhS8LogqqUbH0

**Function: get_user_info**
```python
def get_user_info(nick):
    r = requests.get(f"https://www.instagram.com/{nick}/")
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    description_tag = soup.find("meta", attrs={"property": "og:description"})
    name_tag = soup.find("meta", attrs={"property": "og:title"})
    content = description_tag["content"]
    followers, following, posts = map(str.strip, content.split(","))
    name = name_tag["content"].split("•")[0].strip()
    return name, followers, following, posts
```
This function takes a Instagram username as input and fetches the corresponding Instagram profile page. It then uses BeautifulSoup to parse the HTML content of the page.

It finds two meta tags in the HTML - one with the attribute "property" having the value "og:description" and the other with the value "og:title". The "og:description" tag contains the description of the user profile which includes followers, following and posts count. The "og:title" tag contains the name of the user.

The content of the "og:description" tag is split into followers, following, and posts. The content of the "og:title" tag is split to get the name of the user. These values are returned by the function.

**Function: main**
```python
def main():
    nick = input("Enter the Instagram username here: ")
    try:
        name, followers, following, posts = get_user_info(nick)
    except Exception as e:
        print(f"Couldn't retrieve information for {nick}: {e}")
        return
    print(f'''
    Name: {name}
    Followers: {followers}
    Following: {following}
    Posts: {posts}
    ''')
```
This function prompts the user to input an Instagram username. It then calls the `get_user_info` function with this username to get the user's details. If there is any error (like the user doesn't exist or the profile is private), it catches the exception and prints an error message.

If there are no errors, it prints the user's name, follower count, following count, and post count in a nicely formatted way.
"""

import requests
from bs4 import BeautifulSoup

def get_user_info(nick):
    # Make a request to the website
    r = requests.get(f"https://www.instagram.com/{nick}/")
    r.raise_for_status()

    # Parse the page
    soup = BeautifulSoup(r.text, "html.parser")

    # Find the relevant parts of the page
    description_tag = soup.find("meta", attrs={"property": "og:description"})
    name_tag = soup.find("meta", attrs={"property": "og:title"})

    # Extract the information
    content = description_tag["content"]
    followers, following, posts = map(str.strip, content.split(","))
    name = name_tag["content"].split("•")[0].strip()

    return name, followers, following, posts

def main():
    nick = input("Enter the Instagram username here: ")

    try:
        name, followers, following, posts = get_user_info(nick)
    except Exception as e:
        print(f"Couldn't retrieve information for {nick}: {e}")
        return

    # Print the information
    print(f"""
    Name: {name}
    Followers: {followers}
    Following: {following}
    Posts: {posts}
    """)

main()