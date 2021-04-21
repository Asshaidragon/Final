This is the final project for the autotest courses in python. 
The meaning of the program is to output from an improvised database a list of users who fit certain filters.

Run docker-compose 
======

Run it as follows:

```
$ docker-compose up
```

You can click on the link to see all the users: 
http://localhost:3000/users

To sort users by name and department use the following construction:
http://localhost:3000/users?username=van&department=QA
If necessary, you can remove one of the filters

To see all available departments use the following link:
http://localhost:3000/department

To sort by department name, use the following:
http://localhost:3000/department?name=Q
