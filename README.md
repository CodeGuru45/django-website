# Spotify Sharing Website

A site written in Django which allows users to share and rate Spotify songs and playlists. Registered/logged in users are able to create posts with their embedded music and a five-star rating system. All posts are displayed on the homepage, and user specific posts can be filtered by clicking on a user's username. Logged in users are also able to delete their posts.  

## Motivation

This site was developed as a means for providing a collective space where users can share and rate each others' Spotify music. Ideally this functionality would be present in the Spotify app itself, however it is not. One of the main goals for this project was also to gain a better understanding of Django fundamentals and the backend layer. 

## Screenshot

![](django_website_scrnsht.png)
Link: https://spotifyshareapp.herokuapp.com/

## Usage

After cloning the repository run pip install -r requirements.txt to install all the project requirements. I recommend doing this in a virtual environment. If running the site locally note that the username and password environemnt variables (in settings.py) must be set accordingly
