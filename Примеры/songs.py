import cherrypy

songs = {
    '1': {
        'name': 'van',
        'age': '30'
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

class Songs:
    def GET(self, name=None, age=None):
        data1 = []
        data2 = []
        if name == None:
            for user in songs:
                data1.append(songs[user])
        else:
            for user in songs:
                if name in songs[user]['name']:
                    data1.append(songs[user])
        if age == None:
            for user in songs:
                data2.append(songs[user])
        else:
            for user in songs:
                if age == songs[user]['age']:
                    data2.append(songs[user])
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
        Songs(), '/api/songs', {
            '/':
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()