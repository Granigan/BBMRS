# Installation

You can check out the application directly at [Heroku](http://bb-mrs.herokuapp.com/). However, if you want to run your own instance of the application, follow this guide for either Local Use or Using Through Heroku.

## Local Use

### Get the Application
Start by downloading and unpack the [Zip file](https://github.com/Granigan/BBMRS/archive/master.zip), or by cloning the [repository](https://github.com/Granigan/BBMRS) from GitHub. 

### Get Python
To run the application locally, you'll need to have [Python](https://www.python.org/downloads/) installed. 

### Create Virtual Environment
In the folder you've copied the application, run: 
'''
python3 -m venv venv
'''
This creates a specific virtual environment, allowing you to do the next step of getting dependencies just for this app, instead of your whole system. But note that you must also activate the environment, do this by running:
'''
source venv/bin/activate
'''
You should see *(venv)* at the start of your command prompt now, indicating the virtual environment is active.

### Download Dependencies
We'll use *pip* to install the required dependencies. You should have this installed by default with Python, if not, [get it](https://pip.pypa.io/en/stable/reference/pip_download/).
'''
pip install -r requirements.txt
'''

### Run and Use
Activate the local server by
'''
python3 run.py
'''
and access it at [locally](http://127.0.0.1:5000/). Check the [User's Guide](https://github.com/Granigan/BBMRS/blob/master/documentation/manual.md) for details on using the application.


## Using Through Heroku

### Fork the Repository
We'll be using Heroku via GitHub, so instead of directly downloading the application, fork it instead to your own GitHub account. Once you have the repository forked and a synced local copy of it, we can link it to Heroku.

You'll need to have a [Heroku](herokuapp.com) login, and [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed. Then input these commands from the folder you installed the application to.
'''
heroku create your-application-name-here
'''
And then upload via git:
'''
git push heroku master
'''

And now you should be able to access the application online, at your-application-name-here.herokuapp.com. Check the [User's Guide](https://github.com/Granigan/BBMRS/blob/master/documentation/manual.md) for details on using the application.
