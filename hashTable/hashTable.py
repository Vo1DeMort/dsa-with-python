# NOTE: data is stored by mapping the keys to the value
# as key-value pair

# print(map(ord, 'hello world'))
# print({char: ord(char) for char in 'hello world'})
print(sum(map(ord, 'hello world')))

# NOTE: most of the hash functions are inperfect and face collisions
# meaning a hash function gives the same hash value to more than one string

# NOTE: each position in hash table in called 'slot' or 'bucket'
# WARNING: if the slot is not empty ,collision happens
# so find a free slot from the position of the collision
# which is caleed 'open addressing'

# NOTE: open addressing
# ! probing is searching an alternative position until an unused
# slot in the hash table
# linear probing : adding 1 to the hashed value
# quadratic probing
# double hashing


class HashItem:  # sort of a node to hold key and value pair
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self):
        self.size = 256
        # empty value (none) slots for now
        self.slots = [None for i in range(self.size)]
        self.count = 0
        self.maxLoadFactor = 0.65

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size

    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key == key:
                break
            h = (h+1) % self.size
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item
        self.checkGrowth()

    # NOTE: if the table is about to be full , size can be expand(growth)
    # recommand to expand at 75% of use

    def checkGrowth(self):
        loadfactor = self.count / self.size
        if loadfactor > self.maxLoadFactor:
            print("load factor before growing the has table",
                  self.count/self.size)
            self.growth()
            print('load factor after growing the hash table',
                  self.count/self.size)

    def growth(self):
        newHashTable = HashTable()
        newHashTable.size = 2 * self.size
        newHashTable.slots = [None for i in range(newHashTable.size)]

        for i in range(self.size):
            if self.slots[i] is None:
                newHashTable.put(self.slots[i].key, self.slots[i].value)
        self.size = newHashTable.size
        self.slots = newHashTable.slots

    def get(self, key):
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h+1) % self.size
        return None

    def getQuadratic(self, key):
        pass

    def putQuadratic(self, key, value):
        pass


ht = HashTable()
ht.put('good', 'eggs')
ht.put('better', 'ham')
ht.put('best', 'spam')
ht.put('ad', 'do not')
ht.put('ga', 'collide')
ht.put('awd', 'do i not')
ht.put('fwd', 'does not')
ht.checkGrowth()
