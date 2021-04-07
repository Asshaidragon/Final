import cherrypy
from Data import *


class Requests:
    def GET(self, username=None, department=None):
        users = all_users()
        data1 = []
        data2 = []
        if username == None:
            for user in users:
                data1.append(users[user])
        else:
            for user in users:
                if username in users[user]['username']:
                    data1.append(users[user])
        if department == None:
            for user in users:
                data2.append(users[user])
        else:
            for user in users:
                if department == users[user]['department']:
                    data2.append(users[user])
        data3 = []
        for item in data1:
            if item in data2:
                data3.append(item)
        return 'data: %s' % data3


class Department:
    def GET(self):
        users = all_users()
        data1 = []
        for department in users:
            user = users[department]
            user = user['department']
            data1.append(user)
        data1 = list(set(data1))
        return 'departments: %s' % data1
    exposed = True



if __name__ == '__main__':
    cherrypy.tree.mount(
        Requests(), '/users', {
            '/':
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    cherrypy.tree.mount(
        Department(), '/department', {
            '/':
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
