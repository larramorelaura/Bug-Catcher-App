
for i in range(0, 151, 1):
    print(i)

for i in range (5, 1001, 1):
    if i%5==0:
        print(i)

for i in range( 1, 101, 1):
    if i%10==0:
        print('Coding Dojo')
    elif i%5==0:
        print('Dojo')
    else:
        print(i)

sum=0
for i in range(0, 500001, 1):
    if i%2==0:
        sum+=i
print(sum)

i=2018
while i>=0:
    print(i)
    i=i-4

lowNum=3
highNum=15
mult=3
for i in range(lowNum, highNum, 1):
    if i%mult==0:
        print(i)
