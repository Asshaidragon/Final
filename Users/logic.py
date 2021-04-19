import cherrypy
# from Users.Data import all_users
from Data import all_users



class Requests_users:
    def GET(self, username=None, department=None):
        users = all_users()
        data1, data2, data3 = [],[],[]
        if username == None:
            for user in users:
                data1.append(users[user])
        else:
            for user in users:
                if username.lower() in users[user]['username'].lower():
                    data1.append(users[user])
        if department == None:
            for user in users:
                data2.append(users[user])
        else:
            for user in users:
                if department.lower() == users[user]['department'].lower():
                    data2.append(users[user])
        for item in data1:
            if item in data2:
                data3.append(item)
        return 'data: %s' % data3
    exposed = True


class Requests_department:
    def GET(self, name=None):
        users = all_users()
        data1 = []
        data2 = []
        for department in users:
            user = users[department]
            user = user['department']
            data1.append(user)
        data1 = list(set(data1))
        if name == None:
            return 'departments: %s' % data1
        else:
            for i in data1:
                if name.lower() in i.lower():
                    data2.append(i)
            return 'departments: %s' % data2
    exposed = True
# Дописать фильтр для департементов


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': "0.0.0.0", 'server.socket_port': 80})
    cherrypy.tree.mount(
        Requests_users(), '/users', {
            '/':
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    cherrypy.tree.mount(
        Requests_department(), '/department', {
            '/':
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
