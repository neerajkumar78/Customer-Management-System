from customer_pac import Customer
if(__name__=="__main__"):
    while (True):
        print(
            "1.Add Customer\n2.Search Customer\n3.Modify Customer\n4.Delete Customer\n5.Show All\n6.Sort Customer by id\n7.next customer details \n 8.previous customer details\n9.First Customer\n10.Last Customer0.Exit")
        ch = input("Enter ur Choice")
        if (ch == '1'):
            try:
                cus = Customer()
                cus.id = int(input("Enter Id"))
                cus.name = input("Enter Name")
                cus.address = input("Enter Address")
                cus.mob = input("Enter Mobile No")
                cus.addCustomer()
                print("Customer Added Sucessfully")
            except Exception as ex:
                print(ex)
        elif (ch == '2'):
            try:
                cus = Customer()
                id = int(input("Enter Id"))
                cus.searchCustomer(id)
                print(cus)
            except Exception as ex:
                print(ex)
        elif (ch == '3'):
            try:
                cus = Customer()
                cus.id = int(input("Enter Id"))
                cus.name = input("Enter Name")
                cus.address = input("Enter Address")
                cus.mob = input("Enter Mobile No")
                cus.modifyCustomer()
                print("Customer Modified Sucessfully")
            except Exception as ex:
                print(ex)
        elif (ch == '4'):
            try:
                cus = Customer()
                id = int(input("Enter Id"))
                cus.deleteCustomer(id)
                print("Customer Deleted Sucessfully")
            except Exception as ex:
                print(ex)
        elif (ch == '5'):
            result=Customer.showAllCustomers()
            desc=result[0]
            resultset=result[1]
            for i in range(len(resultset)):
                for j in range(len(resultset[i])):
                    print(desc[j][0] + " : " + str(resultset[i][j]), end='  ,   ')
                print()
        elif (ch == '6'):
             try:
                 result =Customer.showSortedCustomers()
                 desc = result[0]
                 resultset = result[1]
                 for i in range(len(resultset)):
                     for j in range(len(resultset[i])):
                         print(desc[j][0] + " : " + str(resultset[i][j]), end='  ,   ')
                     print()
             except Exception as ex:
                 print(ex)
        elif (ch == '7'):
             try:
                 nextId=int(input("enter current Customers Id"));
                 nextCustomer=Customer()
                 nextCustomer.getNextCustomer(nextId)
                 print(nextCustomer);
             except Exception as ex:
                 print(ex)
        elif (ch == '8'):
            prevId = int(input("enter current Customers Id"));
            prevCustomer = Customer()
            try:
                prevCustomer.getPrevCustomer(prevId)
                print(prevCustomer);
            except Exception as ex:
                print(ex)
        elif(ch=='9'):
            try:
                firstCustomer=Customer()
                firstCustomer.getFirstCustomer()
                print(firstCustomer)
            except Exception as ex:
                print(ex)
        elif (ch == '10'):
            try:
                lastCustomer = Customer()
                lastCustomer.getLastCustomer()
                print(lastCustomer)
            except Exception as ex:
                print(ex)
        elif (ch == '0'):
            break

