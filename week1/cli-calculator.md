# Code

```
print("CLI Calculator Tool\nAvaliable Operations: +, -, *, /")
while True:
    print("***********************************")
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    op=input("Enter the operator: ")
    match op:
        case '+': result=n1+n2
        case '-': result=n1-n2
        case '*': result=n1*n2
        case '/': result=n1/n2
        case _: 
                print("Invalid operator")
                continue
    print("Result is: ",result)
    ch=input("Do you want to perform another calculation (Y/n)?: ").lower()
    if ch=='n':
        print("Exiting calculator!")
        break
```
# Output

![image](https://github.com/user-attachments/assets/ad57de22-e35c-4958-8dcc-3c50fe3cadb7)
