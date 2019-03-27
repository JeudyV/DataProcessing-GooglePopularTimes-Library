# DataProcessing-GooglePopularTimes-Library

This project consists in the implement of the [populartime](https://github.com/m-wrzr/populartimes) library. URL:

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

### get_id(...)
Located at `views.py` inside PopularTimesTest folder. Implements popular id method called **get_id**, using as arguments the *API_KEY* and the *Place_ID*, the last one is based from Google Places ID
 



