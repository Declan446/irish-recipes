# Irish Recipes

**About:** I have based my project on Recipes of Ireland. I plan to create a clear , easy and well structured web application so that 
people of all ages can find geart wholesome Irish Recipes. Users can also add their own recipes to the app and edit existing ones.

**Personal** reason  My personal reason for developing the web application is because of my grandmother. Over the years my grandmother 
has accumulated a lot of great recipes from family and friends. She stores them in an old tin in the kicthen and from time to time she 
lends some of her recipes out to people . Occasionally these great recipes never find their way back to the old tin and my grandmother 
has to under go the strenuous task of trying to located the recipe again. This process could take weeks even months to find and sometimes 
the recipe is lost because just like food people dont last forever. So i thought to myself why not add all these recipe to a 
mongo database and save my grandmother countless hours of searching . Not only would this be a great place to store the recipes it would 
also make it extremely easy to share them with family members overseas.

**Business opportunities:**
* Advertising for food products eg meats and fresh vegetables.
* Advertising for new restaurants in Ireland eg restaurants could add a dish to promote their menu
* Advertising for cooking tools.

**Users benefits**
* Access to great Irish recipes hassel free.
* The ability to edit recipes to their own likes eg add or take ingredients they like.
* They can add and store their own recipes with ease.
* Find great irish restaurants on the top Irish restaurants page.

# UX Design

The first thing i did in regards to *UX design* is make a list of users who might visit my web application.
* Someone who loves to try and cook new recipes.
* Someone who has or created a good irish recipe and would like to share it with the world.
* People who have just returned from a trip to Ireland and loved the food.
* Irish people living overseas and want a tste of home.
* A chef looking for inspiration.
* Restaurant, Hotel and Bar owners looking for great irish recipes.

**Users benefits**
* Users will find great irish recipes on my web application with ease.
* Users can add, edit and delete recipes which on most other is not possible.
* Users can be any age and dont have to be a wizkid because of the very clear and  easy layout out.
* Users can also find great inspiration on this web application.

**Users Stories**
1. As a user and chef, i would like to find recipes that will inspire me 
2. AS a user and mother, i would like to find great recipes with the ingredients and cooking method clearly shown.
3. as a user and grandmother, i would to share my recipes with friends and family with ease.
4. As a user and irish person living overseas, i would like to have access to good wholesome irish recipes.
5. As a user and B&B owner, i would like a site that has irish recipes to recommend to my visiters.
6. As a user and Restaurant owner, i would like to Advertise my business.

# Design

**Theme**
I got my inspiration for my theme from a mini project i did with the *Code Institute*. The mini project was 
thorin and company and in this project they used a bootstrap theme called **Clean Blog**. While using this theme 
in the mini project i found it to be very clear, well structured and easy to navigate. For these reasons i decided 
to use it for my Irish Recipes web application. One major deciding factor for choosing this theme was it was the
only free multi page design on the bootstrap site that i liked. I used a theme because it speeds up the design Process
and leaves less room for errors and display problems. 

**Logo**
For my logo i choose a picture of the *Cliffs Of Moher*. Not only is it one of Irelands most popular and beautiful land marks
, i thing its perfect for the web application because it has the sea(fish recipes) and land (Meat, Vegan recipes) in it. I know 
its a weird way to pick a logo but it makes scene to me.

**Colours**
I only used colour in a very small way in my project. I wanted to keep everything black and white except for the logo and images but for
easy navigation and use i add some colour to key components.
* Blue for the background of the recipe title on the recipes page.
* Blue fot Boad Bia's social media links in the footer.
* Blue for my submit buttons .
* Green for my edit buttons.
* Green for the background for recipes names in the sliders on the home page.
* Red for my Delete buttons.

**Icons**
I used Font Awesome for the icons on my Add Recipe page, Edit page and for the social media links for boad bia in the footer.

**Planning**

1. I decided to create a web application on Irish recipes that users could find, add, edit and delete recipes.
2. I talked to potential users and found out their needs.
3. Users needs are as follows: fast, easy to navigate and clean clear recipes.
4. I then picked my bootstrap theme (**Clean Blog**).
5. Picked my images for my logo (*Cliffs Of Moher*).
6. Decided what my pages were going to be in my navbar (Home, Add Recipe, Recipes, Top Irish Recipes).
7. Picked the features that the web application would have.
8. Designed my wireframes.
9. Picked my recipes and images.
10. Picked my 10 restaurants to feature on the top irish resaurants page.
11. Picked mongo database to hold all my recipes.
12. Then i opened gitpod and started coding.

**Wireframes**
I used Balsamiq cloud to develope my wirefames because i was able to create wirefames for large screen sizes and mobile screen sizes.
Balsamiq cloud is a great tool for creating very professional wireframes.

![Home page](/static/Wireframes/Home.png)
Format: ![Home page](url)

![GitHub Logo](/static/Wireframes/Home-Mobile.png)
Format: ![Home mobile view](url)

![GitHub Logo](/static/Wireframes/Add-recipes.png)
Format: ![Add Recipe page](url)

![GitHub Logo](/static/Wireframes/Add-Recipe-Mobile.png)
Format: ![Add Recipe mobile view](url)

![GitHub Logo](/static/Wireframes/Recipes.png)
Format: ![Recipes page](url)

![GitHub Logo](/static/Wireframes/Recipes-Mobile.png)
Format: ![Recipes mobile view](url)

![GitHub Logo](/static/Wireframes/Top-Irish-Restaurants.png)
Format: ![Top Irish Restaurants](url)

![GitHub Logo](/static/Wireframes/Top-Irish-Restaurants-Mobile.png)
Format: ![Top Irish Restaurants mobile view](url)

The first ideas for the home are located in the static/wireframes 

# Features

**Nav Bar:** The nar bar has four links to the pages of the web application(Home, Add Recipe, Recipes, Top Irish Recipes) 
The nav bar displays as a button when been viewed on a mobile device.

**Footer:** The footer has three links in it to Boad Bia's twitter,facebook and instagram.

**Form:** The form on the add recipes page has six input fields and a submit button.
1. The first feild is a drop down menu that generates data using python to access data from the mongo database.
2. The second is the recipe name.
3. Is image URL.
4. Is Ingredients for your recipe.
5. Is cooking method
6. Is a submit button

When these field are filled in and you click submit the recipe will be added to the recipes mongo database.

**Sliders:** On my home page i have four sliders that have 3 rotating images for the recipes.
* Slider 1 = Irish Meat Recipes.
* Slider 2 = Irish Fish Recipes.
* Slider 3 = Irish Vegan Recipes.
* Slider 4 = Irish Dessert Recipes.

I got the slider from bootstrap.

**Collapsible Accordion** On the recipes page the recipes are displayed in a Collapsible Accordion. The idea for this came from 
another mini project called task manager but i got the one on the recipes page from bootstrap.

**Edit button** Their is a edit button on every recipe created and when clicked it will take you to a edit recipes page.
You can changed any detail of the recipe and submit the changes to mongo database.

**Delete button** A delete button is present on every recipe and when clicked not only will it be deleted from the web application
it will also be deleted from the mongo database.

# Technologies Used
The Irish Recipes Web Application main Technologies used were as follows:
* **Gitpod** was used as the IDE for building Irish Recipes web application.
* **GitHub** was used to store the project remotely and always used to deploy the project while in constrcution before deploying to heroku
* **HTML** was used to structure the web pages.
* **CSS** was used for the styling.
* **Phython** was used for alot of the core funtinality
* **JQuery** was used as part of clean blog functionality.
* **JavaScript** was used to initialize the Collapsible Accordion and the sliders.
* **Mongo DB** was used as the database to store the recipes.
* **Imports** os, json, flask, flask.Pymongo and bson.ojectedid were all imported in to the aap.py file for the functions.
* **Bootstrap themes** was used for the theme.
* **Bootstrap** was used for most of the features and functionality.
* **Font Awesome** was used for the icons.
* **Heroku** was used to deploy the final version of the web application.

**Materialize was a big part of the project in the early stages of but had to be scraped because it was
 conflicting with bootstrap**

 # Testing:
 I tested my web application on google chrome, internet explorer, firefox and safari and found no problems displaying the web application
 in any browser. The web application was also tested on all screen sizes.
* Galaxy S5 = No problems.
* Pixel 2 and 2 XL = No problems.
* Iphone 5 = No problems.
* Iphone 6/7/8 = No problems.
* Iphone 5 = No problems.
* Ipads = No problems

 **Although no problems occured with the final testing of the web application, there were huge problems
  with the web application on mobile sceen views when Bootstrap and Materialize were running together. For this reason Materialize
  was scrapped.Bootstrap was kept because the clean blog theme was used and this is a Bootstrap theme.
  To rectify this problem all Materialize components were removed and replaced with Bootstrap one's.
  Due to these problems the web application took a lot longer then expected but it was a great lesson to learn
  the hard way because i now have a much better understanding of Materialize and Bootstrap frameworks.** 

# Deployment
 



# Credits:
**Content:**

All the Recipes in the app were taking from the BBC good food website.
including recipe name, ingredients and cooking method.
https://www.bbcgoodfood.com/recipes/collection/irish - automatic!
[BBC Good Food](https://www.bbcgoodfood.com/recipes/collection/irish)

All the restaurants reviews for the Top Irish Restaurants page were taking from taste.ie.
http://thetaste.ie/wp/category/top-restaurants-in-ireland/irish-restaurants-cuisine-food/- automatic!
[Taste.ie](http://thetaste.ie/wp/category/top-restaurants-in-ireland/irish-restaurants-cuisine-food/)

**Media:**
All the images for my recipes came from BBC good food website.
https://www.bbcgoodfood.com/recipes/collection/irish - automatic!
[BBC Good Food](https://www.bbcgoodfood.com/recipes/collection/irish)

All the restaurant images for the Top Irish Restaurants page were taking from taste.ie.
http://thetaste.ie/wp/category/top-restaurants-in-ireland/irish-restaurants-cuisine-food/- automatic!
[Taste.ie](http://thetaste.ie/wp/category/top-restaurants-in-ireland/irish-restaurants-cuisine-food/)

The logo image was taking off google after searching pictuers of Ireland.
https://www.planetware.com/pictures/ireland-irl.htm - automatic!
[Cliffs Of Moher](https://www.planetware.com/pictures/ireland-irl.htm)

**Acknowledgements:**
* I received inspiration for the top restaurants page from my mini project *Thorin and company* not only the 
layout but also the code help me display the page.

* I received inspiration for the Collapsible Accordion from the mini project *Task manager* . In the mini
project they use a Materialize Accordion and i used a Bootstrap one .

* I received inspiration for the Bootstrap theme(clean blog) from the mini project *Thorin and company*.