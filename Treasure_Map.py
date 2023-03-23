row_1 = ['_','_','_']
row_2 = ['_','_','_']
row_3 = ['_','_','_']
map = [row_1,row_2,row_3]
print(f"{row_1}\n{row_2}\n{row_3}")
ans = input("Where do you want to put the treasure?")
row =  int(ans[0]) - 1
column = int(ans[1]) - 1
map[row][column] = 'X'
print(f"{row_1}\n{row_2}\n{row_3}")
