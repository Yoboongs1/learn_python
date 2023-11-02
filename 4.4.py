example_list = ["A", "B", "C"]
print(enumerate(example_list))
print(list(enumerate(example_list)))

for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다".format(i,value))

a = [1,2,3,4,5]
b = reversed(a)
print(a)
print(b)
print(list(b))

example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C"
}
print(example_dictionary.items())

for i,value in example_dictionary.items():
    print("{} = {}".format(i,value))


array = [i*i for i in range(0,20,2)]
print(array)

array2 = ["사과","자두","초콜릿","바나나"]
output = [fruit for fruit in array2 if fruit != "초콜릿"]
print(output)