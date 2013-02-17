class memoize(object):
    def __init__(self, function):
        self._function = function
        self._cacheName = '_cache__' + function.__name__

    def __get__(self, instance, cls=None):
        self._instance = instance
        return self

    def __call__(self, *args):
        cache = self._instance.__dict__.setdefault(self._cacheName, {})
        if cache.has_key(args):
            return cache[args]
        else:
            object = cache[args] = self._function(self._instance, *args)
            return object
