import  cherrypy

songs = {
    '1' : {
        'Название1' : 'Песня1',
        'Артист1' : 'Петя'
    },
    '2' : {
        'Название2' : 'Песня2',
        'Артист2' : 'Вася'
    }
}

class Songs:
    exposed = True

if __name__ == '__main__':
    cherrypy.tree.mount(
        Songs(), '/api/songs', {
            '/' :
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )