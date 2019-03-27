# DataProcessing-GooglePopularTimes-Library

This project consists in the implement of the [populartime](https://github.com/m-wrzr/populartimes) library, 

This demo uses the populartime library to obtain some information about a specific location, example of the data(place name, 
place address, coordinates, populartime, etc), this information is obtained by means of a Place Id that provides Google Place, 
Place id identifies the location that the user has added in the search engine of the application

## How to run the demo
- Clone or download the project in the folder of your preference
- Open console or windows system symbols  
- Position in the folder where I download the project, with the command **"cd"** example **"cd PopularTimesTest"**
- Run the file **“script.sh”**
- Open the navigation browser of your choice and add in the navigation bar `"localhost:8000/map/"`
- When leaving the application you should go to the terminal or cmd that was opened when the application was running,
and press **"Ctrl c"** this action will close the server and release the port **‘8000’** 

### render_map(request)
Ubicado en la carpeta PopularTimesTest en el archivo views.py, la función se encarga de abrir el map_template.html, que renderiza un mapa de google map en una página web

### get_id(...)
Ubicado en la carpeta PopularTimesTest en el archivo views.py, la función usa la librería populartime para poder obtener la información de un lugar en específico, determinado por el parámetro. Este debe de ser un place_id proveniente de la lista de IDs de Google.
 



