class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def push(self, node):
        self.queue1.append(node)
    def pop(self):
        if len(self.queue1) == 0:
            return None
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop())
        self.queue2, self.queue1 = self.queue1, self.queue2
        return self.queue2.pop()

if __name__=='__main__':
    times=5
    testList=list(range(times))
    testStock=Solution()
    for i in range(times):
        testStock.push(testList[i])
    print(testList)
    for i in range(times):
        print(testStock.pop(),',',end='')  
