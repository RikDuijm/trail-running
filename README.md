[![Build Status](https://travis-ci.org/RikDuijm/trail-running.svg?branch=master)](https://travis-ci.org/RikDuijm/trail-running)

# Trail running - responsive application

This application is developed for a fictitious running store, specializing in products for trail runners. Like many small sports, this is a niche market, in which consumers are willing to pay a lot for products and services that match their interests and perception. The customer is usually intensively engaged in his hobby and very serious about it. He invests hours per week, and in the specific case of the trail runner you can almost say that his hobby is a way of, and attitude to life.

The shopping experience – both online or physical – is therefore extremely important. The customer must be able to identify with the store, love to visit it and feel part of a movement or group. Once the store succeeds in winning over the customer, he/she will keep coming back.
Therefore, having just an online store is not enough. The idea is to create an additional online platform, that engages the customer.

This website aims to achieve the following:
Winning over the customers and maintaining their interest with the ultimate goal of generating income. The customer must identify with this website and return very regularly, so that the chance of selling products is increased. Additional income can also be generated, for example through the sale of advertisements.

- [**View the website here**](https://rik-duijm-trail-running.herokuapp.com/)
- [**View the Github Repository here**](https://github.com/RikDuijm/trail-running/)

![screenshot website](/media/img/screenshot-final-page.jpg)

## Contents Table
1. [**UX**](#ux)
    - [The Audience](#audience)
    - [User Stories](#user-stories)
    - [The application](#application)
    - [User Experience](#user-experience)
    - [Design Ideas](#design-ideas)
    - [Wireframes](#wireframes)

2. [**Functionality and Features**](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)
   - [Manual Testing](#manual-testing)
   - [Automated Testing](#automated-testing)
   - [Note for Code Institute](#note)

5. [**Deployment**](#deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Help with code**](#help-with-code)
    - [**Acknowledgements**](#acknowledgements)

## <a name="ux"></a>UX

### <a name="audience"></a>The Audience

**Who is the target audience?**

***The trail runner***\
Diverse in age and geographical locations and of both genders, there are still important common characteristics in the target audience. 

Obviously the audience share a common hobby and they are all quite passionate about it.

Although it’s not an elite sport, trail runners tend to be higher educated, earning above average. The trail runner is usually intensively engaged in his hobby and very serious about it. For many of the trail runners the equipment is very important. Normally they spend quite some money on shoes, gear, clothes, food and supplements. 
They like nature, are mostly socially engaged and conscious living. And they are above average adventurous. Generally they like to travel and explore new destinies / activities.

***What's cultural appropriate for the audience?***\ 
The site must emanate that the customer and his needs are understood. Product offers, events, stories and information should all 	seamlessly connect to the customer. The customer must feel that the website is on ‘on the same page’, offering information, inspiration and products even before he / she can wonder if this would be available. 

### <a name="user-stories"></a>User Stories
**As the website owner, I would like to distinguish myself from my competition with an application that offers:**
- a range of high quality products that seamlessly fits the needs of the customer, with ‘cool’ marks and gadgets, against very competitive prices. This should include an online cart and payment possibility.
- sublime information, so that the user will have another reason to visit the website and will return there over and over again. These are all sales opportunities!
- inspiring stories and other content (photos, videos) that fulfil the need of the customers to read about / live their hobby. This ensures that the customers feel connected to the website, making it plausible that they will visit the website many times.
- an event calendar, firstly to inform and serve the customer, secondly to facilitate a platform / technical assistance for event organizers. With this calendar a discount can be offered to the customer or a commission could be charged to the organizer. At the same time, a valuable relation with the race organizers is created.
- an online community where users can post blogs and contact each other. This creates a very valuable community feeling, the sense that the user “belongs” to something and connects to the website. Again it makes it very plausible that the user will return many times to the website and let his eye fall on newly promoted products.
 
 
**As a user I’d like to:** 
- search for / purchase high quality products at a favourable price.
- learn about / enrol in cool events.
- read about my hobby.
- find destinations, routes, and advice about health and injuries, diet and training.
- connect with likeminded people, maybe find training mates or exchange stories and tips and tricks.
 

**As an guest editor I’d like to have:** 
- a platform to show off my expertise, to reach and persuade potential clients. 
 

**As an event organizer I’d like to have:** 
- a platform to promote my event. 
- the technological ability to facilitate online enrolments and payments
 

**As an advertiser I’d like to have:** 
- the possibility to advertise to a clearly defined audience that is hugely interested in my specific products / services.
 

### <a name="application"></a>The application
**What are we making?** 
Given the enormous amount of web shops, we feel that our regular web shop isn’t competitive enough anymore. To be able to distinguish from competitors we want to create an environment that the user likes to visit and return to over and over again. 
Secondly we also feel that there always more ways to generate revenue, and we should consider advertisements, and offering collaboration with other companies and organisations that share our audience, as long as they are no direct competitors. 

This is achieved by: 

**1. An online store with weekly offers** 
A selection of products from the separate, larger online store is offered here. The idea is to promote new products every week at a significant discount. Only registered users can purchase these products. 

**Why does the user want this?** 
The user / the citizen wants to be able to see if a problem is already reported and if not, communicate problems with the municipality without hassle / having to waste time in a phone call. Finally he wants to see his report back, so that he’s sure that the municipality has to do something about it.

### <a name="user-experience"></a>User Experience

**What makes a good user experience?**<br>
- Presenting an easy navigable, comprehensive tool to search for problems in a given street and, if a problem is not reported yet, making it as easy as possible for the user to report it.
- To lower the threshold for a citizen to communicate with the municipality, it must take the least amount of time possible to report a problem.
- The idea that the municipality acts upon reported problems.

### <a name="design-ideas"></a>Design Ideas
The website must be accessible. The user must be able to navigate quickly and intuitively and must easily find all relevant information. Given the fact that it’s a website of a city council it also must have a business-like and lean design.

Based on those ideas, I made the following choices:

- **Font**<br>
I chose the Font 'Roboto', sans-serif because this is a soothing, modern letter. This contributes to the clarity of the page.

- **Colours**<br>
I chose to work with only four colours: a bright red, a dark blue for the navigation bar, a black font and a white background. This contributes to the clarity of the page, but shows also its business-like character and a certain authority.

- **Content**<br>
The website is mobile first. The user must be able to report a problem on the spot, not having to start up his computer to do so. It means that the amount of information presented must be minimized. When entering the website it must be clear that reporting a problem is an easy, quick and painless process.

- **Progress bar**<br>
To emphasize the ease of reporting an issue we make use of a progress bar, already in 20% when entering the website. That’s how quick it is!

- **Images**<br>
Although the website must look visually nice, images are of no importance. It’s all about functionality. Therefore, the only image you see is the municipality arms.

### <a name="wireframes"></a>Wireframes
This is a mobile first app. I expect the client to use this app mostly on a mobile phone walking on the street and noticing something, or maybe on a tablet afterwards. I don’t expect many users to use a desktop, but it’s certainly also designed for that, especially since most administrator might use a desktop.

The whole design and the choices I made are based on that assumption. I made six mobile wireframes, reflecting the process of reporting a problem described above.

1. [initial screen](https://github.com/RikDuijm/municipality/blob/master/user-design-experience/Municipality%20App%201.jpg)
2. [screen after searching on street name](https://github.com/RikDuijm/municipality/blob/master/user-design-experience/Municipality%20App%202.jpg)
3. [screen for log in](https://github.com/RikDuijm/municipality/blob/master/user-design-experience/Municipality%20App%203.jpg)
4. [overview of reports](https://github.com/RikDuijm/municipality/blob/master/user-design-experience/Municipality%20App%204.jpg)
5. [form to report a problem](https://github.com/RikDuijm/municipality/blob/master/user-design-experience/Municipality%20App%205.jpg)

I created exactly what I had in mind, with the following exceptions:
- In wireframe 4 it was possible for a user to comment on a problem. To minimize possible abuse (or complaints about the time it takes for the municipality to act upon something) I decided to make this option not available for the public, but only for the administrator. Also, the position of the button “comment” (and “delete”) has changed, and are not placed vertically instead of horizontally, because of readability issues on a mobile phone.
- Initially I was thinking about creating a Dashboard with information about the amount of problems the municipality solved. However I decided to not develop this, but move on with my studies.

**Larger screens**<br>
There is hardly any difference between the mobile and larger screens. Because of that I didn’t feel the necessity to create wireframes for larger screens.

## <a name="features"></a>Functionality and Features

### <a name="existing-features"></a>Existing features

- **Search functionality**<br>
The municipality wants the user to look first if a problem is already reported. On the homepage there is a search functionality with the instruction “1. Look for reported problems – enter street namook for reported problems – enter street name”.
Search functionality must not be case sensitive. Furthermore, if part of a street name is typed, it must give suggestions. If the search button is clicked without typing anything, all results should show.

- **Login and Registration functionalities**<br>
After searching for reported problems in a given street the user has the possibility to login to report a new problem. Therefore he also has the possibility to register himself. In this application he can choose username and password, but in real life he would have to register with his full name and for example his id-number.
If a user wants to register with an existing username, he gets a message that that username is already taken. When registered, the user can log in, providing his credentials. If he makes a typo, he receives a message to try it again.

- **Report form**<br>
After successfully logging in the user is sent to the page where he can use a form to report a problem. His username is already selected and not changeable and also the date / time of the report is filled-in already. He can only fill out the street name and the problem he is reporting.

- **Overview of reports**<br>
After submitting the form, the user is sent to a general overview of all the reported problems. The most recently reported problem will be on top of the list, so the user will see his report immediately. He can click on the report to see if the municipality already posted a reaction.

- **Navigation bar and environment for admin**<br>
There is also a navigation bar on top of the page. If a user logs in using the navigation bar, he technically can report a problem at once, without having to look if it’s already reported. Obviously I could choose to delete the login in the navigation bar, but a user can also be an administrator, and I’ve chosen to maintain the login so that the administrator can enter the system as quickly as possible. He can do so to provide his credentials and he get an overview of all the reports, most recently reported first. Here, he can comment on reports or delete them, something a regular user cannot do. Obviously the administrator can also search per street name.

*`Please check this environment with the following credentials: Username: admin, Password: admin.`*

- **Footer**<br>
Allows the user to see the contact details and opening hours of the municipality and their social media canals (Facebook, Instagram, Twitter). None are clickable for now.

### <a name="features-left-to-implement"></a>Features left to Implement

- **Dashboard**
To show how many problems there have been reported per street / how long it took to solve what type of problems. This might be desirable for the municipality to show off how fantastic a job they are doing, or maybe to make clear internally that they need more infrastructure / resources to do the job. In that case, the dashboard would not be available for the public.

- **Photos of problems on website**
I would like to add the possibility that people can send in a file / photo with the form. Obviously this could help the municipality to get a quick and clear impression on the (urgency of a) problem. It could also help a user to understand whether this is the problem he also wanted to report or not.
I figured out how to receive an uploaded file in MongoDB, but not how to retrieve this on the website in a nice and consistent manner (same size, for example). So for now, I decided to delete the possibility to upload a file from the Form.

## <a name="ux"></a>Technologies Used
- **Languages**
	-   HTML5
	-   CSS
	-   Python
	-   JS

- **Libraries, plugins and modules**
	- Bootstrap 4 for the grid system of the page, the form and the progress bar
	- Flask to construct and render pages
	- Jinja2 to simplify displaying data from the backend
	- Re for the search functionaluty
	- Bcrypt for the login functionality
	- Tempus Dominus as a date / time picker
	- JQuery to set the current date and time in the add-report form
	- Google fonts for the fonts.
	- Font Awesome for the icons in the footer of the website and icons8.com for the icon in the navigation bar / in the background of the page.

- **Tools**
	- IDE: Gitpod
	- Google Chrome developer tools
	- Git for version control
	- GitHub to store all project code remotely
	- MongoDB as the database
	- Heroku to deploy the project


## <a name="testing"></a>Testing
### <a name="manual-testing"></a>Manual testing<br>
#### Responsive testing
I tested the responsiveness of the page 3 times locally: one time after writing the initial code, then after making several changes, and one time right before the final deployment.
After the final deployment on Heroku, I tested it one more time remotely.
Tested devices: Nokia 8110 4G, Galaxy S5,  Galaxy S9/S9+, Pixel 2, Pixel 2 XL, iPhone6/7/8, iPhone6/7/8 Plus, iPhone X, iPad, iPad Pro, Kindle Fire HDX, 1080p Full HD Television and responsive desktop.
I used Chrome developer tools.

#### Testing different browsers
The page is tested in different browsers: Google Chrome, Microsoft Edge, Internet Explorer 11, Firefox and Ecosia. Only in Internet Explorer I found some problems with the buttons I used. This has been solved. I tested locally and also after deployment on Heroku.

#### Testing the functionality ####
I tested the functionalities by going through the steps a user should take to report a problem and by going through the additional steps an admin can take. In all cases the results matched what I expected.

**1. Search Functionality**
1. Filling in a street name that is already in the database (because a problem has been reported):
Expected result: street name and problem is shown.

1. Testing if the search functionality is case sensitive:
Expected result: not case sensitive. I tested this by filling in lower key, capital letters and a combination of upper and lower.

1. Testing if all the reports about a given street show up:
Expected result: all reports show up.

1. Testing what happens if a street is not in the database:
Expected result: no results shown.

1. Testing what happens if you hit search without entering anything.
Expected result: list of all the problems show up.

**2. Login Functionality**
1. Does the button login show in all possible scenarios of step 1?
Expected result: yes.

1. User (citizen) fills in correct credentials:
Expected result: he is redirected to the “add report” page, and the message “Welcome [username]” is shown. His username is already filled-in and the user cannot change this. Also the date is already filled-in. This is changeable.

1. User (citizen) fills in unknown username but correct password:
Expected result: user receives message “wrong credentials".

1. User (citizen) fills in correct username but incorrect password:
Expected result: user receives message “wrong credentials.

1. Administrator fills in correct credentials:
Expected result: he is redirected to an overview of all reported problems. This is the administration environment, in which admin may comment on a problem or delete it. Regular user cannot reach this. Message “Logged in as Admin” is shown.

*`Please check this environment with the following credentials: Username: admin, Password: admin.`*

6. Administrator fills in wrong username but correct password:
Expected result: admin receives message “wrong credentials.

7. Administrator fills in correct username but incorrect password
Expected result: admin receives message “wrong credentials.

**3. Register Functionality**
1. User chooses a username that already exists:
Expected result: user receives a message “username already taken”.

1. User chooses a username that doesn’t exist yet:
Expected result: he is logged in immediately and redirected to“add report” page.

1. User tries to have a space in his username (so he wants it to exist of 2 separate words, i.e. first and last name).
Expected result: this is automatically disabled.

**4. Create Report Functionality**
1. User files a report, describing the problem, entering the street name, and possibly adjust the date / time:
Expected result: after submitting he’s redirected to an overview of all the reported problems, last report (his own) shown first.

1. User doesn’t mention the street name:
Expected result: upon submitting he gets a message that he has to do so before he’s able to file the report.

1. User doesn’t mention what the problem is:
Expected result: upon submitting he gets a message that he has to do so before he’s able to file the report.

**5. Read Functionality (reported problems, regular user)**
1. Expected result if logged in as regular user:
Page that shows all the reports, ordered by date/time, latest filed report shown first. Reports show name of the street, reported problem, date and username of the person that filed the report. Toggle function that shows the response of the municipality as soon as there is one.

**6. Read Functionality (reported problems, administrator)**
1. Expected result if logged in as administrator:
Page that shows all the reports, ordered by date/time, latest filed report shown first. Reports show name of the street, reported problem, date and username of the person that filed the report. Toggle function that shows the response of the municipality as soon as there is a response.

*`Please check this environment with the following credentials: Username: admin, Password: admin.`*

   2. In this environment every item has 2 buttons: Comment and Delete.
	   1.  Update Functionality (comment button):
The admin can comment on the report, with full rights to update / change every field. Additionally he can add a reply of the municipality (i.e.: we’re working on it, problem solved, etc.). After submitting the admin is redirected to the list of reported problems, where he can check his update.
	   1.  Delete Functionality (delete button):
The admin can delete a report. Report disappears from the list of reported problems.

**7. Logout Functionality**

When clicked upon the user is logged out and redirected to the homepage.

### <a name="automated-testing"></a>Automated Testing
#### Validation services
The following validation services were used to check the validity of my code.

-   W3C Markup Validation Service was used to validate HTML.
-   W3C CSS validation was used to validate CSS.
-   JSHint was used to validate JavaScript.

#### <a name="note"></a>Note for Code Institute
After finishing my first Milestone Project I made a complaint that we hadn't had a single lesson about testing our code, but that you expect us to be able to do this. The reply I received:

*I have passed your valuable feedback over to the learning Success Team. I have spoken to someone from the team and they agreed that more information about testing and deployment is due. This is being looked into and in the process of being improved.*

I again made a complaint upon starting this Milestone Project:

*So far we only got a quick introduction to Jasmine with only 1 specific example. I feel that in the Milestone Projects there's an emphasis on the importance of testing, that isn't reflected in the course and based on this 1 lesson I can't create automated testing for this project.*

Now, with the third milestone, again I don’t feel that we received enough – if any – instructions or practice about how to test our projects. I really feel that if you think this is important you should teach us well how to do this. I don’t think I have received the tools to be able to do this.
Given the above and since I've tested all functionalities extensively manually and am sure everything works as I planned for, I didn't do further automated testing.

## <a name="deployment"></a>Deployment

The project was coded in Gitpod, which also was used for version control, and then uploaded to Github. Finally I made a connection between Github and Heroku to deploy the project.

- **Connection with MongoDB Atlas**<br>
A MongoDB Atlas database was used. To connect Flask to the MongoDB I installed the third party library flaks-pymongo. I also installed dnspython to use the new style connection string for MongoDB Atlas.

- **Connection string and secret key**<br>
In the app.py the os class getenv method is used to point Heroku to the config variable (MONGO_URI) and the secret key necessary for the login function in order to keep the production database connection string and the key secret.

- **Requirements and Procfile**<br>
A requirements.txt file is used to specify the dependencies that are required for the application to work.
A Procfile is also used to specify to Heroku the commands that are executed by the app on startup.

- **Connection between Github and Heroku**<br>
To connect the Github repository to Heroku I went to the “Deploy” tab on Heroku Dashboard and select the GitHub pane. I choose the option to auto-deploy the project whenever it’s pushed to on Github.
Finally I specified the IP, PORT, my connection string and secret key in the Heroku settings.

**View deployed version on [Heroku](http://municipality-reports.herokuapp.com/)**

- **To add this repository to your local workspace:**

    -   Go into your local workspace and open up a new terminal (git bash).
    -   You have to be inside of the directory that you want to add the cloning to.
    -   Type git clone, paste the following URL ([https://github.com/RikDuijm/municipality/](https://github.com/RikDuijm/municipality)) and press enter. The process of cloning will now be completed.

## <a name="credits"></a>Credits

### <a name="content"></a>Content
- **Written content**

All written content on this website was made by me.

- **Icons**

The municipality icon was taken from icons8.com and is free of use as long as you put a link to the website - which I did in the footer.
The social media icons are from Font Awesome.

### <a name="help-with-code"></a>Help with code
- The code to restrict the space character when registering a new user, I got from this [page](https://jsfiddle.net/taditdash/hDtA3).
- The code for the search functionaly I found on this [page](https://github.com/5pence/recipeGlut). I adapted it slightly for my own needs.
- I used a combination of the documentation of Bcrypt, tutorials and examples / solutions I found on Google to develop the Registration and Login functionality. I combined all those sources in a long and frustrating process to get the functionalities to work. However, I didn't use code of others 1 on 1.

## <a name="acknowledgements"></a>Acknowledgements
Thanks to my mentor Spencer Barriball and fellow student Peter Lenting for discussing ideas and providing help on several occasions.

