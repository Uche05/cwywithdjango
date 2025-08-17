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

Here is the locally deployed look:

`<img src = "documentation/screenshotone.png" alt= "local-screenshot">`

## Basic-content

For SECURITY reasons, I decided to remove certain variables set in the settings.py and use environment variables instead.

## UX

#### User Experience Documentation

### Target-audience

 My Project 4 (CWY) is a full stack website which is made to benefit two different kinds of users; a visitor (an unregistered user), and the registered users such as staff members/ employees(staff), administrative workers(admin), and businesses(client) that utilize CWY's service. Please note that I have added needed credentials to test admin, user and client. We have made it such that only sign ins are possible and not sign ups as per business requirement, the admin who would have their details can add users and then this would be sent to users and clients when needed.

### User-stories

#### New / Unregistered User

- As a new user (visitor), I want to be able to register my interest to work with CWY, via a form and expect some action to be performed such as a confirmation email or some element pop-up displayed so that I can be ensured the CWY received my interest.

#### Registered Users

- As a staff user, I want to be able to log in to my account, using the details sent to me, so I can know I am part of the organization.
- As a staff user, I want to be able to set my non-availability after login so that my bosses and the workplace I have will know when I am not available/ when I am on holiday.
- As a staff user, I want to be able to see necessary details about myself after login, so that I know the company has needed details about me.
- As a staff user, I want to see what work schedule has been booked into my dashboard.
- As a client user, I want to be able to log in to the client portal, using my login details, so that I can use their client dashboard system.
- As a client user, I want to be able to see the staff made available to my company, request change or set service unavailability so that I know which staff is cleaning when we need cleaning and let you know when we do not need cleaning.
- As a client user, I want to be able to specify when I need or don’t need cleaners.
- As a client user, I want to be able to log in requests and necessary complaints about the staff/ service being received.
- As an admin, I want to be able to sign in using the details sent to me, so that I can have access to necessary employees and workplace details.
- As an admin, I want to be able to view the availability of my staff and the client they work for, so I can approve or disapprove their availability such as holiday.
- As an admin, I want to  be able to view the requests and complaints sent to me by the client.

Future

- As a client user, I want to be able to create an account, so that I can use their client dashboard system and they know I am their client.

## Pre-development

### Colour-scheme

`<img src = "documentation\screenshotcolorscheme.png" alt = "color schemes screenshot">`

### Typography

###### From Google Fonts:

- Noto Sans
- Open Sans
- Work Sans

### Wireframes

`<img src = "documentation\wireframe.png" alt = "wireframes screenshot">`

### Flow-diagram

1. Unregistered user

Home page -> contact page

2. Registered User

- Employees
  Home page -> Staff-Login -> Staff Dashboard
- Clients
  Home page -> Client Login -> Client Dashboard
- Admin
  Home page -> Admin Login -> Admin Dashboard
- There is no sign up feature yet!!

### ERD

UserProfile Table

| Key | Column Name | Type                              |
| --- | ----------- | --------------------------------- |
| PK  | UserID      | SERIAL                            |
|     | Name        | VARCHAR(255)                      |
|     | Email       | VARCHAR(255)                      |
|     | Password    | EMAIL                             |
|     | UserType    | ENUM ("Staff", "Client", "Admin") |
|     | Location    | VARCHAR(255) only for clients     |

 Availability Table

| Key                 | Column Name    | Type                    |
| ------------------- | -------------- | ----------------------- |
| PK                  | AvailabilityID | SERIAL                  |
| FK to Users.UsersID | CustomerID     | VARCHAR(255)            |
|                     | StartDate      | DATETIME                |
|                     | EndDate        | DATETIME                |
|                     | Status         | ENUM ("OPEN", "CLOSED") |

Bookings Table

| Key                 | Column Name    | Type                    |
| ------------------- | -------------- | ----------------------- |
| PK                  | BookingsID     | SERIAL                  |
| FK to Users.UsersID | CustomerID     | VARCHAR(255)            |
| FK to Users.UsersID | EmployeeID     | VARCHAR(255)            |
| FK                  | AvailabilityID | SERIAL                  |
|                     | BookingDate    | DATETIME                |
|                     | Status         | ENUM ("OPEN", "CLOSED") |

TimeOffRequest Table

| Key                 | Column Name | Type                    |
| ------------------- | ----------- | ----------------------- |
| PK                  | ID          | SERIAL                  |
| FK to Users.UsersID | EmployeeID  | VARCHAR(255)            |
|                     | StartDate   | DATETIME                |
|                     | EndDate     | DATETIME                |
|                     | Reason      | TextField               |
|                     | Status      | ENUM ("OPEN", "CLOSED") |

ContactInterest Table (non-relational to the rest of the tables)

| Key | Column Name | Type                              |
| --- | ----------- | --------------------------------- |
| PK  | UserID      | SERIAL                            |
|     | Name        | VARCHAR(255)                      |
|     | Email       | EMAIL                             |
|     | Phone       | VARCHAR(11, with regex)           |
|     | Message     | ENUM ("Staff", "Client", "Admin") |
|     | Created At  | VARCHAR(255) only for clients     |

# Features

### Developer-tools

- ChatGPT to aid me with major deployment issues and think of solutions to non-working code that I made. I used it for debugging, to help me write tests and introduced me to the concept of environment variables.
- CSS to design and style the pre-existing HTML structure
- [Heroku](https://dashboard.heroku.com/apps) used for hosting the deployed front-end & back-end site.
- HTML to give my website full structure
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- Javascript (AJAX) to make adding details dynamic and not involve extra HTML files.
- Microsoft Sniping tool to take screenshots of my local working deployment
- [PEP8 CI Linter](https://pep8ci.herokuapp.com/#) used to do checks for errors on my Python Code.
- Python programming language with Django Framework.
- StackOverflow used to check for similar errors and their solutions.
- [VSCode](https://code.visualstudio.com/) used for local IDE for development. It possessed extensions which helped me immensely during my making of the site.

### Python Libraries and Packages Used

- Django was the main Python framework used in the project

asgiref==3.8.1

bleach==6.2.0

certifi==2025.1.31

charset-normalizer==3.4.1

dj-database-url==0.5.0

Django==4.2.20

django-summernote==0.8.20.0

djangorestframework==3.16.0

dotenv==0.9.9

gunicorn==20.1.0

idna==3.10

psycopg2==2.9.10

PyJWT==2.10.1

python-dotenv==1.1.1

requests==2.32.3

setuptools==78.1.0

sqlparse==0.5.3

tzdata==2025.2

urllib3==2.4.0

webencodings==0.5.1

whitenoise==5.3.0

## Testing

The portal has been well tested and the results can be viewed `<a href= "#TESTING.md">`here `</a>`.

### Future Updates

- Visiblly asethetic webpage
- Clients to be able to create accounts.
- Email notifications after registering interest.
- More visuals after registering or performing a CRUD operation.

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

| Source                                                                                               | Location                                                | Notes                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Markdown Used](https://github.com/markdaniel1982/MD82-P4/tree/main?tab=readme-ov-file#site-objectives) | Markdown                                                | Markdown template was from the given,[github repo](https://github.com/markdaniel1982/MD82-P4) for the both "README" and "TESTING" from [here](https://github.com/markdaniel1982/MD82-P4) |
| [As Full Stack Website](https://uche05.github.io/AsFullStackWebsite/)                                   | HTML and CSS and JS templates where extracted from here | [Here](https://uche05.github.io/AsFullStackWebsite/ "Here")                                                                                                                              |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Ben Kavanagh](benjamin.a.kavanagh@gmail.com) for his support throughout the development of this project.
- I would like to thank [Code Institute](https://codeinstitute.net) for giving me the opportunity to complete the P3 course.
- I would like to thank the [Code Institute](https://codeinstitute.net) facilitator team, [Iris Smok](https://github.com/Iris-Smok/Iris-Smok), [the Code Institute Student Care Team](studentcare@codeinstitute.net) and [Irene Neville](irene.neville@codeinstitute.net) for their advice.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support and general information that helps with my studies with Code Institute.
- I would like to thank my family, for their support and understanding, for believing in me, and allowing me to make this transition into software development.
- I personally enjoyed performing this project as it was a chance to both construct a program using coding programming techniques and paradigms; to make a functional content myself while properly iterating tasks to be performed.
- Written and edited by Uchechukwu Christian Kpadeuwa
