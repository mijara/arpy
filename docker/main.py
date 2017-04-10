import ezrpy

if __name__ == '__main__':
    app = ezrpy.App('api')
    i = app.add_resource('countries')
    i.objects.create({
        'name': 'Chile',
    })
    app.run()
