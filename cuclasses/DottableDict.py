class DottableDict(dict):
    """能用点 '.' 访问的dict"""

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    if isinstance(v, dict):
                        v = DottableDict(v)
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                if isinstance(v, dict):
                    v = DottableDict(v)
                self[k] = v

    def __getattr__(self, attr):
        v = self.get(attr)
        if not v is None:
            return v
        else:
            newDottableDict = DottableDict()
            self.__setitem__(attr,newDottableDict)
            return newDottableDict


    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super().__delitem__(key)
        del self.__dict__[key]

    def __missing__(self, key):
        return super().__setitem__(key, DottableDict())
