# Chat room project
This project creates a chatroom application and a bot that queries the close price of stocks for a company. For now, there is support for only one chatroom and it **MUST** be called 'default'.

## What is inside the repo?
  - app: Contains the code for the chat rooms management
  - bot: Contains the code for managing the queries of stock closing prices. The only supported command is "/stock=stock_code"
  - consumers: This includes the code for fetching the responses for the previous queries.
  - docker-compose.yml: Contains the specifications for managing the containers of each project, as well as the setup of redis server that will be used as message broker.
  - Other files related to django framework, git and python dependencies.

## How does it work?
  1. Clone the repository and create a .env file, following the structure of .env.dev
  2. In other terminal in the same root folder of the repository, issue the command:
```
foo@bar:~$ docker-compose run --rm app sh -c "python manage.py migrate"
```
This will apply the migrations contained in the project, generating the tables and schemas as defined.
  3. Ensure you are at the root folder of the project, and issue the commands:
```
foo@bar:~$ docker-compose build
foo@bar:~$ docker-compose up -d
```
  4. To be able to login, please go [here](http://localhost:8000/login/) and you can signup [here](http://localhost:8000/signup/). Mind the specifications of password and user creation.
  5. Once you log in, you will be redirected to the default chatroom.
  6. To finish the app execution, please use the command:
```
foo@bar:~$ docker-compose down
```
  7. To run the unit tests implemented, please use the command
```
foo@bar:~$ docker-compose run --rm app sh -c "python manage.py test"
```
## ToDo
  - Implement the chat services using [channels](https://channels.readthedocs.io)
  - Add support for CRUD operations on chat rooms, so multiple chat rooms could be managed.
  - Improve price request handling in such a way request reprocess is avoided by marking the corresponding flag accordingly.
  - Create views to manage users and groups.
  - Replace default database by a production database.
  - Customize the default model of User.
