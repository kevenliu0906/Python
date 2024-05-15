import requests
import json

def grab():
  print('Hello Python, count speed over 1000')
  try:
    url = 'https://swapi.py4e.com/api/vehicles'
    r = requests.get(url)

    data = json.loads(r.text)
    if data is not None:
      numResults = int(data['count'])
      # gather all results field information in data
      resultsarrs = data['results']

      for resultsarr in resultsarrs:
        # judge uf max_atmosphering_speed field in resultsarr is over 1000
        if int(resultsarr['max_atmosphering_speed']) > int(1000):
          resText = "WARNING!!! {0} OVER SPEED, speed is {1}".format(resultsarr['name'], resultsarr['max_atmosphering_speed'])
          print(resText)

  except Exception as e:
    print(e)

if __name__ == "__main__":
  grab()