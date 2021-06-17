# Escape The Cave
## by. Ruairidh MacArthur

<div style="text-align:center"><img src="assets/images/logo.png" alt="Escape the cave logo."></div>

- [Live Site]()

- [Repo]()


### Intro

A text based, turn based game that the user will operate in the command line. The aim of the game is to escape the cave without getting caught by your captures. This game is completely written in Python 

## Technologies

### Languages

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Other Technologies and Libraries 

- [time](https://docs.python.org/3/library/time.html)
- [GitHub]()
- [Git]()
- [VS-Code]()
- [Heroku](https://heroku.com)

## Credits

1. [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for my python project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

## Deployment

This application will be deployed via [Heroku](https://heroku.com)

### Creating App.

1. Ensure all code is correct and ready to deployment. 
2. Enter "pip3 freeze > requirements.txt" to import the required dependencies to the requirements.txt file.
    - Heroku will use this file to import the dependencies that are required.
3. Log into or sign up to Heroku(it's free).
    - If signing up, you will need to wait and accept authentication email.
4. Navigate to Dashboard. 
5. Click "New" and select "create new app" from the drop down menu. This is found in the upper right portion of the window. 
6. Provide a name for your application, this needs to be unique, and select your region.
7. Click "Create App".

### Setting up Heroku App

1. Navigate to "Settings" and scroll down to "build packs".
2. Click "build packs" and then click both "python" and "node.js"(node.js is needed for the mock terminal.)
3. Ensure that the python buildpack is above the node.js buildpack, You can click and drag the packs to re-arrange them.

### App Deployment.

1. Navigate to the "Deploy" section.
2. Scroll down to "Deployment Method" and select "GitHub".
3. Authorize the connection of Heroku to GitHub.
4. Search for your GitHub repository name, and select the correct repository.
5. For Deployment there are two options, Automatic Deployments or Manual.
    - Automatic Deployment: This will prompt Heroku to re-build your app each time you push your code to GitHub.
    - Manual Deployment: This will only prompt Heroku to build your app when you manually tell it to do so. 
6. Ensure the correct branch is selected "master/Main", and select the deployment method that you desire. In this case I will be using Automatic Deployment.

