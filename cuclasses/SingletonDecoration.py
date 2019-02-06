from functools import wraps
def singleton(cls):
    """装饰器,被装饰的类为单例模式"""
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance
