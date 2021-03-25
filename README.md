# docker-basic-django
It contains base image of python and a simple "Hello World" django project in it.

## Objective-
* Creating a django project using docker
* Creating docker image on dockerhub, it can be usedby anyone now
* Creating github repository for this django-docker project

## Links and references-
* Why Docker- https://www.docker.com/why-docker
* Documentation- https://docs.docker.com/
* Docker Hub- https://hub.docker.com/
* Docker Important commands- https://docs.docker.com/engine/reference/commandline/docker/
* Quick Project- https://www.geeksforgeeks.org/dockerizing-a-simple-django-app/

### Reference to Install Docker in Ubuntu 18.4-
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04

### Installing Django-
pip3 install django
### Creating project-
django-admin startproject basicdjango
### Creating App-
cd basicdjango
django-admin startapp myapp

### Editing ursl.py-
sudo su
nano basicdjango/urls.py
### Edit - 
path(‘’, include(‘myapp.urls’)),

### Creating urls.py for app-
touch myapp/urls.py
nano myapp/urls.py
### Edit-
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
]

### Editing apps views file-
nano myapp/views.py
### Edit - 
from django.http import HttpResponse
import datetime
def index(request):
    now = datetime.datetime.now()
    html = "<html><body>Hello World. <br> It is now %s.</body></html>" % now
    return HttpResponse(html)
Mentioning app name in settings installedApp array-
nano basicdjango/settings.py
INSTALLED_APPS = [
    'myapp',
]

### Create a requirements.txt with django in it-
pip3 freeze > requirements.txt

### Run this django project to verify if everything is fine-
python3 manage.py runserver
### If no error-
## Goto - localhost:8000


# Let’s use docker now-
### Now from basicdjango main folder parallel to manage.py
Ref- https://www.geeksforgeeks.org/dockerizing-a-simple-django-app/

### Creating Dockerfile-
touch Dockerfile
nano dockerfile
### Edit-
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]



### Building image- 
sudo docker build -t basicdjango .

### Running docker image -
sudo docker run -p 8000:8000 image_name

## Goto- localhost:8000


### Now Push this image to docker hub-
Login to dockerhub(https://hub.docker.com/)-

### Create a repository there
You will get-
To push a new tag to this repository,
docker push diwamishra21/djangobasic:tagname

### Now login to dockerhub from Command line- 
docker login
Provide username and pass

### Tag your image with your dockerhub image
docker tag basicdjango diwamishra21/djangobasic:latest

### Now push to dockerhub-
docker push diwamishra21/djangobasic:latest


## Let’s push this project to github-
### Create a repository in github and copy its clone command

### Clone repository in local machine-
git clone <ur>

### Copy whole project inside this repository-
cp <django-project> <github folder>

### Check git status-
git status

### Now give user details to git config-
git config user.email “your email”

### Now add all files and folders to git-
git add .

### Commit -
git commit -m “Initial commit”

### Push-
git push

### Now provide your username and password

That’s it

## What you Got-
* Created a django project using docker
* Created docker image on dockerhub, it can be usedby anyone now
* Created github repository for this django-docker project

## Thank You
