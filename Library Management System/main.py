class Library:
    countofbooks = 0
    def __init__(self,compbooks,artbooks,engbooks,busbooks,jeebooks,listofbooks,allbooks,cc,ca,ce,cb,cj,name):
        self.listofComputerBooks = compbooks
        self.listofArtsBooks = artbooks
        self.listofEngineeringBooks = engbooks
        self.listofBussinessBooks = busbooks
        self.listofJeeBooks = jeebooks
        self.listofBooks = listofbooks
        self.listofAllBooks = allbooks
        self.cc = cc 
        self.ca = ca
        self.ce = ce
        self.cb = cb
        self.cj = cj
        self.name = name

    def Details(self):
        print(f"COMPUTER BOOKS : \n{self.listofComputerBooks}")
        print(f"ARTS BOOKS : \n{self.listofArtsBooks}")
        print(f"ENGINEERING BOOKS : \n{self.listofEngineeringBooks}")
        print(f"BUSSINESS BOOKS : \n{self.listofBussinessBooks}")
        print(f"JEE BOOKS : \n{self.listofJeeBooks}")
        
        
    def Available(self):
        print("Books Available : ")
        print("\nComputer Books :")
        for i,item in enumerate(self.listofComputerBooks):
            if self.cc[i]=='NOT AVAILABLE':
                continue
            else:
                print(item)
            
        print("\nArts Books :")
        for i,item in enumerate(self.listofArtsBooks):
            if self.ca[i]=='NOT AVAILABLE':
                continue
            else:
                print(item)
            
        print("\nEngineering Books :")
        for i,item in enumerate(self.listofEngineeringBooks):
            if self.ce[i]=='NOT AVAILABLE':
                continue
            else:
                print(item)
            
        print("\nBussiness Books :")
        for i,item in enumerate(self.listofBussinessBooks):
            if self.cb[i]=='NOT AVAILABLE':
                continue
            else:
                print(item)
            
        print("\nJee Books :")
        for i,item in enumerate(self.listofJeeBooks):
            if self.cj[i]=='NOT AVAILABLE':
                continue
            else:
                print(item)
            
        
    def IssueofBook(self):
        if self.countofbooks<3:
                print("Enter :")
                try:
                    inp = int(input('''1] COMPUTER BOOKS
2] ARTS BOOKS 
3] ENGINEERING BOOKS 
4] BUSSINESS BOOKS
5] JEE BOOKS  
\n     '''))
                    if inp==1:
                        print(self.listofComputerBooks)
                        print(f"Books Available {self.cc}")
                        try:
                            inp1 = int(input("Enter The Book Number For Issue :"))
                        
                            if inp1==1 and inp1 in self.cc:
                                print(f"{self.listofComputerBooks[inp1-1]} is Issued To {self.name}")
                                self.cc[inp1-1] = "NOT AVAILABLE"
                                self.countofbooks+=1
                            elif inp1==2 and inp1 in self.cc:
                                print(f"{self.listofComputerBooks[inp1-1]} is Issued To {self.name}")
                                self.cc[inp1-1] = "NOT AVAILABLE"
                                self.countofbooks+=1
                            elif inp1==3 and inp1 in self.cc:
                                print(f"{self.listofComputerBooks[inp1-1]} is Issued To {self.name}")
                                self.cc[inp1-1] = "NOT AVAILABLE"
                                self.countofbooks+=1
                            else:
                                print("Wrong Entry")    
                        
                        except:
                            print("Wrong Syntax")
                    
                    if inp==2:
                        print(self.listofArtsBooks)
                        print(f"Books Available {self.ca}")
                        try:
                            inp1 = int(input("Enter The Book Number For Issue :"))
                        
                            if inp1==1 and inp1 in self.ca:
                                print(f"{self.listofArtsBooks[inp1-1]} is Issued To {self.name}")
                                self.ca[inp1-1] = "NOT AVAILABLE"
                                self.countofbooks+=1
                            elif inp1==2 and inp1 in self.cc:
                                print(f"{self.listofArtsBooks[inp1-1]} is Issued To {self.name}")
                                self.ca[inp1-1] = "NOT AVAILABLE"
                                self.countofbooks+=1
                            else:
                                print("Wrong Entry")    
                        
                        except:
                            print("Wrong Syntax")

                    if inp==3:
                        print(self.listofEngineeringBooks)
                        print(f"Books Available {self.ce}")
                        try:
                            inp1 = int(input("Enter The Book Number For Issue :"))
                        
                            if inp1==1 and inp1 in self.ce :
                                print(f"{self.listofEngineeringBooks[inp1-1]} is Issued To {self.name}")
                                self.ce[inp1-1] = "NOT AVAILABLE"
                                self.countofbooks+=1
                            elif inp1==2 and inp1 in self.ce :
                                print(f"{self.listofEngineeringBooks[inp1-1]} is Issued To {self.name}")
                                self.ce[inp1-1] = "NOT AVAILABLE"
                                self.countofbooks+=1
                            elif inp1==3 and inp1 in self.ce:
                                print(f"{self.listofEngineeringBooks[inp1-1]} is Issued To {self.name}")
                                self.ce[inp1-1] = "NOT AVAILABLE"
                                self.countofbooks+=1
                            else:
                                print("Wrong Entry")    
                        
                        except:
                            print("Wrong Syntax")
                    

                    if inp==4:
                        print(self.listofBussinessBooks)
                        print(f"Books Available {self.cb}")
                        try:
                            inp1 = int(input("Enter The Book Number For Issue :"))
                        
                            if inp1==1 and inp1 in self.cb:
                                print(f"{self.listofBussinessBooks[inp1-1]} is Issued To {self.name}")
                                self.cb[inp1-1] = "NOT AVAILABLE"
                                self.countofbooks+=1
                            elif inp1==2 and inp1 in self.cb:
                                print(f"{self.listofBussinessBooks[inp1-1]} is Issued To {self.name}")
                                self.cb[inp1-1] = "NOT AVAILABLE"
                                self.countofbooks+=1
                            else:
                                print("Wrong Entry")    
                        
                        except:
                            print("Wrong Syntax")

                    if inp==5:
                        print(self.listofJeeBooks)
                        print(f"Books Available {self.cj}")
                        try:
                            inp1 = int(input("Enter The Book Number For Issue :"))
                        
                            if inp1==1 and inp1 in self.cj:
                                print(f"{self.listofJeeBooks[inp1-1]} is Issued To {self.name}")
                                self.cj[inp1-1] = "NOT AVAILABLE"
                                self.countofbooks+=1
                            elif inp1==2 and inp1 in self.cj:
                                print(f"{self.listofJeeBooks[inp1-1]} is Issued To {self.name}")
                                self.cj[inp1-1] = "NOT AVAILABLE"
                                self.countofbooks+=1
                            elif inp1==3 and inp1 in self.cj:
                                print(f"{self.listofJeeBooks[inp1-1]} is Issued To {self.name}")
                                self.cj[inp1-1] = "NOT AVAILABLE"
                                self.countofbooks+=1
                            else:
                                print("Wrong Entry")    
                        
                        except:
                            print("Wrong Syntax")
                except:
                    print("Wrong Entry")            
        else:
            print("You have reached the Limit of Issuing the Book")    

    def Return(self):
        print("Enter The Category Of Book to be Returned : ")
        try:
            inp = int(input('''1] COMPUTER BOOKS
                2] ARTS BOOKS 
                3] ENGINEERING BOOKS 
                4] BUSSINESS BOOKS
                5] JEE BOOKS  
                    '''))
            if inp==1:
                try:
                    inp1 = int(input("Enter The Book Number For Return :"))
                
                    if inp1==1 and "NOT AVAILABLE" == self.cc[inp1-1]:
                        print(f"{self.listofComputerBooks[inp1-1]} is Returned To Library")
                        self.cc[inp1-1] = inp1
                        self.countofbooks-=1
                    elif inp1==2 and "NOT AVAILABLE" == self.cc[inp1-1]:
                        print(f"{self.listofComputerBooks[inp1-1]} is Returned To Library")
                        self.cc[inp1-1] = inp1
                        self.countofbooks-=1
                    elif inp1==3 and "NOT AVAILABLE" == self.cc[inp1-1]:
                        print(f"{self.listofComputerBooks[inp1-1]} is Returned To Library")
                        self.cc[inp1-1] = inp1
                        self.countofbooks-=1
                    else:
                        print("Wrong Entry")    
                except:
                    print("Wrong Syntax")
                
            if inp==2:
                try:
                    inp1 = int(input("Enter The Book Number For Return :"))
                
                    if inp1==1 and "NOT AVAILABLE" == self.ca[inp1-1]:
                        print(f"{self.listofArtsBooks[inp1-1]} is Returned To Library")
                        self.ca[inp1-1] = inp1
                        self.countofbooks-=1
                    elif inp1==2 and "NOT AVAILABLE" == self.ca[inp1-1]:
                        print(f"{self.listofArtsBooks[inp1-1]} is Returned To Library")
                        self.ca[inp1-1] = inp1
                        self.countofbooks-=1
                    else:
                        print("Wrong Entry")    
                except:
                    print("Wrong Syntax")
                    
            if inp==3:
                try:
                    inp1 = int(input("Enter The Book Number For Return :"))
                
                    if inp1==1 and "NOT AVAILABLE" == self.ce[inp1-1]:
                        print(f"{self.listofEngineeringBooks[inp1-1]} is Returned To Library")
                        self.ce[inp1-1] = inp1
                        self.countofbooks-=1
                    elif inp1==2 and "NOT AVAILABLE" == self.ce[inp1-1]:
                        print(f"{self.listofEngineeringBooks[inp1-1]} is Returned To Library")
                        self.ce[inp1-1] = inp1
                        self.countofbooks-=1
                    elif inp1==3 and "NOT AVAILABLE" == self.ce[inp1-1]:
                        print(f"{self.listofEngineeringBooks[inp1-1]} is Returned To Library")
                        self.ce[inp1-1] = inp1
                        self.countofbooks-=1
                    else:
                        print("Wrong Entry")    
                except:
                    print("Wrong Syntax")

            if inp==4:
                try:
                    inp1 = int(input("Enter The Book Number For Return :"))
                
                    if inp1==1 and "NOT AVAILABLE" == self.cb[inp1-1]:
                        print(f"{self.listofBussinessBooks[inp1-1]} is Returned To Library")
                        self.cb[inp1-1] = inp1
                        self.countofbooks-=1
                    elif inp1==2 and "NOT AVAILABLE" == self.cb[inp1-1]:
                        print(f"{self.listofBussinessBooks[inp1-1]} is Returned To Library")
                        self.cb[inp1-1] = inp1
                        self.countofbooks-=1
                    else:
                        print("Wrong Entry")    
                except:
                    print("Wrong Syntax")

            if inp==5:
                try:
                    inp1 = int(input("Enter The Book Number For Return :"))
                
                    if inp1==1 and "NOT AVAILABLE" == self.cj[inp1-1]:
                        print(f"{self.listofJeeBooks[inp1-1]} is Returned To Library")
                        self.cj[inp1-1] = inp1
                        self.countofbooks-=1
                    elif inp1==2 and "NOT AVAILABLE" == self.cj[inp1-1]:
                        print(f"{self.listofJeeBooks[inp1-1]} is Returned To Library")
                        self.cj[inp1-1] = inp1
                        self.countofbooks-=1
                    elif inp1==3 and "NOT AVAILABLE" == self.cj[inp1-1]:
                        print(f"{self.listofJeeBooks[inp1-1]} is Returned To Library")
                        self.cj[inp1-1] = inp1
                        self.countofbooks-=1
                    else:
                        print("Wrong Entry")    
                except:
                    print("Wrong Syntax")     

        except:
            print("Wrong Syntax")           
    @staticmethod        
    def Instructions():
        print("\n Welcome To Instructions of Library ")
        print("\n Rules:")
        print("1) A Student Can issue a Book one at a time")
        print("2) A Student Once issued the book , should return the book in 30 days from date of issue")
        print("3) A Student can issue max of 3 Books")    
        print("4) If any Damange to Book is found , then penalty will be issued ")
        print("5) For Issuing and Returning the book , Follow to The page without fail")        

    def profile(self):
            print(f"Books Issued By : {self.name}")
            
            print("\nComputer Books :")
            count=0
            for i,item in enumerate(self.cc):
                if "NOT AVAILABLE" == item:
                    print(self.listofComputerBooks[i])    
                else:
                    count+=1    
                if count==3:
                    print("No Books Issued")
                    
            print("\nArts Books :")
            count=0
            for i,item in enumerate(self.ca):
                if "NOT AVAILABLE" == item:
                    print(self.listofArtsBooks[i])    
                else:
                    count+=1    
                if count==2:
                    print("No Books Issued")
            
            print("\nEngineering Books :")
            count=0
            for i,item in enumerate(self.ce):
                if "NOT AVAILABLE" == item:
                    print(self.listofEngineeringBooks[i])    
                else:
                    count+=1    
                if count==3:
                    print("No Books Issued")
            
            print("\nBussiness Books :")
            count=0
            for i,item in enumerate(self.cb):
                if "NOT AVAILABLE" == item:
                    print(self.listofBussinessBooks[i])    
                else:
                    count+=1    
                if count==2:
                    print("No Books Issued")
            
            print("\nJee Books :")
            count=0
            for i,item in enumerate(self.cj):
                if "NOT AVAILABLE" == item:
                    print(self.listofJeeBooks[i])    
                else:
                    count+=1    
                if count==3:
                    print("No Books Issued")


if __name__ == '__main__':
    listofComputerBooks = ["1) Practical Ethical Hacking - Ansh Goyal",
                        "2) Head First Python - Shroff/O'Reilly", 
                        "3) Modern C++ - Scott Meyers"]
    listofArtsBooks = ["1) Little Nemo - Winson",
                    "2) Stand Up Comendy - Judy Cater"]
    listofEngineeringBooks = ["1) Electrical Engineering - Max",
                            "2) System Requirements Engineering - Jean Bron",
                            "3) Advanced Mathematics - Erwing Kreyzing "]
    listofBussinessBooks = ["1) Science of Getting Rich - Wallace D.Wattles",
                            "2) Law of Success - Napoleaon Hills"]
    listofJeeBooks = ["1) Concepts of Physics - HC Verma",
                    "2) Organic Chemistry - MS Chouhan",
                    "3) Mathematics - Cengage"]

    count_cc = [1,2,3]
    count_ce = [1,2,3]
    count_cj = [1,2,3]
    count_ca = [1,2]
    count_cb = [1,2]

    listofBooksAll = [i for i in listofComputerBooks]
    for item in listofArtsBooks:
        listofBooksAll.append(item)
    for item in listofEngineeringBooks:
        listofBooksAll.append(item)
    for item in listofBussinessBooks:
        listofBooksAll.append(item)
    for item in listofJeeBooks:
        listofBooksAll.append(item)

    listofBooks = {}

    listofBooks['1] COMPUTER BOOKS'] = listofComputerBooks
    listofBooks['2] ARTS BOOKS'] = listofArtsBooks
    listofBooks['3] ENGINEERING BOOKS'] = listofEngineeringBooks
    listofBooks['4] BUSSINESS BOOKS'] = listofBussinessBooks
    listofBooks['5] JEE BOOKS'] = listofJeeBooks
    listofBooks['6] All BOOKS'] = listofBooksAll

    print("\t\t\t\t LIBRARY SYSTEM ")
    name = input("\n\n Enter Your Name : ")

    name1 = Library(listofComputerBooks,listofArtsBooks,listofEngineeringBooks,listofBussinessBooks,listofJeeBooks,listofBooks,listofBooksAll,count_cc,count_ca,count_ce,count_cb,count_cj,name)
    
    while True:
        try:
            n = int(input("\nEnter :\n1) Start\n2) Stop : \n"))
        except:
            print("Wrong Syntax")
            continue
        
        if n==1:
            inp=int(input('''\n\nMenu:
                1) Details of Books Available in Library
                2) Books Available
                3) Books For Issue
                4) Return Of Book  
                5) Instructions 
                6) Student Details\n 
                        '''))

            if inp==1:
                name1.Details()
            elif inp==2:
                name1.Available()
            elif inp==3:
                name1.IssueofBook()
            elif inp==4:
                name1.Return()
            elif inp==5:
                name1.Instructions()
            elif inp==6:
                name1.profile()
                
            else:
                print("Wrong Entry")
                
        elif n==2:
            print("Thank You for visiting the Library")
            exit()
                                    
        else:
            print("Wrong Entry")    

        



