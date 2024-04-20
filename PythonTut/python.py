file=open("abc.txt","w")
for num in range(10):
    square=num*num
    file.write(str(square)+'\n')
file.close()

filess=open("abc.txt","r")
print(filess.read()[:14])