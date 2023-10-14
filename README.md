# Brainstation-Capstone
Initial EDA for Capstone Project: Nutrino 

## Project Nutrino

<p align="center"> 
  
  ![image](https://github.com/RafayKhan2/Brainstation-Capstone/assets/144967604/0facb35c-efe1-4dc9-ba99-2539c86aebb3)

</p>

### Project Overview

#### The Problem Area:
The past decade has seen the individual consumer market become increasingly saturated with online
food delivery apps; their expansion only spurred by the onset of the global pandemic. The growth of
industry giants such as Uber Eats and Skip the Dishes has not only allowed its users access to hundreds if
not thousands of restaurants at their fingertips but also helped the struggling restaurant sector weather
the waves of lockdowns, with many restaurants opting to go entirely delivery based.
While these food delivery apps do segregate restaurants into specific categories (ex; types of cuisines,
dietary restrictions, on sale), they lack detailed specifications and tend to catalogue restaurants
wholistically instead of by individual dishes.
My team intends to use an open-source API database of the most common restaurant offerings as well
as their macro nutrient profile to help recommend offerings which fit into health-conscious consumers’
diet plans.

#### The Users:
I am a home cook with an obsessive desire to control my macros. While I have been able to conform to
that lifestyle throughout my university life, as I entered the workplace the shifting priorities of my day
have led me to rely on my crutch of using Uber Eats more often. While I always try to cross reference my
orders with the macros listed on restaurant websites, the process is often fruitless. My extension for
Uber Eats and other food delivery apps can help health focused individuals make informed decisions by
recommending them specific meals that fit their diet plans and goals.

#### The Big Idea:
Given that users input their daily targets as well as the macro count of food consumed up until that point
in the day, the extension would be able to sample dishes in the users’ surroundings and recommend
dishes based on filters that the user can choose in a hierarchical fashion.
The Impact: What societal or business value do you anticipate your project to add? If possible,
try to quantify the scale of the problem (in dollars, in CO2, in time spent, ...)
With the global health and wellness food market projected to bloom to a trillion dollars by 2026, brands
like Sweet Green and Freshii will likely create brand deals with Uber to jump start this sector of online
food delivery. This will increase not only increase customer acquisition but also create a new niche for
health-centric businesses.

#### The Data:
I will be using three databases for this project: 
1) Nutrionix, which is the world’s largest verified nutrition database with over 209,000 restaurants with macros tracked for every item on the menu. https://www.nutritionix.com/
2) Food.com, which is a open database comprising off over 350,000 dishes indivudals can cook at home all the while being able to track their macros
https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews
3) Local resturant data which will be scraped from food delievry apps. This will initially start with Uber Eats and then extend into other popular food delivery apps.
