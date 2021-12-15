class Googlepay:                                                                                   #OOPS
    
    def __init__(self,Email_ID,Phone_number,Name,bank):                                                                  #FUNCTION
        self.emailid=Email_ID
        self.mobile=Phone_number
        self.name=Name
        self.account=bank
       
        
    def email_verification(self):
        if type(self.emailid) == str:                                                                               #VALUE VALIDATION
            if len(self.emailid) <= 30:                                                                              
                print("email_id verified")
            else:
                raise ValueError("the emailid should not contain more 30 values")
        else:
            raise TypeError("invalid emailid")

        
    def mobile_verification(self):
        if (len(self.mobile)==10):
            if type(self.mobile) == str:                                                                            #TYPE VALIDATION
                print("phone number verified")
            else:
                raise TypeError("the phone should contain only integers ")
        else:
            raise ValueError("the phone number should not be grater than or lesser than 10")
        
        
    def name_verification(self):
        if type(self.name) == str:
            if len(self.name) <= 20:                                                                                #LEN FUNCTION
                print("name verified")
            else:
                raise ValueError("The name should contain lesser than or equal to 20 letters")
        else:
            raise TypeError("The name should contain letters only")



    def Bank_verification(self):
        if type(self.account) == str:
            if len(self.account) <= 15:                                                                                #LEN FUNCTION
                print("bank verified")
            else:
                raise ValueError("The account number should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("The account number should contain numbers only")

  

    def set_Pin(self,number):
        self.pin=number
        if (len(self.pin)==4 or len(self.pin) ==6):
            print("your pin is successfully created")
        else:
            raise ValueError("Invalid pin_number")
        

    def Enter_your_Pin(self,match,pin):
        self.match=match
        self.pin=pin
        if self.match==self.pin:
            print("DONE")
        else:
            raise ValueError("pin not matched")
