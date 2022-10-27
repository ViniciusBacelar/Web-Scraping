import requests as rq
import os
from bs4 import BeautifulSoup as bs
import pathlib


def save_image(folder: str, name: str, url: str):
    # Get the data from the url
    image_source = rq.get(url)

    # If there's a suffix, we will grab that
    suffix = pathlib.Path(url).suffix

    # Check if the suffix is one of the following
    if suffix not in ['.jpg', '.jpeg', '.png', '.gif']:
        # Default to .png
        output = name + '.png'
    else:
        output = name + suffix

    # Check first if folder exists, else create a new one
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Create our output in the specified folder (wb = write bytes)
    with open(f'{folder}{output}', 'wb') as file:
        file.write(image_source.content)
        print(f'Successfully downloaded: {output}')


if __name__ == '__main__':
    username = input("Type your username: ")
    url = 'https://github.com/'+username
    r = rq.get(url)
    soup = bs(r.content, 'html.parser')
    profile_image = str(soup.find('img', {'alt': 'Avatar'}))
    profile_image_url = profile_image.split("src")[1].split("style")[0][2:-1]
    output_name = input('Enter output name: ')
    save_image('folder/', output_name, profile_image_url)
