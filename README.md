
# Automation with Python Selenium

> Webscrapping COVID data to display in a Django application

<p align="center">
  <a href="https://www.linkedin.com/in/sergio-hg-pereira/" target="_blank" rel="noopener noreferrer">
    <img alt="Author" src="https://img.shields.io/badge/Author-sergiohgp-%23FF9000">
  </a>
  
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/sergiohgp/GoStack_GoBarber?color=%23FF9000">

  <a href="https://github.com/tiago-web/GoBarber-api/stargazers">
    <img alt="Stars" src="https://img.shields.io/github/stars/sergiohgp/GoStack_GoBarber?color=%23FF9000" />
   </a>

  <a href="https://github.com/tiago-web/GoBarber-api/issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/sergiohgp/GoStack_GoBarber?color=%23FF9000">
  </a>

  <img alt="GitHub" src="https://img.shields.io/github/license/sergiohgp/GoStack_GoBarber?color=%23FF9000">
</p>

<p id="insomniaButton" align="center">
  <a href="https://insomnia.rest/run/?label=GoStack_GoBarber&uri=https%3A%2F%2Fraw.githubusercontent.com%2Fsergiohgp%2FGoStack_GoBarber%2Fmaster%2FInsomnia.json" target="_blank"><img src="https://insomnia.rest/images/run.svg" alt="Run in Insomnia"></a>
</p>

# :pushpin: Table of Contents

* [About the project](#robot-about-the-project)
* [Technologies](#rocket-technologies)
* [Getting Started](#checkered_flag-getting-started)
* [How to contribute](#thinking-how-to-contribute)
* [Found a bug? Missing a specific feature?](#hammer-issues)
* [License](#book-license)



# :robot: About the project

This automation program uses webscraping to get worldwide COVID data and display it in a Django web application.

The data can be edited or even added.

# :rocket: Technologies

Technologies that I used to develop this Automation



- [Python](https://www.python.org)
- [Selinium](https://www.selenium.dev/documentation/en/)
- [Django](https://docs.djangoproject.com/en/3.2/)
- [MongoDB](https://docs.mongodb.com)


# :checkered_flag: Getting Started

### Requirements

- [Selinium](https://www.selenium.dev/documentation/en/)
- [Python](https://www.python.org)
- [MongoDB](https://docs.mongodb.com)

> PS: I recommend using a virtual environment

**Clone the project and access the folder**

```bash
$ git clone https://github.com/sergiohgp/COVID_webscrapping.git && cd COVID_webscrapping
```

**Follow the steps below**

```bash
# Install the dependencies
$ python -m pip intall selenium
$ python -m pip intall django
$ python -m pip intall pymongo

# Make a copy of '.env.example' to '.env'
# and set with YOUR environment variables.
$ cp .env.example .env

# Run the webscraping main file to get the data from google website and populate the database
$ cd src/webscraping
$ python main.py

# Run the application server to start Django app
$ cd ..
$ cd django
$ python manage.py runserver

# Go to the browser and input the url of the port from django server

# Well done, project is started!
```

# :thinking: How to contribute

**Make a fork of this repository**

```bash
# Fork using GitHub official command line
# If you don't have the GitHub CLI, use the web site to do that.

$ gh repo fork sergiohgp/COVID_webscrapping
```

**Follow the steps below**

```bash
# Clone your fork
$ git clone your-fork-url && cd COVID_webscrapping

# Create a branch with your feature
$ git checkout -b my-feature

# Make the commit with your changes
$ git commit -m 'feat: My new feature'

# Send the code to your remote branch
$ git push origin my-feature
```

After your pull request is merged, you can delete your branch

# :hammer: Issues

Feel free to file a new issue with a respective title and description on the [GoBarber-api](https://github.com/sergiohgp/COVID_webscrapping/issues) repository. 
If you already found a solution to your problem, **i would appreciate to review your pull request**!


# :book: License

Released in 2020.
This project is under the [MIT license](https://github.com/sergiohgp/COVID_webscrapping/blob/master/LICENSE).

---


Made by Sergio Pereira [LinkedIn](https://www.linkedin.com/in/sergio-hg-pereira) 🚀
