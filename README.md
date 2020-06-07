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
    - [Content](#content)
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
**What are we making?**\
Given the enormous amount of web shops, we feel that our regular web shop isn’t competitive enough anymore. To be able to distinguish from competitors we want to create an environment that the user likes to visit and return to over and over again. 

Secondly we also feel that there always more ways to generate revenue, and we should consider advertisements, and offering collaboration with other companies and organisations that share our audience, as long as they are no direct competitors. 

This is achieved by: 

**1. An online store with weekly offers**\
A selection of products from the separate, larger online store is offered here. The idea is to promote new products every week at a significant discount. Only registered users can purchase these products. 

The objective is threefold:
1. Generate sales
1. Generate traffic to the larger store. 
1. Ensure that users regularly check the website. That should increase the amount of visits to the community and the attention for the editorial part and the events calendar - while these other sections in turn should increase the attention to the online store.


**2. Online community**\
The website offers an online community. Trail runners can post their blogs and contact other users. 

***Blog***\
Analysing social media, it becomes pretty clear that many trail runners like to write about their “epic adventures” and that many others like to read their articles. The obvious question is how many would publish on this website, but you could stimulate this by developing a discount system for runners that publish their stories here (still to be developed). 

***Profile***\
Trail runners can also create their own profile. This is needed to receive special discounts on products and events and to engage with other users. On their profile they can publish extra texts and pictures and read messages that other users sent them. 
On the protected part of the website - only accessible after registration / login - the user can find all other profiles. And the user can also send messages to other users. 

**3. An editorial section for reference and inspiration**\
The content of this section will be written by employees of the store and by specialists in one of the subjects. There are four sections where the user can find professionally written advice, tips or articles: Excercise & Injuries, Routes & Destinations, Health & Food, Stories.\
For other entrepreneurs (for example physiotherapists, dieticians, psychologists, but also tour operators and national tourist offices) it’s interesting to publish here, because it’s free publicity to their target audience.\
Also, advertising space can be sold as an additional income.

**4: An event calendar**\
Many trail runs are small-scale initiatives, created by passionate trail runners. However, they are not always able to properly promote such an event, or arrange an online registration: they often lack this specific knowledge. By facilitating an event calendar, you both form a bond with these types of organizations - with every thinkable advantage - and you provide interesting content for your target group. The user will receive a small discount upon registration through the website. However, you could also consider charging a small commission from the organizer (like booking.com) to generate extra income.

**Important note:**\
This website co-exists with our normal webshop and offers only a selection of products, at high discounts. On it, we mention that our store is behind this new website, but we don’t emphasize this. Further customer research must show whether it is desirable to integrate our normal webshop into this website or to maintain 2 separate websites. This website relies heavily on the positive feeling the user receives from it. It may be that a fully integrated webshop detracts from this feeling.

**Why does the user want this?**\
The user is interested in purchasing products for a favourable price, but given the intensity of which most trail runners “live” their hobby many will be interested in reading about it, finding trustworthy information, being able to connect with other runners and finding nice, small and unknown races in which to participate. Although the sport is getting bigger, most trail runners don’t like big events; they don’t like the mass and  mainstream and most aren’t members of a sport club. They practice their sport individually. That makes it more difficult to get engaged in the sport, finding a running mate, information – basically how to do everything. A website that offers all is very helpful. And even if a customer doesn’t make use of the community for example, he or she might still be interested in other aspects of the website. Apart from that, even if someone doesn’t make use of any of the offered extras, those can still be appreciated, making the user choose to purchase a product on this website anyway.

### <a name="content"></a>Content
**What content type would be relevant?**\
Products and people, information and inspiration: these are basically the four pillars the website stands on. They are introduced already above.

Every suggestion must be excellent, whether it’s the product choice, the presented events or the offered information. The user must be surprised every time he / she visits a page. Quantity is not the most important aspect, it’s the quality of the products or information that is offered and the positive feelings a story or picture evokes. 

### <a name="user-experience"></a>User Experience

**What makes a good user experience?**\
- The website must be easy to navigate intuitively. The structure must be clear, the user should be able to find everything within a few moments, without having to wonder how to get there. This gives the user the idea that the website owner knows what he’s doing.
- The user should get inspired and be surprised when using the website because of the quality of content presented and the way it’s presented in. The website, products and information must be original and of high quality, and should be beautifully presented. 

### <a name="design-ideas"></a>Design Ideas
The website must be accessible. The user must be able to navigate quickly and intuitively and must easily find all relevant information. 

Based on those ideas, I made the following choices:

- **Font**\
I chose the Font 'Roboto', sans-serif because this is a soothing, modern letter. This contributes to the clarity of the page.

- **Colours**\
I chose soft colours, green azure and black, representing nature. It combines well with many outdoor pictures. The plain white background also contributes to the clarity.

- **images**\
This website is about the hobby of the customer. Therefore, the selection of photos is hugely important. The customer has to get a positive feeling and should get activated and inspirated on the website. Photos should show nature and landscape on it's best.

- **Presenting the content**\
The website offers a lot of different content. Therefore it should be very easy to navigate. I chose to present the different sections of the website very clearly on the homepage. 

In the section Inspiration the subsections are presented likewise. 

In the section Discounts the categories (clothes, shoes, events, accessories) are not ordered right now (this would mean I would have to create a lot of content, which is not the purpose of the project), but it would be logical to do the same.

The events calendar only shows a search functionality to not overwhelm the senses with a long lists of events and the page that present all the user profiles is very similar. 

### <a name="wireframes"></a>Wireframes
This is a mobile first app, but many customers will also use tablet or desktop. The whole design and the choices I made are based on that assumption. I made four mobile wireframes. As I made these, it became clear that the design of the different pages was always based on the same characteristics. Therefore, to make the most of my time, I decided not to make more wireframes.

The difference between mobile, tablet and desktop design is basically a difference in the grid. That's why I didn't find it necessary to design wireframes for tablet and desktop.

1. [homepage](/media/wireframes/home.jpg)
2. [store](/media/wireframes/discounts.jpg)
3. [events](/media/wireframes/events.jpg)
4. [user profile](/media/wireframes/profile.jpg)

I created exactly what I had in mind, but you see that there are a few differences in the design and the final result, most notably that I used more colour and less white. Because of the soft green colour that I used, for me personally that isn't overwhelming. 

Although it's not visible in the design,  I was playing with the idea to integrate maps to show the routes of the race events. I planned on using the Google maps API. Because of time issues, in the end I decided not to do this. 

## <a name="features"></a>Functionality and Features

### <a name="existing-features"></a>Existing features

- **Navigation bar **/
The navigation bar contains links to all the important pages. What it shows depends on whether the user is logged in or not. 

If not logged in it shows: Home, Events, Discounts, Inspiration, Forum, Register, Login, Contact. It also shows the logo (clickable and linking to Home) and a shopping cart.
If logged in the navigation bar shows: Home, Events, Discounts, Inspiration, Forum, Community (dropdown with User Profiles, Forum, and Add Post), My Profile, Logout and Contact. 

Below, I will introduce these pages and their functionalities. 

- **Footer**/
Contains links to (not yet existing) social media pages: Twitter, Facebook, Instagram and YouTube.

- **Homepage**/
Introduces the four main sections of the website: Events, Discounts, Inspiration and Community.  

- **Events**/
Exists of a search functionality. The user can find races by searching directly on the name of the race, but also by filtering month, distance, or region. There’s also a reset button. 

After a query the races appear, ordered by date, showing the date, name, distance and place name. When clicked on a race, more information appears, and there’s a button with the possibility to register, bringing the user to the discount section where he can purchase his ticket for the race. 

If no results are found / or a query isn’t be made yet, a message “Please search (again)” appears.

Note: for now I’ve only published a few races / months / distances and regions – just to show the idea of the functionality. 

- **Discounts**/
Shows products a user can purchase / events a user can enrol into. Per item it shows the name, a picture, the normal price, the discount price, the date until the offer is valid, a box to select the quantity of items to purchase, the possibility to select the size (if applicable), and a button to add the product to the shopping cart. More info is hidden but can be read by clicking the ‘read more’ button.

The user can only add products to the cart if he’s logged in. He will see a message that the product is added to his cart. In the navigation bar he will also see the number of items in the cart appear, in a distinguished orange colour. 

If the user forgets to select the amount of products he wants to purchase he gets a message to do so. 

`Note:`
For now, I didn’t categorise the products (for example in categories like watches, clothes, shoes, events). Reason is that this is an educational project and creating0 a number of products per category would be a lot of work that isn’t important for the learning outcome. Depending on the number of products it could be better to categorise them, especially to separate the race events from the products.

However the category (or product_type as I named it in the Model) is important for the size selection: with events and watches this is not applicable, shoes get a size of 40, 41 etc, and clothes S, M, L, etc. This selection appears depending on which category the product belongs to.

- **Cart (only if logged-in)**/
On the top of the page, the total price of the products in the cart is given, with buttons to return to the store (Discounts) or to the Checkout. Below, the products in the Cart are specified with the following info: name, size, price, the date until the price is valid, an image of the product, the amount of that products are being purchased, and additional information. It’s again possible to adjust the amount of products, or to remove the product from the Cart.
 
- **Checkout (only if logged-in)**/
On the top of the page, the total price of the products is given, along with a button that sends the user back to the Cart. 

Below, the products that are being purchased are shown, again including the name, size, price, date until the price is valid, an image, the amount of that product that is ordered, and the price per product.

Below the products there is the payment form. After submitting the payment, the user gets a message that he successfully (or not) purchased the products, and he is redirected to the products page. 

- **Inspiration**/
Introduces four different sections: Exercice & Injuries, Routes & Destinations, Health & Food, Stories. For now I only worked-out Routes & Destination. Reason is that this is an educational project and writing a certain number of articles per section would be a lot of work that isn’t important for the learning outcome. 

Every section introduces the articles that are written and the user can read the complete article by clicking the ‘read more’ button. Every article shows the writer, the number of times the article is read (nice statistic for the advertisers) and a button to get the user back to the section. I’ve only written a part of 2 articles, for the same reason as mentioned above, including a fictional advertisement. 

- **Forum**/
Shows the posts of bloggers, ordered by date. Every post shows the name of the author, a thumbnail of his profile picture, the number of views, the date/time the post was created and the first few lines of the post, with a read more button. Only if the user is logged-in the name of the author is clickable, linking to his/her profile page. 

After clicking the ‘read more’ button, the complete post shows, including the same information as mentioned above and, optionally, a picture that is uploaded by the author. There is also a ‘back to forum’ button.
The author of a specific post, and the admin will see additional buttons to edit or delete the post.

- **Add Post (only if logged-in)**/
Shows a form. If filled-out and submitted a new post is created and the user is redirected to the forum, showing his newly created post on top. 

- **Edit Post (only if logged-in and author of that specific post or admin)**/
Shows the same form as Add Post, now filled-out with the earlier posted content. User can edit this and submit in the same way as with Add Post. 

- **Delete Post (only if logged-in and author of that specific post or Admin)**/
Shows a small message, asking if the user is certain to delete the post. If confirmed, post is deleted and user is returned to Forum, if cancelled user is returned to the post.
(Your post is deleted)

- **User Profiles (only if logged-in)**/
Shows a list of all user profiles, with a thumbnail of the profile picture, user-name, first and last name, age and residence.

There’s also a ‘contact user’ button. This will lead to a form that a user can fill out. The message (including an optional picture) will be send to the profile page of the user that is contacted, obviously only readable by that user. 

On top of the page there’s a search functionality, much like that on the Events page. You can find a profile, searching on first name, last name or location. There’s also a reset button.

If no results are found  a message “No profiles found” appears.

- **My Profile (only if logged-in)**/
Shows the basic dates the user filled out upon registering (first and last name, location, email, gender, age and an optional profile picture (if a user chooses not to upload a picture an icon of a runner is shown here).

Below the personal introduction that the user submitted is shown. There are buttons to edit all this information or to delete the complete profile. There is also a button to create a new post,so that a user can for example create different entrances on his profile page (date of the entrance is published, creating a small diary if you will, ordered by date). Again, these additional posts can be deleted.

There is also a section with Personal Messages: messages the user received from other users. The user is able to delete these messages.

- **Register (only if not logged-in)**/
When a user is not logged in, the navigation bar shows a link to the registration page. On top of the form there is a link to the sign in page, for when the user already has an account. 
The form contains: Username, Email address, Password, Password Confirmation, First name, Last name, Repeat email, Gender, Age the possibility to upload a picture and a field to write a short introduction. 
Only the gender, picture upload and the personal introduction are not required.

If the form is filled in, the user is logged in and taken to his profile, showing the message “You have successfully registered and are logged in”.
When a required field is not filled-in, a user name already exists or the password confirmation is incorrect the user receives warnings. 	

- **Login (only if not logged-in)**/
Allows the user with an account to login. User can also request a new password, or can go the registration page when he is a new. 

- **Reset Password**/
If the user has forgotten his password he can request an email and after clicking on the link in the email change his password.

- **Logout (only if logged-in)**/
Allows the user to log out.


### <a name="features-left-to-implement"></a>Features left to Implement

- **Events:**
	-   Maps showing the route of the race. This could be done with the Google Maps API.
	-   A nice photographic presentation of the races, possibly with thumbnails / slider. This should be the same functionality as the presentation of the products (see below).

- **Discounts:**
	-   Categorising the products (for example in categories like watches, clothes, shoes, events).
	-   Possibly a search functionality to search for a specific product. This would depend on how big the store will eventually get (the main idea is to present a small amount of products from the larger store that have a nice discount for only one week), so it might not be necessary to have a search functionality because there is only a limited amount of products.
	-   The ability to select and purchase the products in other colours.
	-   Clickable thumbnails to show the product from various angels / viewpoints.
	-   Pagination if there are many products for sale. 

- **Inspiration**
	-   Now, all articles of a certain category (for example Exercise & Injuries, Routes & Destinations) are introduced on the same page. As the number of articles grow, they should be further categorised and the user should be able to select rapidly the topic of interest. The category Exercise & Injuries could be ordered by body parts for example and Routes & Destinations by region and/or distance of the route, so that the user can find easily the information he wants.

- **Community:**
	-   As the number of posts grow, they should be organised by topic and the user should be able to search by topic. Logically this would be the same technology as on the Inspiration page. 
	-   A chat room for members could be implemented later.

- **Public profile / Events**
	-   It would be nice to see which users will participate in which events and later on publish the results of the users. This can be both done in the calendar, and on the public profile of the user. Obviously the user should agree, because of privacy regulations.


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

