class HashTable():
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h%self.max

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
t = HashTable()
t['march 6'] = 130
t['dec 9'] = 250
t['october 17'] = 279
print(t['dec 9'])


