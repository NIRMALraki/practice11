print('1.uppercase\n 2.lowecase\n 3.length\n 4.max\n 5.min\n 6.slice\n 7.reverse\n 8.concatenation\n 9.member\n 10.sort\n')
print('enter zero to exit')
while True:
      choice=int(input('enter your choice:'))
      if choice==1:
         n1=input('Enter a string')
         if not(n1):
            print('empty')
         elif n1.isalnum():
            print('n1.upper')
         else:
            print('not possible')
      
      elif choice==2:
           n1=input('enter a string')
           if not(n1):
              print('empty')
           else:
              print(n1.lowercase)
      
      elif choice==3:
           n1=input('enter a string')
           if not(n1):
              print('empty')
           else:
              print(len(n1))
      
      elif choice==4:
           n1=input('enter a string')
           if not(n1):
              print('empty')
           else:
              print(max(n1))
      
      elif choice==5:
           n1=input('Enter a string')
           if not(n1):
              print('empty')
           else:
              print(min(n1))
    
      elif choice==6:
           n1=input('Enter a string')
           if not(n1):
              print('empty')
           else:
              print(n1[2:4])

      elif choice==7:
           n1=input('enter a string')
           if not(n1):
              print('empty')
           else:
              print(n1[::-1])
    
      elif choice==8:
           n1=input('enter a string')
           if not(n1):
              print('empty')
              n2=input('enter a string')
              print(n1+n2)
     
      elif choice==9: 
           n1=input('enter a string')
           n2=input('enter a substring')
           print(n2 in n1)
 
      elif choice==10:
           n1=input('enter a string')
           print(''.join(sorted(n1)))
      elif choice==0:
         exit()
      break
      
          
 
