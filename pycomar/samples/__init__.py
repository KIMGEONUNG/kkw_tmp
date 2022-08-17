from PIL import Image
import requests
from io import BytesIO


def get_img(index: int) -> Image.Image:
  if index == 1:
    url = "https://raw.githubusercontent.com/KIMGEONUNG/comars-core/master/resource/sample01.jpg"
  else:
    raise
  response = requests.get(url)
  img = Image.open(BytesIO(response.content))
  return img


if __name__ == '__main__':
  img = get_img(1)
  img.show()
