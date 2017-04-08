Restpy
======

Simple REST Python library for prototypes.

## Example of usage

Define an API for markers:

```python
# markers.py
import restpy


if __name__ == '__main__':
    app = restpy.App('api')
    markers = app.add_resource('markers')
    app.run()

```

Execute it:

```
$ python markers.py
Create route for ideas_list: /api/ideas/
Create route for ideas_post: /api/ideas/
Create route for ideas_get: /api/ideas/<pk>/
Create route for ideas_delete: /api/ideas/<pk>/
Create route for ideas_put: /api/ideas/<pk>/
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Done!

## Using custom actions

Obtaining a range of markers:

```python
import restpy


class Markers(restpy.Resource):
    def on_create(self):
        self.register(self.near, 'POST')

    def near(self, body):
        lat, lng, delta = body['lat'], body['lng'], body['delta']

        def selector(marker):
            d_lng = marker['lng'] - lng
            d_lat = marker['lat'] - lat
            return (d_lng * d_lng + d_lat * d_lat) < delta * delta

        return self.objects.filter(selector)


if __name__ == '__main__':
    app = restpy.App('api')
    app.add_resource(Markers)
    app.run()
```
