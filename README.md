# IMDB like REST API

## Prelim works

### Abstract

###### IMDB like API, made using MySQL and Flask

###### copy and paste the below commands in command prompt

```cmd
git clone https://github.com/AkashSCIENTIST/imdb_rest_api.git
cd imdb_rest_api
python rest_server.py
```

## Rest Endpoints

#### GET requests

| End Point | Description |
| --------- | ----------- |
| ```/master``` | Displays the Movies as well as Actors |
| ```/movies``` | Displays all Movies |
| ```/movies/:id``` | Displays the Movie with movie ID |
| ```/actors``` | Displays all the Actors |
| ```/actors/:id``` | Displays the Actor with actor ID |
| ```/movies_by_actor/:actor_id``` | Displays all the Movies with actor ID |
| ```/actors_by_movie/:movie_id``` | Displays all the Actors with movie ID |

#### POST requests

| End Point | Description |
| --- | --- |
| ```/insert_movie``` | accepts form values ```id```, ```name```, ```year```|
| ```/insert_actor``` | accepts form values ```id```, ```name```, ```age```, ```country```|
| ```/insert_movie_actor``` | accepts form values ```movie_id```, ```actor_id```|
