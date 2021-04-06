import cherrypy

users = {
    '1': {
        'id': '1',
        'username': 'van',
        'email ': 'van@ya.ru',
        'department ': 'QA',
        'date_joined': '2021.04.01 23:45',
    },
    '2': {
        'name': 'billy',
        'age': '33'
    },
    '3': {
        'name': 'max',
        'age': '99'
    },
    '4': {
        'name': 'max',
        'age': '99'
    }
}


class Requests:
    def GET(self, username=None, department=None):
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
        return ('data: %s' % data3)

    def POST(self, a, b):
        return
    exposed = True

if __name__ == '__main__':
    cherrypy.tree.mount(
        Requests(), '/users', {
            '/':
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
