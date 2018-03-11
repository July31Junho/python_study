print("Hello World")

a = 10
b = 20
c = 30
# resut 1
print ( a +  b)

# result 2
print(" Result : "+ str(a+b+c) ,end = "\n")

dica = {'name ' : 'pey' , 'phone' : '0101010101' , 'birth' : '0731'}
print(dica.keys())

for k  in dica.keys():
    print(k)
for k in dica.keys():
    print(k+":"+dica[k])
print(dica.items() , end=' ')

