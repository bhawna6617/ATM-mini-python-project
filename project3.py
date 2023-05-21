print("ATM Machine Management System using python")

username='Aayu'
password="Nandu6617"


c_name=input("enter your name:-")
c_pass=str(input("enter your password:-"))
if c_name==username and c_pass==password:
    # print("succuss")
    print('''
          1.deposite
          2.withdrow
          3.mini_statement
          4.exit
          
          ''')
    
    amount=50000
    option=int(input("select your option:-"))
    if option==1:
        dep=int(input("enter the amount :-"))
        amount+=dep
        print("total amount:-",amount)
    elif option==2:
        withd=int(input("enter your amount:-"))
        amount-=withd
        print("total amount:-",amount)
    elif option==3:
        print("======ATM=======")
        print("Username:",username)
        print("total amount :-",amount)
        print("THANKS FOR VISITING")
        print("=============")
    elif option==4:
        exit()
else:
    print("please enter correct logins")
    