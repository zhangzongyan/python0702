
class Dictclass(dict):
    def __init__(self):
        super(Dictclass, self).__init__()
    def del_dict(self, key):
        self.pop(key)
    def get_dict(self, key):
        if key in self:
            return self[key]
        return "not found"
    def get_key(self):
        return self.keys()
    def update_dict(self, dt):
        #print(self.items())
        #self = dict(self.items()+dt.items())
        self.update(dt)
        return self.values()

d1 = Dictclass()
d1['name'] = "aa"
d1['age'] = 10
d1['sex'] = "male"
d1.del_dict('sex')
print(d1)
print(d1.get_dict('name'))
print(d1.get_key())

d2 = {"sunday":7, "sat":6}
print(d1.update_dict(d2))

d3 = {"吃":"火锅", "man":"强壮"}
d4 = dict(d2, **d3)
print(d4)
