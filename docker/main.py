import ezrpy

if __name__ == '__main__':
    app = ezrpy.App('api')
    app.add_resource('countries')
    app.run()

