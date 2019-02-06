class StrKeyDict(dict):
    '''StrKeyDict在查询时把非字符串键转换为字符串'''
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, k,default=None):
        try:
            return self[k]
        except KeyError:
            return default

    def __contains__(self, k):
        ks = self.keys()
        return k in ks or str(k) in ks
