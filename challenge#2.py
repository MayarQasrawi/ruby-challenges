
def totalSequnce(numbers):
     
     minumam=int( min(numbers))
     maximun= int(max(numbers))

     series=set()
     while(minumam<=maximun):
          series.add(minumam)
          minumam +=1

     missing =series- set(numbers)
     return missing
     
try:
     user_input = input("Enter the elements of the set, separated by spaces: ")
     my_set=  set(int(element) for element in user_input.split())
     print('my set is:',my_set)
     print('missing numbers: ',totalSequnce(my_set))
except ValueError:
     print('please enter a valid set of integer :)')
