import web

urls = (
    '/', 'index',
)

movies = [
        {
            'title': 'Forrest Gump',
            'year': 1994,
            },
        {
            'title': 'Titanic',
            'year': 1997,
            },
        ]

render = web.template.render('templates/')

class index:
    def GET(self):
        return render.index(movies)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

