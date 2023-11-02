import pandas as pd

dict_data = {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}
df = pd.DataFrame(dict_data)
print(type(df))
print('\n')
print(df)

df2 = pd.DataFrame([[20,'남','공학'],[21,'여','경제학']], index= ['민교','한솔'], columns=['나이','성별','학과'])  #index = heading of each row, columns = heading of each column
print(df2)
print('\n')
print(df2.index)
print(df2.columns)
print(df2.values)

df2.rename(columns={'나이':'연령','성별':'남녀','학과':'공부'}, inplace=True) #changing column headings
print(df2)

# inplace = True --> 원본 객체 변경

df2.rename(index={'민교':'학생1','한솔':'학생2'}, inplace=True) #changing row headings
print(df2)



#행/열 삭제

exam_data = {'수학':[70,93,100],'국어': [88,74,99], '과학': [66,79,88]}
df3 = pd.DataFrame(exam_data, index=['학생1','학생2','학생3'])
print(df3)
print('\n')
#데이터프레임 df3를 복제하여 변수 df4에 저장, df4의 1개 row 삭제
df4 = df3.copy()
df4.drop('학생1', inplace=True) # axis = 0 --> deleting rows, but this can be omitted
print(df4)
print('\n')
#데이터프레임 df3를 복제하여 변수 df5에 저장, df5의 2개 row 삭제
df5 = df3.copy()
df5.drop(['학생1','학생2'], inplace=True)
print(df5)
print('\n')

#데이터프레임 df3를 복제하여 변수 df6에 저장, df6의 1개 column 삭제
df6 = df3.copy()
df6.drop('수학', axis=1, inplace=True) #axis = 1 --> deleting columns
print(df6)
print('\n')
#데이터프레임 df3를 복제하여 변수 df7에 저장, df7의 2개 column 삭제
df7 = df3.copy()
df7.drop(['국어','과학'], axis = 1, inplace = True)
print(df7)
print('\n')

#행 선택
label1 = df3.loc['학생1'] # finding row with heading "학생1"
position1 = df3.iloc[0] #finding the first row
print(label1)
print('\n')
print(position1)

label2 = df3.loc[['학생1','학생2']]
position2  = df3.iloc[[0,1]]
print(label2)
print('\n')
print(position2)
print('\n')

#열 선택

math1 = df3['수학'] #method 1
print(math1)
print('\n')

language = df3.국어 # method 2
print(language)
print('\n')

stem = df3[['수학','과학']] #extracting more than 1 column
print(stem)
print('\n')

#범위 슬라이싱

print(df3.iloc[::2])
print(df3.iloc[::-1])

#원소 선택