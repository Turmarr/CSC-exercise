# CSC-exercise

The app takes the username of the wanted user and returns after authentication the starred public repositories of the user.

## Track and content

The exercise was done for the Backend track with a Dockerfile added. The JSON file that is returned has the following fields:

amount : the amount of returned repositories
repositories : a list containing the information of the repositories

The single repositories have the following fields:

name : name of the repository
url : url of the repository
description : description of the repository
topics : a list of all the topics of the repository

Additionally if the repostiory has a license the following field is added

license : the information of the license

## Setup

### Command line

To setup the application on Windows run the setup_win.bat file. It will install all of the needed dependencies and create the .env file. After that add the Oauth application information to the .env file. The app was developed in Windows and it does not have a ready-made setup file for Linux. Below are the four libraries that are needed to run the app.

### Docker

For Docker create the image using the command "docker build -t <NAME FOR APP> .". After that create a .env file, add the variables to it after the model of the env.example file and fill in the required Oauth information.

### Dependencies

httpx
fastapi
"uvicorn[standard]"
pydantic-settings

## Runing

### Command line

To run the application execute the run.bat file. The application can be found under the IP address http://127.0.0.1:8000 or http://localhost:8000

### Docker

To run the application run the command "docker run --env-file .env -p 8000:8000 csc-exercise". The application can be found under the address http://localhost:8000 the IP address can be found using ipconfig and taking the localhost address.

## Features

There are two addresses that are supposed to be called by the user: /git/noauth/{Username} and /git/auth/{Username}. The noauth address utilizes the unauthorized access based on a Username from git and returns the starred repositories in its raw format. The auth version is the actual task that redirects the user over to the Oauth app and then returns the wanted information.

## Problems in testing

While I tested the app without Docker a lot I couldn't get the Oauth app to work with the Docker image. What it eventually seemed to boil down to was that git did not accept the URL for the docker app. 