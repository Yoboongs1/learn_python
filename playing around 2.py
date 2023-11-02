import math
import re



aword = "test1b"
breakdown = re.findall(r'[a-zA-Z]+|\d+|\W+', aword)
print(breakdown)
nums = [1,3,1,5]


input = nums
for i in range(len(nums)-1):
    nums[i+1] += nums[i] 
print(nums)


nums2 = [1,7,3,6,5,6]

print(sum(nums2[:3]))
print(sum(nums2[3:]))
print(list(enumerate(nums)))


#Zip 함수
s = "egg"
t = "add"

for pair in zip(s,t):
    print(pair)

print(list(zip(s,t)))

###

# .index()
cool_list = [1,2,3,4,5]
print(s.index("g"))
print(cool_list.index(4))

###

# iter() and next()

l = iter(range(3)) ## more generally, iter(obj,sentinel) where obj = object to be converted to iterable and sentinel = value used to represent the end of the sequence (end iteration)
print(next(l))
print(next(l))
print(next(l))
#print(next(l)) ## no more values remaining for l -- we can remove error by next(l, num) where num will be displayed as default if l goes out of range
print(next(l,10))

word = "handsome"
word2 = "had"
for i in word2:
    c = word.find(i) ##finds the position (index) of the letter
    print(c)
c2 = word.find("q") #if the character does not exist, the result is -1
print(c2)
####

mylist = []
for i in range(len(s)):
    mylist.append(s[i])
print(mylist)

# Eliminating a letter from string each time

q = "mingyo"
q = q[1:]
print(q)
q = q[1:]
print(q)



def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다")
        #print(list_a) adding this line will enable the statements under except 
        return #return 키워드로 try 구문 중간에서 탈출합니다--> else 아래에 있는 코드는 실행되지 않습니다 ; 하지만 finally 아래에 있는 코드는 무조건 실행됩니다
        print("try 구문의 return 키워드 뒤입니다")
    except:
        print("except 구문이 실행되었습니다")
    else:
        print("else 구문이 실행되었습니다")
    finally:
        print("finally 구문이 실행되었습니다")
    print("test() 함수의 마지막 줄입니다")
test()



#예외 처리
try:
    number_input = int(input("Type an integer>"))
    print("Radius", number_input)
    print("Circumference", 2*3.14*number_input)
    print("Area", 3.14 * number_input*2)
except Exception as exception:
    print("Type of Exception:", type(exception))
    print("Execption:" , exception)
    
new_list =[1,2,3,4,5]

new_list = new_list[1:]
print(new_list)


#Maximum profit (buy first and then sell afterwards) using pointers

class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit


funny_word = "abbcddee"
funny_set = set(funny_word)

empty_list = []
empty_list.append([1,2,3])
print(empty_list)

full_list = [[1,3,2],[3,6,4],[1,2,3]]
for x in full_list:
    x = x.sort()
print(full_list)
'''
full_list = list(set(full_list))
print(full_list)
'''
cute_word = "aabcc"
new_word = ""
for i in range(len(cute_word)):
    new_word += cute_word[len(cute_word)-i-1]
print(new_word)
print(cute_word[::-1])

two_d_array = [[1,2,3],[2,3,4],[3,4,5]]
print(len(two_d_array))


my_word = "aabcc"
characters = []


for i in my_word:
    if i not in characters:
        characters.append(i)

print(characters)

for i in range(10):
    print(i)

list1 = [1,3,2,4]
list1.sort() # this returns none, but has changed the order of list1--> to display the sorted list, print(list1)
print(list1.sort()) #this returns none
print(sorted(list1)) #this will return the sorted list

myword= "17231"
myword2 = ""
for i in myword:
    myword2 += i
print(myword2)



string1 ="172.12.13.1"
string2 = "111.13..1"
string3 = "255.255.255.255"
string4 = "256.1341.1.12"

def solution(s):
    p = s.split('.') #split() splits a string into a list of strings after breaking the given string by the specified separator

    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)   

print(solution(string1))
print(solution(string2))
print(solution(string3))
print(solution(string4))

my_sentence = "Hi my name is mingyo"
my_sentence = my_sentence.split()
print(my_sentence)
#all()- 모두 True여야 True 반환
#any()- 하나라도 True이면 True 반환


word_list = ["happy","new","year"]
print(word_list[0][0])

brackets = "([])"


def isValid(s):
    stacking = []
    for i in range(len(s)):
        if s[i] in ["[", "(", "{"]:
            stacking.append(s[i])
        else:
            if stacking[-1] + s[i] in ["()","[]","{}"]:
                stacking.pop(-1)
    return stacking
print(isValid(brackets))

state1 = False
state2 = None
print(state1 == state2)

#Multiply all elements of a list by 2 using lambda and map() function

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(map(lambda x: x*2, li))
print(final_list)

#Filter out all odd numbers using filter() and lambda function

new_final_list = list(filter(lambda x: (x % 2 != 0), li)) #filter() only keeps elements where it produces True, and removes elements where it produces False
print(new_final_list)


#Roman to integer

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(lambda x: roman_to_integer[x], s))

print(string1.split('.'))

#Add two numbers in linked list
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next

#Merge two sorted list
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur =  list1.next, cur.next
            else:
                cur.next =  list2
                list2, cur = list2.next, cur.next
        if list1 or list2:
            cur.next = list1 if list1 else list2
        return dummy.next
        
s.isalnum(); #checks whether s is alphanumerical (either letter or number)