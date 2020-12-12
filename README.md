# Django Project
A web project in Python demonstrating use of the Django framework. The project encompasses both a blog and a projects section as well as an 'About' page.

The website could be purposed for a variety of uses. For example, a developer wishing to showcase his projects alongside a personal blog.

## Commands
The main command for running the server is as below:

```
python manage.py runserver
```

## Users & User Access
The project contains functionality for user access including registration and login pages. Some content only displays if the user is signed in. For example, the links for login and logout are dependent on whether the user is logged in or not. The links for the members area is also only available to view when logged in. 

The details for the test administrator account is as below:
```
andy-test
test1
```
## Projects
The main project page, which is also the hompage, displays a description of each project along with a small image. Each individual project page displays the full image and more detail on the project.

## Blog
The main blog page displays a summary of all the currently uploaded blog posts. Each individual blog post displays post content along with a comment section, which visitors can add to.

Administrators can add new blog posts through the administration section.

## About
There is largely static About page that is intended to display information about the author.

