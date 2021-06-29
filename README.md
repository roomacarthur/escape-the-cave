# Escape The Cave
## by. Ruairidh MacArthur

![Escape the Cave live example](assets/images/example1.gif)

- [Live Site](https://escape-the-cave.herokuapp.com/)

- [Repo](https://github.com/roomacarthur/escape-the-cave)

# Table of Contents
1. [Intro](#intro)
2. [Technologies](#technologies)
3. [Bugs & Fixes](#bugs--fixes)
4. [Testing](#testing) 
5. [Credits](#credits)
6. [Deployment](#deployment)



## Intro

A text-based, turn-based game that the user will operate in the command line. The aim of the game is to escape the cave without getting caught by your captures. This game is completely written in Python.

## Design

[Code Logic Flow Chart](assets/flowchart.pdf)

[Game Story/Content](https://docs.google.com/document/d/1gkMlBvm8pnAvG1E_excuL2s7OM48bxCQQx1XOgrXz50/edit?usp=sharing)

### Goals

The main goal of this application to provide a fun text-based, turn-based game that runs in the command line. I hope to achieve a good level of nostalgia for the older generations. 

### Audience

The application has no strict audience, it is aimed at anyone that want's to play, I believe the older generations will find it more interesting as there are no fancy graphics.

## Technologies

### Languages

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Other Technologies and Libraries 

- [GitHub](https://github.com/)
- [Git](https://gitforwindows.org/)
- [VS-Code](https://code.visualstudio.com/)
- [Heroku](https://heroku.com)
- [Time](https://docs.python.org/3/library/time.html)
    - To allow for timing between character output in the typing() function to achieve a typing style animation for the output.
- [sys](https://docs.python.org/3/library/sys.html)
    - sys standard output is used to allow for the typing() function to output to the terminal. This prevents it being printed out 1 character per line as it would with the print() function.

## Bugs & Fixes

1. The typing animation function works flawlessly in the terminal but when pushing to Heroku and running it through the terminal template provided the animation isn't showing. 
    - Currently no fix found.
    
2. FIXED: When passing the code through the [pep8 validator](https://pep8online.com) there was a lot of errors for line length.
    - I have shortened the story outputs and moved the functions onto new lines.
    ![Pep8 line error](assets/images/pep8-line-error.png)

## Testing

For testing, print statements were used heavily during the coding of the application. 
Once finished I manually tested the application, navigating all paths to see if they gave the expected result.
All manual testing results can be found below:
### [TESTING SHEET](https://docs.google.com/spreadsheets/d/1a76gGDzSrekAAO0boTX2rMBjeMiLd7eRQbkZOI7SfSQ/edit?usp=sharing)

### User testing feedback.

1. Fun and enjoyable, reminded me a lot of the earlier games and activities I could play when I first got a PC.

2. I really enjoyed the fact I could play the game completely through my keyboard! The fact I could name the axe was pretty cool.

## Credits

1. [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for my python project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.
2. [Stack Overflow](https://stackoverflow.com/questions/4627033/printing-a-string-with-a-little-delay-between-the-chars)
    - For assistance with the typing() function in functions.py

## Deployment

This application will be deployed via [Heroku](https://heroku.com)

### Creating App.

1. Ensure all code is correct and ready for deployment. 
2. Enter the following code to import the required dependencies to the requirements.txt file:
    > pip3 freeze > requirements.txt
    - Heroku will use this file to import the dependencies that are required.
3. Log into or sign up to Heroku(it's free).
    - If signing up, you will need to wait and accept an authentication email.
4. Navigate to Dashboard. 
5. Click "New" and select "create new app" from the drop-down menu. This is found in the upper right portion of the window. 
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
6. Ensure the correct branch is selected "master/Main", and select the deployment method that you desire. In this case, I will be using Automatic Deployment.

### Forking Repository

If you wish to experiment with the code freely, you can achieve this by forking the repository. Forking a repository allows you to experiment without the original project being affected. To achieve this you need to:

1. Navigate to the repository roomacarthur/escape-the-cave.
2. In the top right of the page, below your profile you should see a "Fork" button. Simply click on this.
3. A copy of the repository will then be added to your own Repositories Page.

### Cloning Repository

1. Open GitBash ad create a directory where you want to save the code.
    
    > $ mkdir "directory-name"
2. Navigate into the new directory
    
    > $ cd "directory-name"
3. Navigate to the repository on GitHub [HERE](github.com/roomacarthur/escape-the-cave)
4. On the upper right hand side of the content, click on the button "Code"
5. A dropdown box should appear, copy the SHH key.
6. Open up your GitBash terminal from before. 
7. Clone the repository with the following command.
    
    > $ git clone "SSH-KEY"

The code will now be cloned into a local directory for you to access. You can now access the code in your IDE by entering the following code into your terminal:
    
    > $ code .

