# 1352. Product of the last K numbers - Medium
# Solved without any help, runtime: 36 ms. Beats 60.82%


# Idea: We can achieve O(1) for both the "add" and "getProduct" functions.
# We can do this by using a dictionary (Hash-Map) for inserting a new number in constant time
# And we can use a "Prefix sum" auxiliary array to achieve retrieval in constant time
class ProductOfNumbers:

    def __init__(self):
        self.size = 0
        self.numbers = {}
        self.prefixSum = {} # Should have called this prefix product
        self.lastZeroIndex = -1 # initally we assume that the array does not contain any zeroes
        self.prefixIndex = 0
        

    def add(self, num: int) -> None:
        self.numbers[self.size] = num
        if num == 0:
            self.lastZeroIndex = self.size
            self.prefixIndex = 0
        else:
            self.prefixSum[self.prefixIndex] = self.prefixSum.get(self.prefixIndex - 1, 1) * num
            self.prefixIndex += 1

        self.size += 1
        # print(f"current prefixArray: {self.prefixSum.values()}, prefixIndex = {self.prefixIndex}")


    def getProduct(self, k: int) -> int:
        if self.size - k <= self.lastZeroIndex:
            return 0
         
        return self.prefixSum[self.prefixIndex - 1] // self.prefixSum.get(self.prefixIndex - k - 1, 1)

# Test cases:

productOfNumbers = ProductOfNumbers()
productOfNumbers.add(1)
print(f"product = {productOfNumbers.getProduct(1)}") # Expect: 1
print(f"product = {productOfNumbers.getProduct(1)}") # Expect: 1
print(f"product = {productOfNumbers.getProduct(1)}") # Expect: 1
productOfNumbers.add(7)
productOfNumbers.add(6)
productOfNumbers.add(7)


# productOfNumbers = ProductOfNumbers()
# productOfNumbers.add(3);      #  // [3]
# productOfNumbers.add(0);       # // [3,0]
# productOfNumbers.add(2);        #// [3,0,2]
# productOfNumbers.add(5);        #// [3,0,2,5]
# productOfNumbers.add(4);        #// [3,0,2,5,4]
# print(f"product = {productOfNumbers.getProduct(2)}") #// return 20. The product of the last 2 numbers is 5 * 4 = 20
# print(f"product = {productOfNumbers.getProduct(3)}") #// return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
# print(f"product = {productOfNumbers.getProduct(4)}"); #// return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
# productOfNumbers.add(8);        #// [3,0,2,5,4,8]
# print(f"product = {productOfNumbers.getProduct(2)}"); #// return 32. The product of the last 2 numbers is 4 * 8 = 32 

# # Your ProductOfNumbers object will be instantiated and called as such:
# # obj = ProductOfNumbers()
# # obj.add(num)
# # param_2 = obj.getProduct(k)