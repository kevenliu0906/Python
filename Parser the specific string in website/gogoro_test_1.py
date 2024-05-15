# print the current python version
!python --version

import requests
import json

def grab():
  try:
    print('Hello Python Online Compiler - Colab')
    url = 'https://swapi.py4e.com/api/films/6'
    r = requests.get(url)

    data = json.loads(r.text)
    if data is not None:
      speciesarrs = data['species']

      speciesarrsSize = len(speciesarrs)
      resText = "count:{0}".format(speciesarrsSize)
      # print total count for named 'species' data in website
      print(resText)

      resText = "{0}".format(speciesarrs)
      # print all named 'species' data
      print(resText)

  except Exception as e:
      print(e)

if __name__ == "__main__":
    grab()