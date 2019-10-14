class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.ages = {}
        self.age = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #print 'Getting', key, 'from cache =', self.cache
        if key in self.cache:
            self.age += 1
            #print 'Bumping age to', self.age
            self.ages[key] = self.age
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if len(self.cache) == self.capacity and key not in self.cache:
            (minKey, _) = min(self.ages.items(), key=lambda (k, age): age)
            #print 'Kicking out', minKey
            del self.cache[minKey]
            del self.ages[minKey]
        self.age += 1
        self.ages[key] = self.age
        self.cache[key] = value
        #print 'Putting', key, value, 'for cache =', self.cache



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
