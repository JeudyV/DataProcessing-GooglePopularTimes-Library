# DataProcessing-GooglePopularTimes-Library

This project consists in the implement of the [populartime](https://github.com/m-wrzr/populartimes) library. URL:

Get a Google Maps API key https://developers.google.com/places/web-service/get-api-key
clone the repository, cd into the populartimes directory and run pip install .
Alternatively install directly from github using pip install --upgrade git+https://github.com/m-wrzr/populartimes
import populartimes and run with populartimes.get(...) or populartimes.get_id(...)
Note: The library is not available via PyPI, so you have to clone/download the repository and install it locally.

This demo uses the populartime library to obtain some information about a specific location, example of the data(place name, 
place address, coordinates, populartime, etc), this information is obtained using the Place Id that provides Google Place, this one identifies the location that the user has added in the search engine of the application.

## How to run the demo
- Clone or download the project in the folder of your preference
- Open console or windows system symbols  
- Position in the folder where I download the project, with the command **"cd"** example **"cd PopularTimesTest"**
- Run the file **“script.sh”**
- Open the navigation browser of your choice and add in the navigation bar `"localhost:8000/map/"`
- When leaving the application you should go to the terminal or cmd that was opened when the application was running,
and press **"Ctrl+c"** this action will close the server and release the port **‘8000’** 

### info_populartime(place_id)

Retrieves information for a given place id and adds populartimes, wait, time_spent and other data not accessible via Google Places. If founds a JSON without data fill the row with "None". If there is a place with just zeros in the populartimes data replace the output with "data" : "Closed"

- **place_id** str; unique google maps id; retrievable via populartimes.get() or https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder
Example call

- get_id("your-api-key", "ChIJSYuuSx9awokRyrrOFTGg0GY")
Response

- The response is formatted is equal to the .json described below.
- The information present for places is highly varying. Therefore popularity, current_popularity, rating, rating_n, time_wait, time_spent and phone are optional return parameters and only present if available.
time_wait and time_spent are in minutes
> **Note:** The time_wait and time_spent parameters were only added recently to Google Maps and are only present as a language specific string. The extracted values may therefore be incorrect and you might have to parse the raw string yourself, depending on your language settings.

**_example_**

## Unittest one

```python 

def test_info_populartime():
    try:
        temp = json.dumps(get_id("ChIJdbK33I7joI8RleAOLkLhykg"))
        tempDict = json.loads(temp)
        checkAssert = dict(id= 'ChIJdbK33I7joI8RleAOLkLhykg', name= 'La Pataconería', address= 'San José Province, San Pedro, Costa Rica', types= ['restaurant', 'point_of_interest', 'food', 'establishment'], coordinates= dict(lat= 9.9331525, lng= -84.0540713), rating= 4.4, rating_n= 369, international_phone_number= '+506 2253 3354', time_spent= [60, 90])
        assert tempDict==checkAssert
        print("Test Result: False")
        print("JSON: "+ str(tempDict))
    except:
        print("Test Result: True")
        print("JSON Obtained: " + str(checkAssert))
        print("JSON Expected: " + str(tempDict))

```

### Result

```
Test Result: True

```
```
JSON Obtained:{
   'id':'ChIJdbK33I7joI8RleAOLkLhykg',
   'name':'La Pataconería',
   'address':'San José Province, San Pedro, Costa Rica',
   'types':[
      'restaurant',
      'point_of_interest',
      'food',
      'establishment'
   ],
   'coordinates':{
      'lat':9.9331525,
      'lng':-84.0540713
   },
   'rating':4.4,
   'rating_n':369,
   'international_phone_number':'+506 2253 3354',
   'time_spent':[
      60,
      90
   ]
}
}

```
```
JSON Expected:{  
   'populartimes':'None',
   'time_wait':'None',
   'time_spent':[  
      60,
      90
   ]
}

```
# Unittest two

```python

def test_info_populartime():
    try:
        temp = json.dumps(info_populartime("ChIJSYuuSx9awokRyrrOFTGg0GY"))
        tempDict = json.loads(temp)
        checkAssert = dict({'id': 'ChIJSYuuSx9awokRyrrOFTGg0GY', 'name': 'Gran Morsi', 'address': '22 Warren St, New York, NY 10007, USA', 'types': ['restaurant', 'point_of_interest', 'food', 'establishment'], 'coordinates': {'lat': 40.7143138, 'lng': -74.0077763}, 'rating': 4.4, 'rating_n': 227, 'international_phone_number': '+1 212-577-2725', 'populartimes': [{'name': 'Monday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 14, 23, 22, 14, 10, 19, 36, 52, 53, 40, 20, 0]}, {'name': 'Tuesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 26, 34, 30, 20, 17, 32, 60, 81, 74, 45, 19, 0]}, {'name': 'Wednesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 36, 42, 33, 18, 14, 29, 56, 69, 53, 24, 7, 0]}, {'name': 'Thursday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 44, 48, 39, 29, 34, 55, 83, 100, 93, 68, 39, 0]}, {'name': 'Friday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 29, 33, 27, 19, 17, 28, 51, 72, 77, 60, 36, 0]}, {'name': 'Saturday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 55, 79, 97, 97, 78, 48, 0]}, {'name': 'Sunday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 22, 20, 14, 7, 3, 0]}], 'time_wait': [{'name': 'Monday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'name': 'Tuesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'name': 'Wednesday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'name': 'Thursday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'name': 'Friday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {'name': 'Saturday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 0, 0, 0]}, {'name': 'Sunday', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 0, 0, 0, 0, 0]}], 'time_spent': [90, 180]})
        assert tempDict==checkAssert
        print("Test Result: False")
        print("JSON: "+ str(tempDict))
    except:
        print("Test Result: True")
        print("JSON Obtained: " + str(checkAssert))
        print("JSON Expected: " + str(tempDict))

```
### Result

```
Test Result: True

```
```
JSON Obtained:{
  'id':'ChIJSYuuSx9awokRyrrOFTGg0GY',
   'name':'Gran Morsi',
   'address':'22 Warren St, New York, NY 10007, USA',
   'types':[
      'restaurant',
      'point_of_interest',
      'food','establishment'
   ],
   'coordinates':{
      'lat':40.7143138,
      'lng':-74.0077763
   },
   'rating':4.4,
   'rating_n':227,
   'international_phone_number':'+1 212-577-2725',
   'populartimes':[
      {
        'name':'Monday',
         'data':[0,0,0,0,0,0,0,0,0,0,0,5,14,23,22,14,10,19,36,52,53,40,20,0]
      },
      {
         'name':'Tuesday',
         'data':[0,0,0,0,0,0,0,0,0,0,0,14,26,34,30,20,17,32,60,81,74,45,19,0]
      },
      {
         'name':'Wednesday',
         'data':[0,0,0,0,0,0,0,0,0,0,0,20,36,42,33,18,14,29,56,69,53,24,7,0]
      },
      {
         'name':'Thursday',
         'data':[0,0,0,0,0,0,0,0,0,0,0,29,44,48,39,29,34,55,83,100,93,68,39,0]
      },
      {
         'name':'Friday',
         'data':[0,0,0,0,0,0,0,0,0,0,0,19,29,33,27,19,17,28,51,72,77,60,36,0]
      },
      {
         'name':'Saturday',
         'data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55,79,97,97,78,48,0]
      },
      {
         'name':'Sunday',
         'data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,22,20,14,7,3,0]
      }
     ],
   'time_wait':[
      {
         'name':'Monday',
         'data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       },
       {
         'name':'Tuesday',
         'data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       },
       {
         'name':'Wednesday',
         'data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       },
       {
         'name':'Thursday',
         'data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        },
        {
          'name':'Friday',
          'data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        },
        {
          'name':'Saturday',
          'data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,15,0,0,0]
        },
        {
          'name':'Sunday',
           'data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,15,0,0,0,0,0]
        }
        ],
    'time_spent':[90,180]}

```

```
JSON Expected:{
  'populartimes':[
    {
      'name':'Monday',
      'data':[0,0,0,0,0,0,0,0,0,0,0,5,14,23,22,14,10,19,36,52,53,40,20,0]
    },
    {
      'name':'Tuesday',
      'data':[0,0,0,0,0,0,0,0,0,0,0,14,26,34,30,20,17,32,60,81,74,45,19,0]
    },
    {
      'name':'Wednesday',
      'data':[0,0,0,0,0,0,0,0,0,0,0,20,36,42,33,18,14,29,56,69,53,24,7,0]
    },
    {
      'name':'Thursday',
      'data':[0,0,0,0,0,0,0,0,0,0,0,29,44,48,39,29,34,55,83,100,93,68,39,0]
    },
    {
      'name':'Friday',
      'data':[0,0,0,0,0,0,0,0,0,0,0,19,29,33,27,19,17,28,51,72,77,60,36,0]
    },
    {
      'name':'Saturday',
      'data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55,79,97,97,78,48,0]
    },
    {
      'name':'Sunday',
      'data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,22,20,14,7,3,0]
    }
    ],
  'time_wait':[
    {
      'name':'Monday',
      'data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    },
    {
      'name':'Tuesday','data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    },
    {
      'name':'Wednesday',
      'data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    },
    {
      'name':'Thursday',
      'data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    },
    {
      'name':'Friday','data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    },
    {
      'name':'Saturday','data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,15,0,0,0]
      },
      {
        'name':'Sunday','data':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,15,0,0,0,0,0]
      }
      ],
    'time_spent':[90,180]}
```
### How to user the map

#### 1. Run the Demo
![Webp net-gifmaker](https://user-images.githubusercontent.com/46583912/55092869-f9472e00-5078-11e9-9f4b-5e76819e7045.gif)

#### 2. User The demo
![Webp net-gifmaker (1)](https://user-images.githubusercontent.com/46583912/55095765-52fe2700-507e-11e9-9bc2-a3c01776f545.gif)

