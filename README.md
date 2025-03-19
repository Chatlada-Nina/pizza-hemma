# BKK Coffee Corner

![The website shown on a variety of screen sizes](/documentation/readme/screen-responsive.png)

[View Live Website here.](https://pizza-hemma-4a540b28342f.herokuapp.com/)

[GitHub Repo](https://github.com/Chatlada-Nina/pizza-hemma)

**Welcome to Pizza Hemma Restaurant!!**

**Pizza Hemma Restaurant** The purpose of the Pizza Hemma website is to provide an inviting and heartfelt space that reflects the cozy, home-like atmosphere of the pizzeria. It aims to share the story of Pizza Hemma’s cherished traditions, highlighting its use of high-quality ingredients and affordable, delicious pizzas crafted with love. The website serves as a bridge between the restaurant and customers by offering essential information such as the menu, prices, and contact details while also fostering a sense of community through customer testimonials and interactive features. For the owner, it is a tool to engage with the local community, build loyalty, and showcase the unique qualities that make Pizza Hemma a beloved dining destination.

![GitHub last commit](https://img.shields.io/github/last-commit/Chatlada-Nina/BKK-Coffee-Corner?color=brown&style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/chatlada-nina/BKK-Coffee-Corner?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/chatlada-nina/BKK-Coffee-Corner?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/chatlada-nina/BKK-Coffee-Corner?color=yellow&style=for-the-badge)
![W3C Validation](https://img.shields.io/w3c-validation/html?targetUrl=https%3A%2F%2Fbkk-coffee-corner-f07d5b0b8233.herokuapp.com%2F&style=for-the-badge)

## CONTENTS

- [UX - User Experience](#ux)

  - [Colours Theme](#colours-theme)
  - [Typography](#typography)
  - [Wireframes](#wireframes)
  - [Data Schema](#data-schema)
  - [User stories](#user-stories)
  - [Agile Development](#agile-development)

- [Features](#features)

  - [Navigation Bar](#navigation-bar)
  - [Home page](#home-page)
  - [About us page](#about-us-page)
  - [Menu page](#menu-page)
  - [Cart page](#cart-page)
  - [checkout page](#checkout-page)
  - [Reviews page](#review-page)
  - [Sign up page](#sign-up-page)
  - [Sign in page](#sign-in-page)
  - [Contact page](#contact-page)
  - [Profile page](#profile-page)
  - [The Footer](#the-footer)
  - [Custom Error Handler page](#custom-error-handler-page)
  - [Features left to implement](#features-left-to-implement)

- [Testing](#testing)

- [Deployment & Local deployment](#deployment-&-Local-deployment)

  - [Deployment](#deployment)
  - [Local Deployment](#local-deployment)

- [Credits](#credits)
  - [Content](#contents)
  - [Media](#media)
  - [Code](#code)
  - [Acknowledgments](#acknowledgments)

## UX

### User’s Goal

Users want to explore and connect with the restaurant in their local area which is in Gothenburg in this website,They want to learn about the story and values behind Pizza Hemma, browse the menu to find their favorite pizza, check prices, or gather practical information like location and opening hours. Some users aim to order online, make a contact, or even share their own experiences on the reviews page and get some exclusive offering.

### Owner’s Goal

The site owner aims to enhance the restaurant's visibility and attract more customers by showcasing its unique qualities, such as traditional recipes, affordable prices and love behind each pizza. The owner seeks to grow Pizza Hemma’s reputation as a beloved, home-like destination while fostering loyalty and trust among customers in the local area.

### Colours Theme

The Pizza Hemma page is a local user-friendly restaurant website. The main colours I chose are Green and Red, Green represents freshness, natural ingredients, and health. Red is known to stimulate appetite and create a sense of warmth, passion, and excitement, food-focused environment. It draws attention and makes the space feel vibrant and welcoming. Both colors highlights the use of high-quality, fresh ingredients in the pizzas. Moreover, I used [WebAIM:Contrast Checker](https://webaim.org/resources/contrastchecker/) to check the contrast of my colours to ensure they are easy to read for users.

![The colour theme of the website](/documentation/readme/color-theme.png)

### Typography

I used [Alfa Slab One](https://fonts.google.com/specimen/Alfa+Slab+One) pairing with [Chivo](https://fonts.google.com/specimen/Chivo) referred to [Creatopy-Goole Fonts Pairings](https://www.creatopy.com/blog/google-font-pairings/) Chivo have details that make the text look remarkable but not steal the spotlight from Alfa Slan One designed for a title with great personality that is meant to be seen.

Additionally, I use [Font Awesome](https://fontawesome.com/) for icons to make the site casual and friendly and for my social media icons in the footer to help users quickly and easily identify my social media sites.

### Wireframes

[Homepage 1](/documentation/wireframe/homepage1.png)

[Homepage 2](/documentation/wireframe/homepage2.png)

[About page](/documentation/wireframe/about-page.png)

[Menu page](/documentation/wireframe/menu-page.png)

[Reviews page 1](/documentation/wireframe/reviews-page1.png)

[Reviews page 2](/documentation/wireframe/reviews-page2.png)

[Profile page 1](/documentation/wireframe/profile-page1.png)

[Profile page 2](/documentation/wireframe/profile-page2.png)

[Checkout page](/documentation/wireframe/checkout-page.png)

[Sign up page](/documentation/wireframe/signup-page.png)

[Sign in page](/documentation/wireframe/signin-page.png)

[Contact page](/documentation/wireframe/contact-page.png)

[Mobile Screen page 1](/documentation/wireframe/mobile-screen1.png)

[Mobile Screen page 2](/documentation/wireframe/mobile-screen2.png)

### Data Schema

I used [Lucidchart](https://www.lucidchart.com/pages) for my data plan. The data schema for the Pizza Hemma Restaurant website is structured using a relational model, as illustrated in the Entity Relationship Diagram (ERD) provided. Below is an Entity Relationship Diagram that shows the key models and their fields:

![Entity Relationship Diagram (ERD)](documentation/readme//er-diagram.png)

### User stories

1. As a new user, I can create an account so that I can save my personal details and preferences for a personalized experience.
2. As a user, I can log in and log out so that I can securely access my account and order history.
3. As a user, I can browse the menu so that I can see all the pizzas and other menus and their details.
4. As a user, I can see my order details and price so that I can make sure my order is correct before payment.
5. As a user, I can add pizzas to my cart or delete pizzas from my cart so that I can place a correct order for my favorite pizzas.
6. As a user, I can choose to place an order online so that I can get my pizza delivered or pick it up from the restaurant.
7. As a user, I can place an order online so that I can get my pizza delivered from the restaurant.
8. As a user, I can make secure payments easily so that I can pay for my order online through the website.
9. As a user, I can receive a receipt after a successful payment so that I have proof of my purchase.
10. As a user, I can update my profile information so that I can keep my contact details and preferences up to date.
11. As a user, I can view my order history so that I can reorder my favorite pizzas easily.
12. As a user, I can subscribe to special offers so that I can receive exclusive deals and promotions.
13. As an admin, I can add new pizzas and ingredients to the menu so that I can keep the menu up to date with new offerings.
14. As an admin, I can manage user accounts so that I can assist users with account-related issues and maintain security.
15. As an admin, I can view and manage orders so that I can ensure correctly orders, timely preparation and delivery of pizzas.
16. As an admin, I can view and manage payments so that I can keep track of all transactions and handle any payment issues.
17. As a user, I can leave feedback and reviews for pizzas so that I can share my dining experience and help others make informed choices.
18. As an admin, I can monitor and respond to user feedback so that I can address any issues and improve the restaurant's service.

User Stories and Acceptance Criteria help me ensure each feature meets the desired functionality and user experience.

### Agile Development

This project was designed using Agile methodology, utilising the Project Board and Issues sections in GitHub

- [Project Board](https://github.com/users/Chatlada-Nina/projects/10/views/1)
