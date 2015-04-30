Flask-SQLAlchemy-App
====================
Python application using Flask and SQLAlchemy. This application exposes GET, POST, PUT, DELETE APIs that talk to MySQL database.

** How to start server:
----------------------

python app/message.py



** Examples:
------------

curl "http://127.0.0.1:5000/messages/3" 

curl "http://127.0.0.1:5000/messages"

curl "http://127.0.0.1:5000/messages" -X POST -H "content-type:application/json" -d '{"message":"New message"}'

curl "http://127.0.0.1:5000/messages/7" -X PUT -H "content-type:application/json" -d '{"message":"Edited message"}'

curl "http://127.0.0.1:5000/messages/7" -X DELETE -H "content-type:application/json" 
