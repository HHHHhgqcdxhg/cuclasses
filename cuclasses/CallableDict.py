class CallableDict(dict):
    """call时返回自身字典"""
    def __call__(self, *args, **kwargs):
        return self
