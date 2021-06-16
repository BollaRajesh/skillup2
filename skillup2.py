##a=100
##b=20
##if (a<b):
##    print(a+b)
##else:
##    print(a-b)
##    
##print('done')


##a=int(input())#10
##b=int(input())#10
##
##if a>b:
##    print(a,"is bigger")
##elif a==b:
##    print(a,b,'are same')
##else:
##    print('number',b,'is bigger')


##a=int(input())#10
##b=float(input())#20
##c=input()

##per=int(input())
##bl=int(input())
###>=60,no backlogs
##if per>=60 and bl==0:
##    print('eligible')
##else:
##    print('not eligible')


##m=int(input())
##
##if m>=0 and m<=100:
##    if m>=80:
##        print('A grade')
##    elif m>=60 and m<80:
##        print('B grade')
##    elif m>=40 and m<60:
##        print('C grade')
##    else:
##        print('Failed')
##
##else:
##    print('Invalid marks')


##m=35
##if m>=80:
##    print('A')
##elif 80>m>=60:
##    print('B')
##elif 60>m>=40:
##    print('C')
##else:
##    print('failed')


##uid=input()
##upw=input()
##
##if uid=='thub@123.com' and upw=='python123':
##    print('login successfully')
##else:
##    print('wrong credintials')


##uid=input()
##upw=input()
##
##if uid=='thub@123.com' :
##    if upw=='python123':
##        print(' "login successfully" ')
##    else:
##        print('wrong password')
##else:
##    print('wrong id')
    

##for i in range(1,10):#1,2,3,4,5,6,7,8,9
##    print(i,end=' ')#1,2,3,4,5,6,7,8,9

##for i in range(1,11,1):#1,2
##    print(i,end=' ')#1
##    i+=2#3
##    print(i)#3

##for i in range(1,11,3):
##    print(i,end=' ')

##for i in range(1,11,1):
##    print(i,end=' ')
##
##print()
##print(i)
##
##
##print()

##i=1#1
##while i<=10:#1,2,3,4,5,6,7,8,9,10
##    print(i,end=' ')#1,2,3,4,5,6,7,8,9,10
##    i+=1#2,3,4,5,6,7,8,9,10,11

##i=-10
##while i<=1:
##    print(i,end=' ')
##    i+=2

##i=1
##while i<10:
##    print(i,end=' ')


##for i in range(1,11):
##    print(i,end=' ')
##    if i==5:
##        
##        break
##print('done')
##
##
##for i in range(1,11):
##    if i==5:
##        continue
##    print(i,end=' ')
##
##print('done')

##i=1
##while i<=10:
##    if i==6:
##        break
##    print(i,end=" ")
##    i+=1
##
##print('done')


##i=0
##while i<10:
##    i+=1
##    if i==5:
##        continue
##    print(i,end=" ")
##print('done')

##for i in range(1,11):
##    if i==5:
##        break
##    print(i,end=' ')
##else:
##    print('done')


##for i in range(1,11,1):#1,3
##    print(i,end=' ')#1
##    i+=2#3
##    
##    print(i)#3
##    


##for i in range(1,10,2):
##    print(i,end=' ')
##
##print()
##
##for i in range(1,10):
##    if i%2==1:
##        print(i,end=' ')
##
##print()
##
##for i in range(1,10):
##    if i%2==0:
##        continue
##    print(i,end=' ')

##n=int(input('enter a number: '))
##s=int(input('enter a start point: '))
##e=int(input('enter end point: '))
##
##for i in range(s,e+1):
##    print(n,'*',i,'=',n*i)
##
##while s<=e:
##    print(n,'*',s,'=',n*s)
##    s+=1

##n = int(input("Number: "))
##j = int(input("End Value:"))
## 
##i = 1
##while i <= j:
##    n * i
##    print(f"{n} * {i} = {n * i}"))
##    i += 1



##n=int(input('enter a number: '))#5
##s=int(input('enter a start point: '))#6
##e=int(input('enter end point: '))#3
##
##if s<e:#6<3 false
##    for i in range(s,e+1):
##        print(n,'*',i,'=',n*i)
##else:        
##    for i in range(s,e-1,-1):#(6,5,4,3)
##        print(n,'*',i,'=',n*i)


##s=int(input('enter a start point: '))#10
##e=int(input('enter end point: '))#25
##n=int(input('enter a number'))#3
##for i in range(s,e+1):
##    if i%n==0:
##        print(i,end=' ')


##n=int(input('enter a number: '))#5
##c=0
##for i in range(1,n+1):#1,2,3,4,5
##    if n%i==0:#1,5
##        c+=1#1,2
##        print(i)
##
##if c==2:
##    print(n,'is prime')
##else:
##    print(n,'is not a prime')

##n=int(input('enter a number: '))#9
##for i in range(2,n):#(2,9)  2 3 4 5 6 7 8
##    if n%i==0:#3
##        print(n,'is not a prime')
##        break
##else:
##    print(n,'is a prime')

##n=int(input('enter a number: '))
##c=0
##for i in range(1,(n//2)+1):
##    if n%i==0:
##        c+=1
##if c>1:
##    print(n,'is not a prime')
##else:
##    print(n,'is a prime')

##n=int(input('enter a number: '))
##import math
##s=int(math.sqrt(n))
##
##c=0
##
##for i in range(1,s+1):
##    if n%i==0:
##        c+=1
##
##if c>1:
##    print(n,'is not a prime')
##else:
##    print(n,'is a prime')

      
##n=int(input('enter a number: '))#253
##a=n
##rev=0
##while n:#253,25,2
##    rem=n%10#
##    rev=rev*10+rem
##    n=n//10   
##print(rev)
##
##if rev==a:
##    print(a,'is a palindrome')
##else:
##    print(a,'is not a palindrome')


##n=input('enter a number: ')
##if n==n[::-1]:
##    print(n,'is a palindrome')
##else:
##    print(n,'is not a palindrome')


##n=int(input('enter series range: '))
##a=0
##b=1
##print(a,b,end=' ')
##for i in range(3,n+1):
##    c=a+b
##    a=b
##    b=c
##    print(b,end=' ')

##n=int(input('enter series range: '))
##a=0
##b=1
##print(a,b,end=' ')
##for i in range(3,n+1):
##    c=2*a+b
##    a=b
##    b=c
##    print(b,end=' ')


##n=int(input('enter series range: '))
##a=0
##b=0
##c=1
##print(a,b,c,end=' ')
##for i in range(3,n+1):
##    d=a+b+c
##    a=b
##    b=c
##    c=d
##    print(c,end=' ')

##a=int(input())#3
##b=int(input())#10
##if a>b:#
##    a,b=b,a
##c=b#10
##while True:
##    if c%a==0 and c%b==0:#10,11,12,13.....30
##        print('LCM of',a,b,'is',c)
##        break
##    c+=1


##a=int(input())#8    12 
##b=int(input())#12   8
##if a>b:#12>8
##    a,b=b,a#8 12
##print(a,b)
##for i in range(a,0,-1):#8,7,6,5,4
##    if a%i==0 and b%i==0:#4
##        print('gcd of',a,b,'is',i)
##        break
##    


##def example():
##    print(10+20)
##
##example()


##def example(a,b):#formal parameters
##    print(a+b)
##
##x=int(input('enter a number: '))
##y=int(input('enter a number: '))
##example(x,y)#actual parameters
##
##n=int(input('enter a number: '))
##m=int(input('enter a number: '))
##example(n,m)#actual parameters


##def example(c,d):#formal parameters
##    print(c+d)#9
##x=int(input('enter a number: '))#4
##y=int(input('enter a number: '))#5
##example(x,y)#actual parameters
##
##
##def example(c,d):
##    return(c+d)
##x=int(input('enter a number: '))#4
##y=int(input('enter a number: '))#5
##
##print(example(x,y))#9

##def example():
##    global a
##    a=12#local variable
##    print('inside function',a)
##
##a=10#global variable
##print('before function',a)
##
##example()
##
##a+=1
##print('after function',a)


##def example():
##    global b
##    b=12
##    print('inside function',b)
##
##example()
##
##print('after function',b)



##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            #print(n,'is not a prime')
##            break
##    else:
##        print(n,'is a prime')
##
##
##s=int(input('enter a number: '))
##e=int(input('enter a number: '))
##for i in range(s,e+1):
##    prime(i)

##def add(a,b):
##    return(a+b)
##def sub(a,b):
##    return(a-b)
##def mul(a,b):
##    return(a*b)
##def div(a,b):
##    return(a%b)    
##
##a=int(input('enter a number: '))#10
##b=int(input('enter a number: '))#5
##print('1:addition,2:subtraction,3:multiplication,4:division')
##c=int(input('enter a choice: '))
##
##if c==1:
##    add(a,b)
##elif c==2:
##    sub(a,b)
##elif c==3:
##    mul(a,b)
##elif c==4:
##    div(a,b)
##else:
##    print('wrong choice')



##def add(a,b):
##    print(a+b)#huigfushGDFUHSGKFZGf
##add(5,4)
##
##def add1(a,b):
##    return(a+b)
##print(add1(5,4))#kjdsghugsUVGUyg
##

##
##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            print('False')
##            break
##    else:
##        print(True)
##
##prime(6)
##
##
##def prime111(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##    else:
##        return True
##
##print(prime111(6))





##a=int(input('entera number: '))
##if prime(a):
##    print(a,'is prime')


##while True:
##    a+=1
##    if prime(a):
##        print(a,'is prime')
##        break
##        
##


##def fact(n):#6
##    if n==1 or n==0:
##        return 1
##    else:
##        return(n*fact(n-1))
##print(fact(6))


##def fact(n):
##    f=1
##    for i in range(1,n+1):#1 2 3 4 5 6
##        f*=i#1 1*2  1*2*3 1*2*3*4 1*2*3*4*5 1*2*3*4*5*6
##    print(f)
##fact(6)

##def fact(n):
##    f=1
##    for i in range(1,n+1):#1 2 3 4 5 6
##        f*=i#1 1*2  1*2*3 1*2*3*4 1*2*3*4*5 1*2*3*4*5*6
##    return(f)
##print(fact(6))



def fun(a):
    l=0
    for i in a:
        l+=1
    return(l)

























        





































