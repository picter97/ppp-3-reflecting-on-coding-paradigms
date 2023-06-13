def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

input_array = [[1,3,4],[5,2,6]]
result = flatten_and_sort(input_array)
print(result)

# How does this solution ensure data immutability?
  #this solution ensures data immutability by just appending and returning whats insiede the array
# Is this solution a pure function? Why or why not?
  #i believe this solution is a pure function because it does not change any value
# Is this solution a higher order function? Why or why not?
  #this solution is a higher order function because it puts numbers from lower to higher
# Would it have been easier to solve this problem using a different programming style?
  #i would not know for sure 
# Why in particular is functional programming a helpful paradigm when solving this problem?
  #i belive because it ensures immutability

