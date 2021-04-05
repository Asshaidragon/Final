import cherrypy

songs = {
    '1': {
        'name': 'Песня1',
        'age': 'Петя'
    },
    '2': {
        'name': 'Песня2',
        'age': 'Вася'
    }
}


class Songs:
    def GET(self, id=None):
            if id == None:
                return ("All songs: %s" % songs)
            elif id in songs:
                song =songs[id]
                return ("Here's your song: %s" % songs[id])
            else:
                return ("No songs: %s" % id)
        exposed = True

        # data1 = []
        # data2 = []
        # if name == None:
        #     data1 = songs
        # else:
        #     for user in songs:
        #         if name == songs[user]["name"]:
        #             data1.append(user)
        # if age == None:
        #     data2 = songs
        # else:
        #     for user in songs:
        #         if age == songs[user]["age"]:
        #             data2.append(user)
        # data3 = []
        # for item in data1:
        #     if item in data2:
        #         data3.append(item)
        # return "Привет"
        # return ('data: %s' % data3)


    #     if id == None:
    #         return ("All songs: %s" % songs)
    #     elif id in songs:
    #         song =songs[id]
    #         return ("Here's your song: %s" % songs[id])
    #     else:
    #         return ("No songs: %s" % id)
    # exposed = True


if __name__ == '__main__':
    cherrypy.tree.mount(
        Songs(), '/api/songs', {
            '/':
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()