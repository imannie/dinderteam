# Milestone 2

## HTML & CSS Click-through



### Find button
Users can fill out information and click the Find button from the home page, to navigate to the swiper page and start swipe
![](https://raw.githubusercontent.com/imannie/dinderteam/master/Milestones/img/clickthrough/startfind.png)

### Category icon
Users can also click the icons from category list from the home page, to navigate
to the swiper page and start swipe until they get 3 favorites at a time
![](https://raw.githubusercontent.com/imannie/dinderteam/master/Milestones/img/clickthrough/category.png)

### Red and Green arrow (aka "No" and "Maybe")
Click Red for skip (No) and click Green for save (Maybe). Each time the user makes a decision, a count is incremented and a new resturant is displayed. Then the "maybe counter" = 3, the page will navigate to the next step of the process.

Opening the link in the verification email will bring them to a confirmation 
page.
![](https://raw.githubusercontent.com/imannie/dinderteam/master/Milestones/img/clickthrough/swiper.png)


### Features clickthrough
Click to the photo to navigate to detail page
If user want to keep searching more option, then click keep swiping button
![](https://raw.githubusercontent.com/imannie/dinderteam/master/Milestones/img/clickthrough/featured.png)

### Listing overview
![](https://raw.githubusercontent.com/imannie/dinderteam/master/Milestones/img/clickthrough/listing.png)


### Detail overview 
Users will navigate to this page whenever they click to tho photo of the business
![](https://raw.githubusercontent.com/imannie/dinderteam/master/Milestones/img/clickthrough/detail.png)

## Wireframes
Wireframes of the front-end design we are striving for.
Refer to the drawing "flow_diagram_showing_db_read_write.jpg" for the flow between pages and database Create, Read and Delete operations as the site is traversed.
### Homepage
This is the welcome screen where the site is explained and the user filters are set.
![]()

### Swipe page
The Swipe page is the place users will do their primary interaction with the app. Each time this page is loaded, an API call is made to Yelp and a new resturant matching the search filters is retrieved. If the user swipes "no," we will either discard this data, or timer permitting, add the Yelp ID to a list of shown pages so that we prevent the possibility of a user being shown the same resturant more than once in a single session.

If user swipes "maybe," then the resturant data is written to the database. A "maybe_counter" is checked at this point and if maybe_counter == 3, then we jump to the details page showing their top picks, or if we don't have time to finish that, we choose one resturant at random from their top picks and jump to Detail Overview page.
![]()

### Feature page

![]()

### Listing Page

![]()

### Detail page
Initially, this page is accessible only when the maybe_counter hits the limit. A future enhancement could allow access to this page to help the user decide between no and maybe.
![]()

## Backend Concepts
Our App uses the Yelp Fusion API to retrieve resturant data filtered by some user criteria, such as city, price, type of food, etc. Our database model will exercise CR&D, as we must create data, read it and delete it (the drawing "flow_diagram_showing_db_read_write.jpg"). There is no current need for data updating in our initial design. We chose to have users interact with the site only as guests. If we had user login, then Update to data would be added to the design. 
