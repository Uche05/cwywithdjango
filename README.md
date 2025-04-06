# [CWY-P4](link)

- My Project 4 (CWY) is a full stack website which is made to benefit two different kinds of users; a visitor (an unregistered user), and the registered users such as staff members, administrative workers, etc.
- This project for the sake of client, customer confidentiality (as it solves a real-life organization) will be named CWY-P4 or CWY or My Project 4.

## Table of Contents

<details>
<summary>Click here for Table of Contents</summary>

[Mock-up Screenshots](#mockup-screenshots)
[Basic Content](#basic-content)

[User Experience/ UX](#ux)

- [Target Audience](#target-audience)
- [User Stories](#user-stories)

[Pre-development: Design &amp; Database Choices](#pre-development)

- [Colour Scheme](#colour-scheme)
- [Typography](#typography)
- [Wireframes](#wireframes)
- [Flow Diagram](#flow-diagram)
- [ERD](#erd)

[Features](#features)

[Tools and Technologies Used](#developer-tools)

[AGILE](#agile)

[Testing](#testing)

[Deployment](#deployment)

[Credits](#credits)

- [Content and Code](#content-and-code)
- [Acknowledgments](#acknowledgements)

</details>

## Mockup-screenshots

<img src="#" alt = "screenshot 1">
<img src= "#" alt= "screenshot 2">

## Basic-content

Rewrite what Project 4 is about and a list of necessary general features and how it solves a problem.

## UX
#### User Experience Documentation

### Target-audience

 My Project 4 (CWY) is a full stack website which is made to benefit two different kinds of users; a visitor (an unregistered user), and the registered users such as staff members/ employees(staff), administrative workers(admin), and businesses(client) that utilize CWY's service.

### User-stories

#### New / Unregistered User
- As a new user (visitor), I want to be able to register my interest to work with CWY, via a form and expect some action to be performed such as a confirmation email or some element pop-up displayed so that I can be ensured the CWY received my interest.

#### Registered Users
- As a staff user, I want to be able to log in to my account, using the details sent to me, so I can know I am part of the organization.
- As a staff user, I want to be able to set my non-availability after login so that my bosses and the workplace I have will know when I am not available/ when I am on holiday.
- As a staff user, I want to be able to see necessary details about myself after login, so that I know the company has needed details about me.
As a staff user, I want to see what work schedule has been booked into my 

- As a client user, I want to be able to create an account, so that I can use their client dashboard system and they know I am their client.
- As a client user, I want to be able to log in to the client portal, using my login details, so that I can use their client dashboard system.
- As a client user, I want to be able to see the staff made available to my company, request change or set service unavailability so that I know which staff is cleaning when we need cleaning and let you know when we do not need cleaning.
- As a client user, I want to be able to specify when I need or don’t need cleaners.
- As a client user, I want to be able to log in requests and necessary complaints about the staff/ service being received.

- As an admin, I want to be able to sign in using the details sent to me, so that I can have access to necessary employees and workplace details.
- As an admin, I want to be able to view the availability of my staff and the client they work for, so I can approve or disapprove their availability such as holiday.
- As an admin, I want to  be able to view the requests and complaints sent to me by the client.


## Pre-development

### Colour-scheme
Copy from the cwyspecs Word document made!!!

### Typography

### Wireframes

### Flow-diagram

### ERD

## Features

## Developer-tools

- [Heroku](https://dashboard.heroku.com/apps) used for hosting the deployed front-end & back-end site.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [GitPod&#39;s Workspace](https://codeinstitute-ide.net/workspaces) used to manage and run the development workspace for the Product Sales Aid project seamlessly.
- [Google Sheets](https://docs.google.com/spreadsheets/d/1QKMGuemIVcsDW5-9jmrrAfPrRtCDpV8x_o3t4_soqMk/edit?gid=0#gid=0) used to store user inputted data and will be the sheet the Uche Company uses to view their customer orders.
- [PEP8 CI Linter](https://pep8ci.herokuapp.com/#) used to do checks for errors on my Python Code.
- [Microsoft Visio](https://www.microsoft365.com/launch/Visio/?auth=2&home=1) used as flowchart making tool to make the steps the application would take.
- [VSCode](https://code.visualstudio.com/) used for local IDE for development. It possessed extensions which helped me immensely during my making of the site.
- [MS Copilot]() was used to help me understand the errors brought out in the PEP8 Linter from CI and I used it as a tool to help me better understand the meaning of those errors and how to face them such as the E128 continuation line under-indented for visual indent. It was used as a tool to also aid me better understand the "gspread" and "google-auth" packages as looking at documentation was very uncanny.
- [W3C HTML Validator](https://validator.w3.org/) used to do checks for errors on HTML elements of the official website.

### Python Libraries and Packages Used

- Django was the main library of the project

## Testing

The portal has been well tested and the results can be viewed <a href= "#TESTING.md">here</a>.

### Future Updates

- Update A
- Update B
- Update C


## Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

### Heroku

The Application has been deployed from GitHub to Heroku by following the steps:

- Create or log in to your account at heroku.com
- Create a new app, add a unique app name and then choose your region from Europe or America.
- Click on create app
- Go to "Settings"
- Under Config Vars add the private API key information using key 'CRED' and into the value area copy the API key information added to the .json file. - Also add a key '' and value ''.
- Add required buildpacks (further dependencies). For this project, set it up so Python will be on top and Node.js on bottom
- Go to "Deploy" and select "GitHub" in "Deployment method"
- To connect Heroku app to your Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
- Choose the branch you want to build your app from
- If preferred, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
- Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.
- Branching the GitHub Repository using GitHub Desktop and Visual Studio Code
- Go to the GitHub repository.
- Click on the branch button in the left hand side under the repository name.
- Give your branch a name.
- Go to the CODE area on the right and select "Open with GitHub Desktop".
- You will be asked if you want to clone the repository - say yes.
- GitHub desktop will suggest what to do next - select Open code using Visual Studio Code.
- The deployed project live link is HERE - Use Ctrl (Cmd) and click to open in a new window.

#### Cloning

- You can clone the repository by following these steps:

1. Go to the [GitHub repository](link to Github here!!).
2. Locate the Code button above the list of files and click it.
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard.
4. Open Git Bash or Terminal.
5. Change the current working directory to the one where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone my repository:
   - `git clone link to Github here!!.git`
7. Press Enter to create your local clone.

For Gitpod users, this was not implemented on gitpod, it was from gitpod to an SSH Connection on my local PC directly to Github via git and some useful VSCode extensions.

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](link to Github here!!).
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account.

## Credits

The following are credits to various people and technologies that have directly or otherwise assisted in the creation of the Uche's PAS(Product Sales Aid) site.

### Content and Code

| Source                                                  | Location                                                                                                    | Notes                                                                                                                                                                                                                  |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Markdown Used](https://github.com/markdaniel1982/MD82-P4/tree/main?tab=readme-ov-file#site-objectives)    | Markdown                                                                                                    | Markdown template was from the given, [github repo](https://github.com/markdaniel1982/MD82-P4) for the both "README" and "TESTING" from [here](https://github.com/markdaniel1982/MD82-P4)               |
| [A](https://linktoGithubhere!!) |stuff about it |More stuff...     |
| [A](https://linktoGithubhere!!) |stuff about it |More stuff...     |
| [A](https://linktoGithubhere!!) |stuff about it |More stuff...     |
| [A](https://linktoGithubhere!!) |stuff about it |More stuff...     |
| [A](https://linktoGithubhere!!) |stuff about it |More stuff...     |
| [A](https://linktoGithubhere!!) |stuff about it |More stuff...     |



### Acknowledgements

- I would like to thank my Code Institute mentor, [Ben Kavanagh](benjamin.a.kavanagh@gmail.com) for his support throughout the development of this project.
- I would like to thank [Code Institute](https://codeinstitute.net) for giving me the opportunity to complete the P3 course.
- I would like to thank the [Code Institute](https://codeinstitute.net) facilitator team, [Iris Smok](https://github.com/Iris-Smok/Iris-Smok), [the Code Institute Student Care Team](studentcare@codeinstitute.net) and [Irene Neville](irene.neville@codeinstitute.net) for their advice.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support and general information that helps with my studies with Code Institute.
- I would like to thank my family, for their support and understanding, for believing in me, and allowing me to make this transition into software development.
- I personally enjoyed performing this project as it was a chance to both construct and actually program using coding programming techniques and paradigms; to make a functional content myself.
- Written and edited by Uchechukwu Christian Kpadeuwa
