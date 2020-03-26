import pymysql
class Customer:
    con = pymysql.connect(host="localhost", user="root", password="", database='cms')
    def __init__(self):
        self.id=0
        self.name=''
        self.address=''
        self.mob=''
    def __str__(self):
        return "id: "+str(self.id)+" Name: "+self.name+" Address: "+ self.address+" mobileno: "+self.mob

    def addCustomer(self):
        myCursor = Customer.con.cursor()
        strQuery = "insert into Customer(id,name,address,mob) values(%s,%s,%s,%s)"
        myCursor.execute(strQuery, (self.id, self.name, self.address, self.mob))
        Customer.con.commit()
    def searchCustomer(self,id):
        myCursor = Customer.con.cursor()
        strQuery = "select * from Customer where id=%s"
        rowAffected=myCursor.execute(strQuery, (id))
        if(rowAffected!=0):
            row=myCursor.fetchone()
            self.id = row[0]
            self.name = row[1]
            self.address = row[2]
            self.mob = row[3]
        else:
            raise Exception("Id not found")
    def modifyCustomer(self):
        try:
            mycursor = Customer.con.cursor()
            #query = "UPDATE `customer` SET `name`="+"'"+self.name+"'"+" ,`address`="+"'"+self.address+"'"+",`mob`="+"'"+self.mob+"'"+" WHERE id="+"'"+str(id)+"'"+""
            query="UPDATE customer SET name=%s,address=%s,mob=%s WHERE id=%s"
            mycursor.execute(query,(self.name,self.address,self.mob,str(self.id)))
            Customer.con.commit()
        except Exception as ex:
            raise ex

    def deleteCustomer(self,id):
        mycursor = Customer.con.cursor()
        query = "DELETE FROM customer WHERE id=%s"
        mycursor.execute(query, (id))

    @staticmethod
    def showAllCustomers():
        query="SELECT * FROM customer"
        mycursor=Customer.con.cursor()
        mycursor.execute(query)
        desc=mycursor.description
        resultset=mycursor.fetchall()
        if(len(resultset)>0):
            return (desc,resultset)
        else:
            raise Exception("No Customer Exists")
    @staticmethod
    def showSortedCustomers():
        query = "SELECT * FROM customer ORDER BY id"
        mycursor = Customer.con.cursor()
        mycursor.execute(query)
        desc = mycursor.description
        resultset = mycursor.fetchall()
        if (len(resultset > 0)):
            return (desc, resultset)
        else:
            raise Exception("No Customer Exists")

    def getPrevCustomer(self,id):
        index = -1
        query = "SELECT * FROM customer"
        mycursor = Customer.con.cursor()
        mycursor.execute(query)
        desc = mycursor.description
        resultset = mycursor.fetchall()
        for i in range(len(resultset)):
            for j in range(len(resultset[i])):
                if (desc[j][0] == 'id'):
                    if (resultset[i][j] == id):
                        index = i
        if (index - 1 >= 0):
            for j in range(len(resultset[index-1])):
                if (desc[j][0] == 'id'):
                    self.id = resultset[index-1][j]
                elif (desc[j][0] == 'name'):
                    self.name = resultset[index-1][j]
                elif (desc[j][0] == 'address'):
                    self.address = resultset[index-1][j]
                elif (desc[j][0] == 'mob'):
                    self.mob = resultset[index-1][j]
        else:
            raise Exception("previous customer does not exists")

    def getNextCustomer(self, id):
        index = -1
        query = "SELECT * FROM customer"
        mycursor = Customer.con.cursor()
        mycursor.execute(query)
        desc = mycursor.description
        resultset = mycursor.fetchall()
        for i in range(len(resultset)):
            for j in range(len(resultset[i])):
                if (desc[j][0] == 'id'):
                    if (resultset[i][j] == id):
                        index = i
        if (index + 1 < len(resultset)):
            for j in range(len(resultset[index+1])):
                if (desc[j][0] == 'id'):
                    self.id = resultset[index+1][j]
                elif (desc[j][0] == 'name'):
                    self.name = resultset[index+1][j]
                elif (desc[j][0] == 'address'):
                    self.address = resultset[index+1][j]
                elif (desc[j][0] == 'mob'):
                    self.mob = resultset[index+1][j]
        else:
            raise Exception("next customer does not exists")

    def getFirstCustomer(self):
        query = "SELECT * FROM customer "
        mycursor = Customer.con.cursor()
        mycursor.execute(query)
        desc = mycursor.description
        resultset = mycursor.fetchone()
        length=len(resultset)
        if(length>0):
            for j in range(len(resultset)):
                    if(desc[j][0]=='id'):
                        self.id=resultset[j]
                    elif(desc[j][0]=='name'):
                        self.name=resultset[j]
                    elif(desc[j][0]=='address'):
                        self.address=resultset[j]
                    elif(desc[j][0]=='mob'):
                        self.mob=resultset[j]
        else:
            raise Exception("No Customer Exists")
    def getLastCustomer(self):
        query = "SELECT * FROM customer "
        mycursor = Customer.con.cursor()
        mycursor.execute(query)
        desc = mycursor.description
        resultset = mycursor.fetchall()
        #return resultset
        length=len(resultset)
        if(length>0):
            for j in range(len(resultset[length-1])):
                if (desc[j][0] == 'id'):
                    self.id = resultset[length-1][j]
                elif (desc[j][0] == 'name'):
                    self.name = resultset[length-1][j]
                elif (desc[j][0] == 'address'):
                    self.address = resultset[length-1][j]
                elif (desc[j][0] == 'mob'):
                    self.mob = resultset[length-1][j]
        else:
            raise Exception("No Customer Exists")