class LRUCache:
    #[key, value]
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []








        # self.capacity = capacity
        # # self.cache = [0] * capacity
        # self.cache = []

    def get(self, key: int) -> int:

        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                temp = self.cache.pop(i)
                self.cache.append(temp)
                return temp[1]
        return -1







        # for i in range(len(self.cache)):
        #     if self.cache[i][0] == key:
        #         temp = self.cache.pop(i)
        #         self.cache.append(temp)
        #         return temp[1]
        # return -1
        

    def put(self, key: int, value: int) -> None:
        # check if it exists first
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                temp = self.cache.pop(i)
                temp[1] = value
                self.cache.append(temp)
                return

        if len(self.cache) == self.capacity:
            self.cache.pop(0)
        self.cache.append([key, value])












        # for i in range(len(self.cache)):
        #     if self.cache[i][0] == key:
        #         temp = self.cache.pop(i)
        #         temp[1] = value
        #         self.cache.append(temp)
        #         return

        # if self.capacity == len(self.cache):
        #     self.cache.pop(0)
        # self.cache.append([key, value])
        
