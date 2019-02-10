class NumGetDict(dict):
    def __missing__(self, key):
        if isinstance(key,int):
                l = list(self.keys())
                if key > l.__len__() - 1:
                    raise IndexError("list index out of range")
                else:
                    return self[l[key]]
        else:
            raise ValueError(repr(key))



if __name__ == '__main__':
    a = NumGetDict()
    a["aa"] = 10
    print(a["vv"])
