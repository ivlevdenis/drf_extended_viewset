Django Rest Framework Extended ViewSet
======================================


![https://pypi.python.org/pypi/drf_extended_viewset](https://img.shields.io/pypi/v/drf_extended_viewset.svg) ![https://travis-ci.com/ivlevdenis/drf_extended_viewset](https://img.shields.io/travis/ivlevdenis/drf_extended_viewset.svg) ![https://drf-extended-viewset.readthedocs.io/en/latest/?badge=latest](https://readthedocs.org/projects/drf-extended-viewset/badge/?version=latest) ![https://pyup.io/repos/github/ivlevdenis/drf_extended_viewset/](https://pyup.io/repos/github/ivlevdenis/drf_extended_viewset/shield.svg)


Django Rest Framework extension for implement by action serializers, permissions & /etc


**Dependencies**

* Python 3.7+
* Django 2.0+
* Django Rest Framework 3.10+

**Setup**

You can install the library directly from pypi using pip:

`$ pip install drf-extended-viewset`


License
-------
Free software: MIT license


Features
--------

```python
class MyModelViewSet(ExtendedModelViewSet):
    serializer_class_map = {
        'list': ListMyModelSerializer,
        'retrieve': RetrieveMyModelSerializer,
        'update': UpdateMyModelSerializer,
        ...
    }
    permission_classes_map = {
        'list': AllowAny,
        'retrieve': IsAuthenticated,
        'update': (IsOwner | IsAdminUser),
        ...
    }
```

<!-- * TODO -->

Credits
-------

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.



