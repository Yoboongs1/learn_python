import pandas as pd
dict_data = {'a' : 1, 'b' : 2, 'c' : 3}
sr1 = pd.Series(dict_data)
print(type(sr1))
print('\n')
print(sr1)

list_data = ['hi', 25, True]
sr2 = pd.Series(list_data)
idx = sr2.index
val = sr2.values
print(type(sr2))
print('\n')
print(sr2) #dictionary의 키처럼 인덱스로 변환될 값이 없기에 디폴트로 정수형 위치 인덱스가 지정된다
print(f"{idx}\n{val}")

tup_data = ('윤민교', '2003-01-02', '남', True)
sr3 = pd.Series(tup_data, index= ['이름', '생년월일', '성별', '학생여부'])
print(sr3)
print(sr3[0])
print(sr3['이름']) #정수형 위치 인덱스와 인덱스 라벨이 같긴 때문에 똑같은 값이 프린트된다