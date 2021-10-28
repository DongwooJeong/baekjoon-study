crodic = ['c=','c-','dz=','d-','lj','nj','s=','z=']
input_cro = input()
for i in crodic:
    input_cro = input_cro.replace(i,'*')
print(len(input_cro))