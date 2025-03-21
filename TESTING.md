# Testing

Return back to the [README.md](README.md) file.

## CONTENTS

- [AUTOMATED TESTING](#automated-testing)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)
  - [Python](#python)
  - [Lighthouse](#lighthouse)
- [MANUAL TESTING](#manual-testing)
  - [Responsiveness](#responsiveness)
  - [Defensive Programming](#defensive-programming)
  - [User Story Testing](#user-story-testing)
- [SOLVED BUGS](#solved-bugs)

## AUTOMATED TESTING

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page             | Screenshot                                                         | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Home             | ![screenshot](documentation/testing/w3c-html/homepage.png)         | The error occurs because the aria-current is empty and should be used when the link represents the current page. Since this is a standard navigation link and does not serve that purpose, the attribute was unnecessary and has been removed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| About            | ![screenshot](documentation/testing/w3c-html/about.png)            | The warning is about the article element is missing a heading inside it. To fix this, I move h2 and add p element inside the article element to properly associate them with the content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Menu             | ![screenshot](documentation/testing/w3c-html/menu.png)             | The warning is about the type of javascript attribute is unnecessary in modern HTML5 and no longer required so I have removed it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Contact Us       | ![screenshot](documentation/testing/w3c-html/contact.png)          | Pass: No Errors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Cart             | ![screenshot](documentation/testing/w3c-html/cart.png)             | Pass: No Errors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Checkout         | ![screenshot](documentation/testing/w3c-html/checkout.png)         | 1.) The warning occurs because XML doesn't allow consecutive hyphens(--) in comments so I replaced them with a valid format. 2.) The error occurs because the placeholder attribute is not valid for the select element in HTML. To resolve this, I removed the placeholder from the delivery_method field so that it no longer has a placeholder. Additionally, I updated the loop to bypass adding the placeholder for the delivery_method field while preserving the existing logic for other fields. This modification allows Django to render the default select dropdown as intended. 3.) The warning is caused by having an empty heading (h1). To improve accessibility for screen readers, I added span with text "Loading...", added class sr-only to keep it visually hidden but still accessible. |
| Checkout Success | ![screenshot](documentation/testing/w3c-html/checkout-success.png) | Pass: No Errors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Reviews          | ![screenshot](documentation/testing/w3c-html/reviews.png)          | This error come from myself copied the code from another part of the site which in this page, doesn't need label for so I have replace label element with p element.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Profile          | ![screenshot](documentation/testing/w3c-html/profile.png)          | The validation error arises from the default Django form rendering engine used by allauth, which generates the HTML automatically. This issue originates from how Django's crispy-forms library renders form errors by default. Since this is not code I have written manually but part of the third-party package’s default behavior, I have chosen to leave it as is, as it does not impact the website’s functionality.                                                                                                                                                                                                                                                                                                                                                                                    |
| Login            | ![screenshot](documentation/testing/w3c-html/login.png)            | Pass: No Errors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Logout           | ![screenshot](documentation/testing/w3c-html/signout.png)          | Pass: No Errors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Signup           | ![screenshot](documentation/testing/w3c-html/signup.png)           | The validation error arises from the default Django form rendering engine used by allauth, which generates the HTML automatically. This issue originates from how Django's crispy-forms library renders form errors by default. Since this is not code I have written manually but part of the third-party package’s default behavior, I have chosen to leave it as is, as it does not impact the website’s functionality.                                                                                                                                                                                                                                                                                                                                                                                    |
| Custom Error 404 | ![screenshot](documentation/testing/w3c-html/error404.png)         | Pass: No Errors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Custom Error 500 | ![screenshot](documentation/testing/w3c-html/error500.png)         | Pass: No Errors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file.

| Page      | Screenshot                                                     | Notes           |
| --------- | -------------------------------------------------------------- | --------------- |
| style.css | ![screenshot](documentation/testing/css-validated-results.png) | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files. After inserting /*jshint esversion: 6/, /*global $/, stripe and bootstrap/ at the top of the files no errors were returned.

| File               | Screenshot                                                         | Notes |
| ------------------ | ------------------------------------------------------------------ | ----- |
| menu.js            | ![screenshot](documentation/testing/jshint/menu-js.png)            | Pass  |
| reviews.js         | ![screenshot](documentation/testing/jshint/reviews-js.png)         | Pass  |
| stripe_elements.js | ![screenshot](documentation/testing/jshint/stripe-elements-js.png) | Pass  |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files. No errors were returned:

#### Validation For Pizza Hemma App

| File        | Screenshot                                                              | Notes           |
| ----------- | ----------------------------------------------------------------------- | --------------- |
| asgi.py     | ![screenshot](documentation/testing/python/pizzahemma-app/asgi.png)     | Pass: No Errors |
| settings.py | ![screenshot](documentation/testing/python/pizzahemma-app/settings.png) | Pass: No Errors |
| urls.py     | ![screenshot](documentation/testing/python/pizzahemma-app/urls.png)     | Pass: No Errors |
| views.py    | ![screenshot](documentation/testing/python/pizzahemma-app/views.png)    | Pass: No Errors |
| wsgi.py     | ![screenshot](documentation/testing/python/pizzahemma-app/wsgi.png)     | Pass: No Errors |

#### Validation For about App

| File      | Screenshot                                                       | Notes           |
| --------- | ---------------------------------------------------------------- | --------------- |
| admin.py  | ![screenshot](documentation/testing/python/about-app/admin.png)  | Pass: No Errors |
| apps.py   | ![screenshot](documentation/testing/python/about-app/apps.png)   | Pass: No Errors |
| models.py | ![screenshot](documentation/testing/python/about-app/models.png) | Pass: No Errors |
| urls.py   | ![screenshot](documentation/testing/python/about-app/urls.png)   | Pass: No Errors |
| views.py  | ![screenshot](documentation/testing/python/about-app/views.png)  | Pass: No Errors |

#### Validation For Contact App

| File      | Screenshot                                                         | Notes           |
| --------- | ------------------------------------------------------------------ | --------------- |
| admin.py  | ![screenshot](documentation/testing/python/contact-app/admin.png)  | Pass: No Errors |
| apps.py   | ![screenshot](documentation/testing/python/contact-app/apps.png)   | Pass: No Errors |
| forms.py  | ![screenshot](documentation/testing/python/contact-app/forms.png)  | Pass: No Errors |
| models.py | ![screenshot](documentation/testing/python/contact-app/models.png) | Pass: No Errors |
| urls.py   | ![screenshot](documentation/testing/python/contact-app/urls.png)   | Pass: No Errors |
| views.py  | ![screenshot](documentation/testing/python/contact-app/views.png)  | Pass: No Errors |

#### Validation For Home App

| File      | Screenshot                                                      | Notes           |
| --------- | --------------------------------------------------------------- | --------------- |
| admin.py  | ![screenshot](documentation/testing/python/home-app/admin.png)  | Pass: No Errors |
| apps.py   | ![screenshot](documentation/testing/python/home-app/apps.png)   | Pass: No Errors |
| models.py | ![screenshot](documentation/testing/python/home-app/models.png) | Pass: No Errors |
| urls.py   | ![screenshot](documentation/testing/python/home-app/urls.png)   | Pass: No Errors |
| views.py  | ![screenshot](documentation/testing/python/home-app/views.png)  | Pass: No Errors |

#### Validation For Reviews App

| File      | Screenshot                                                         | Notes           |
| --------- | ------------------------------------------------------------------ | --------------- |
| admin.py  | ![screenshot](documentation/testing/python/reviews-app/admin.png)  | Pass: No Errors |
| apps.py   | ![screenshot](documentation/testing/python/reviews-app/apps.png)   | Pass: No Errors |
| forms.py  | ![screenshot](documentation/testing/python/reviews-app/forms.png)  | Pass: No Errors |
| models.py | ![screenshot](documentation/testing/python/reviews-app/models.png) | Pass: No Errors |
| urls.py   | ![screenshot](documentation/testing/python/reviews-app/urls.png)   | Pass: No Errors |
| views.py  | ![screenshot](documentation/testing/python/reviews-app/views.png)  | Pass: No Errors |

#### Validation For Profiles App

| File      | Screenshot                                                          | Notes           |
| --------- | ------------------------------------------------------------------- | --------------- |
| apps.py   | ![screenshot](documentation/testing/python/profiles-app/apps.png)   | Pass: No Errors |
| forms.py  | ![screenshot](documentation/testing/python/profiles-app/forms.png)  | Pass: No Errors |
| models.py | ![screenshot](documentation/testing/python/profiles-app/models.png) | Pass: No Errors |
| urls.py   | ![screenshot](documentation/testing/python/profiles-app/urls.png)   | Pass: No Errors |
| views.py  | ![screenshot](documentation/testing/python/profiles-app/views.png)  | Pass: No Errors |

#### Validation For Cart App

| File        | Screenshot                                                        | Notes           |
| ----------- | ----------------------------------------------------------------- | --------------- |
| apps.py     | ![screenshot](documentation/testing/python/cart-app/apps.png)     | Pass: No Errors |
| contexts.py | ![screenshot](documentation/testing/python/cart-app/contexts.png) | Pass: No Errors |
| urls.py     | ![screenshot](documentation/testing/python/cart-app/urls.png)     | Pass: No Errors |
| views.py    | ![screenshot](documentation/testing/python/cart-app/views.png)    | Pass: No Errors |

#### Validation For Checkout App

| File               | Screenshot                                                                   | Notes           |
| ------------------ | ---------------------------------------------------------------------------- | --------------- |
| apps.py            | ![screenshot](documentation/testing/python/checkout-app/apps.png)            | Pass: No Errors |
| forms.py           | ![screenshot](documentation/testing/python/checkout-app/forms.png)           | Pass: No Errors |
| models.py          | ![screenshot](documentation/testing/python/checkout-app/models.png)          | Pass: No Errors |
| signals.py         | ![screenshot](documentation/testing/python/checkout-app/signals.png)         | Pass: No Errors |
| urls.py            | ![screenshot](documentation/testing/python/checkout-app/urls.png)            | Pass: No Errors |
| views.py           | ![screenshot](documentation/testing/python/checkout-app/views.png)           | Pass: No Errors |
| webhook-handler.py | ![screenshot](documentation/testing/python/checkout-app/webhook-handler.png) | Pass: No Errors |
| webhooks.py        | ![screenshot](documentation/testing/python/checkout-app/webhooks.png)        | Pass: No Errors |

#### Validation For Menu App

| File      | Screenshot                                                      | Notes           |
| --------- | --------------------------------------------------------------- | --------------- |
| apps.py   | ![screenshot](documentation/testing/python/menu-app/apps.png)   | Pass: No Errors |
| forms.py  | ![screenshot](documentation/testing/python/menu-app/forms.png)  | Pass: No Errors |
| models.py | ![screenshot](documentation/testing/python/menu-app/models.png) | Pass: No Errors |
| urls.py   | ![screenshot](documentation/testing/python/menu-app/urls.png)   | Pass: No Errors |
| views.py  | ![screenshot](documentation/testing/python/menu-app/views.png)  | Pass: No Errors |

### Lighthouse

I've audited my deployed project with the Lighthouse tool to identify any significant issues. Overall, I'm pleased with the results. However, it's worth noting that the 'Best Practices' score is notably affected by the Cloudinary images.

| Page       | Size    | Screenshot                                                   |
| ---------- | ------- | ------------------------------------------------------------ |
| Home       | Desktop | ![screenshot](documentation/testing/lighthouse/home.png)     |
| About      | Desktop | ![screenshot](documentation/testing/lighthouse/about.png)    |
| Menu       | Desktop | ![screenshot](documentation/testing/lighthouse/menu.png)     |
| reviews    | Desktop | ![screenshot](documentation/testing/lighthouse/reviews.png)  |
| checkout   | Desktop | ![screenshot](documentation/testing/lighthouse/checkout.png) |
| My Profile | Desktop | ![screenshot](documentation/testing/lighthouse/profile.png)  |
| Contact us | Desktop | ![screenshot](documentation/testing/lighthouse/contact.png)  |
| Sign In    | Desktop | ![screenshot](documentation/testing/lighthouse/signin.png)   |
| Sign Up    | Desktop | ![screenshot](documentation/testing/lighthouse/signup.png)   |
