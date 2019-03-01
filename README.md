# [massoth.tech](https://www.massoth.tech/)
## Code and resources of my personal website
This is the repository containing most of the code that runs on my personal website, [massoth.tech](https://www.massoth.tech/).
## Repository Structure
In the base directory, general Google app-engine related files can be found. The main entry point, `main.py` can also be found here. The modules are located inside of the `app/` directory along with the templates and static files. 
## Installation and Running
If you want to install and run this application locally (why), you will need to install the [Google App Engine Cloud SDK](https://cloud.google.com/appengine/docs/standard/python/download). `pip` is also required. After cloning the repository, navigate into it and run `pip install -t lib -r requirements.txt`. This installs all the requirements locally into `lib/`.<sup>[1](#footnote)</sup> You can then run a dev server with `dev_appserver.py app.yaml`. 
## Stack
The website is a Flask deployment on Python 2.7, using Jinja2 templates for most of the frontend. It is hosted on Google App Engine.


<a name="footnote"><sup>1</sup></a>: you may need to create this directory manually with `mkdir lib`. 
