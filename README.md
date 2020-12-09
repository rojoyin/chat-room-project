# Chat room project
This project creates a chatroom application and a bot that queries the close price of stocks for a company. For now, there is support for only one chatroom and it **MUST** be called 'default'.

## What is inside the repo?
  - app: Contains the code for the chat rooms management
  - bot: Contains the code for managing the queries of stock closing prices. The only supported command is "/stock=stock_code"
  - consumers: This includes the code for fetching the responses for the previous queries.
  - docker-compose.yml: Contains the specifications for managing the containers of each project, as well as the setup of redis server that will be used as message broker.
  - Other files related to django framework, git and python dependencies.

## How does it work?
  1. Clone the repository
  2. Ensure you are at the root folder of the project, and issue the commands:
```
foo@bar:~$ docker-compose build
foo@bar:~$ docker-compose up
```
  3. In other terminal in the same root folder of the repository, issue the command:
```
foo@bar:~$  docker-compose run --rm app sh -c "python manage.py migrate"
```
this will apply the migrations contained in the project, generating the tables and schemas as defined.

  4. To be able to login, please go [here](http://localhost:8000/login/) and you can signup [here](http://localhost:8000/signup/). Mind the specifications of password and user creation.
  5. Once you login, you will be redirected to the defatult chatroom.