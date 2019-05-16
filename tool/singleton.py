def Singleton(cls):
    _instance = {}

    # @wraps(cls)
    def _singlenton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singlenton