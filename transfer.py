import pay
emailid=input("enter the email id")
phno=input("enter the email phone number")
name=input("enter the name ")
acno=input("enter the bank account number")
print("____________________________________________________________")
raja=pay.Googlepay(emailid,phno,name,acno)

raja.email_verification()
print("____________________________________________________________")

raja.mobile_verification()
print("____________________________________________________________")

raja.name_verification()
print("____________________________________________________________")

raja.Bank_verification()
print("____________________________________________________________")


class Phone_pe(pay.Googlepay):                                                                                          #INHERITANCE
    def __init__(slef,Email_ID,Phone_number,Name,bank):
        super().__init__(Email_ID,Phone_number,Name,bank)

    def open_phonepe(self):
        print("Phone pe")
        
Ranjini=Phone_pe("rajaprabhu@gmail.com","9003085347","Mano","90023555")

Ranjini.open_phonepe()

Ranjini.mobile_verification()

Ranjini.name_verification()

Ranjini.Bank_verification()

print("____________________________________________________________")

y=input("set your pin")

print("************************************************************")

Ranjini.set_Pin(y)

i=input("enter the pin")

print("************************************************************")

Ranjini.Enter_your_Pin(i,i)


        
googlepay=[{"name":"ramesh","googlepaynum":7397266887,"type":"personal","account":"saving  account"},                       #DICTIONARY INSIDE LIST
           {"name":"ram","googlepaynum":7305341565,"type":"personal","account":"saving  account"},
           {"name":"vasu","googlepaynum":6381347949,"type":"personal","account":"current account"},
           {"name":"vasanth","googlepaynum":7358355054,"type":"personal","account":"current account"},
           {"name":"ajay","googlepaynum":7200636126,"type":"personal","account":"current account"},
           {"name":"meera","googlepaynum":9597916931,"type":"personal","account":"current account"},
           {"name":"sree","googlepaynum":8056469214,"type":"personal","account":"saving  account"},
           {"name":"subu","googlepaynum":9962454833,"type":"personal","account":"current account"},
           {"name":"dhana","googlepaynum":8015341851,"type":"personal","account":"current account"},
           {"name":"meha","googlepaynum":7305624091,"type":"personal","account":"current account"},
           {"name":"jela","googlepaynum":8939509826,"type":"personal","account":"current account"},
           {"name":"aarthi","googlepaynum":6369121983,"type":"personal","account":"saving  account"},
           {"name":"shuka","googlepaynum":9833807044,"type":"personal","account":"saving  account"},
           {"name":"asma","googlepaynum":9941297487,"type":"personal","account":"current account"},
           {"name":"babu","googlepaynum":7200001990,"type":"personal","account":"saving  account"},
           {"name":"bala","googlepaynum":6382880108,"type":"personal","account":"current account"},
           {"name":"mano","googlepaynum":9941656319,"type":"personal","account":"saving  account"},
           {"name":"shivani","googlepaynum":9500075619,"type":"personal","account":"current account"},
           {"name":"renu","googlepaynum":8072512570,"type":"personal","account":"saving  account"},
           {"name":"shree","googlepaynum":6382761961,"type":"personal","account":"current account"},
           {"name":"dharaneesh","googlepaynum":9791045340,"type":"personal","account":"saving  account"},
           {"name":"arun","googlepaynum":9841032642,"type":"personal","account":"saving  account"},
           {"name":"bharath","googlepaynum":6383908036,"type":"personal","account":"saving  account"},
           {"name":"syed","googlepaynum":8248631340,"type":"personal","account":"current account"},
           {"name":"mono","googlepaynum":6374339918,"type":"personal","account":"saving  account"},
           {"name":"mutakosu","googlepaynum":9840644601,"type":"personal","account":"saving  account"},
           {"name":"nenu","googlepaynum":6379741175,"type":"personal","account":"saving  account"},
           {"name":"papa","googlepaynum":8124252926,"type":"personal","account":"saving  account"},
           {"name":"liila","googlepaynum":9176093745,"type":"personal","account":"saving  account"},
           {"name":"guna","googlepaynum":9176358088,"type":"personal","account":"saving  account"},
           {"name":"kila","googlepaynum":7305331140,"type":"personal","account":"current account"},
           {"name":"lolo","googlepaynum":6384316771,"type":"personal","account":"saving  account"},
           {"name":"gracy","googlepaynum":9150381712,"type":"personal","account":"saving  account"},
           {"name":"grishma","googlepaynum":9003037517,"type":"personal","account":"saving  account"},
           {"name":"hari","googlepaynum":9515605233,"type":"personal","account":"saving  account"},
           {"name":"haripriya","googlepaynum":9791143754,"type":"personal","account":"saving  account"},
           {"name":"harikrishnan","googlepaynum":8056265597,"type":"personal","account":"saving  account"},
           {"name":"hema","googlepaynum":7010469081,"type":"personal","account":"saving  account"},
           {"name":"indumathi","googlepaynum":6379840455,"type":"personal","account":"current account"},
           {"name":"jaya","googlepaynum":9791280444,"type":"personal","account":"saving  account"},
           {"name":"jayadev","googlepaynum":8667639927,"type":"personal","account":"current account"},
           {"name":"jeevitha","googlepaynum":8667464628,"type":"personal","account":"saving  account"},
           {"name":"jemima","googlepaynum":9962821791,"type":"personal","account":"saving  account"},
           {"name":"jes","googlepaynum":9551852580,"type":"personal","account":"current account"},
           {"name":"jesintha","googlepaynum":8939475795,"type":"personal","account":"saving  account"},
           {"name":"jo","googlepaynum":7338935895,"type":"personal","account":"current account"},
           {"name":"joel","googlepaynum":9444919116,"type":"personal","account":"saving  account"},
           {"name":"jonnah","googlepaynum":8531025248,"type":"personal","account":"saving  account"},
           {"name":"josh","googlepaynum":9789869415,"type":"personal","account":"saving  account"},
           {"name":"jothika","googlepaynum":9677150962,"type":"personal","account":"saving  account"},
           {"name":"julaika","googlepaynum":9003899016,"type":"personal","account":"current account"},
           {"name":"jv","googlepaynum":9361486028,"type":"personal","account":"saving  account"},
           {"name":"kamali","googlepaynum":6382826039,"type":"personal","account":"saving  account"},
           {"name":"kamini","googlepaynum":9080995159,"type":"personal","account":"saving  account"},
           {"name":"kani","googlepaynum":8220584872,"type":"personal","account":"current account"},
           {"name":"kannan","googlepaynum":9710405288,"type":"personal","account":"current account"},
           {"name":"karthi","googlepaynum":8778799456,"type":"personal","account":"saving  account"},
           {"name":"kavitha","googlepaynum":9840042296,"type":"personal","account":"saving  account"},
           {"name":"keerthi","googlepaynum":7305066119,"type":"personal","account":"current account"},
           {"name":"kingsley","googlepaynum":8754554295,"type":"personal","account":"saving  account"},
           {"name":"kiran","googlepaynum":6383634327,"type":"personal","account":"current account"},
           {"name":"kiruthika","googlepaynum":9789029339,"type":"personal","account":"saving  account"},
           {"name":"kowsalya","googlepaynum":7871125838,"type":"personal","account":"saving  account"},
           {"name":"kowsi","googlepaynum":7448744931,"type":"personal","account":"current account"},
           {"name":"kumar","googlepaynum":7358565943,"type":"personal","account":"saving  account"},
           {"name":"lekha","googlepaynum":7305772128,"type":"personal","account":"saving  account"},
           {"name":"lokesh","googlepaynum":7358479530,"type":"personal","account":"saving  account"},
           {"name":"monisha","googlepaynum":6383188073,"type":"personal","account":"saving  account"},
           {"name":"madhan","googlepaynum":9940235467,"type":"personal","account":"current account"},
           {"name":"madhumitha","googlepaynum":7358602342,"type":"personal","account":"saving  account"},
           {"name":"madhuri","googlepaynum":9500771102,"type":"personal","account":"saving  account"},
           {"name":"maha","googlepaynum":9092042867,"type":"personal","account":"saving  account"},
           {"name":"maheswari","googlepaynum":9445891948,"type":"personal","account":"saving  account"},
           {"name":"malathi","googlepaynum":8754348244,"type":"personal","account":"current account"},
           {"name":"manni","googlepaynum":7395949407,"type":"personal","account":"saving  account"},
           {"name":"mannjula","googlepaynum":9751783763,"type":"personal","account":"saving  account"},
           {"name":"manoj","googlepaynum":7358160847,"type":"personal","account":"saving  account"},
           {"name":"mathu","googlepaynum":7550228649,"type":"personal","account":"saving  account"},
           {"name":"megna","googlepaynum":9620423983,"type":"personal","account":"current account"},
           {"name":"mohan","googlepaynum":8526264054,"type":"personal","account":"current account"},
           {"name":"moideen","googlepaynum":6381281050,"type":"personal","account":"saving  account"},
           {"name":"mrithula","googlepaynum":9840696542,"type":"personal","account":"saving  account"},
           {"name":"muthu","googlepaynum":8124263483,"type":"personal","account":"saving  account"},
           {"name":"mythili","googlepaynum":63830035506,"type":"personal","account":"saving  account"},
           {"name":"nabisha","googlepaynum":9094639197,"type":"personal","account":"saving  account"},
           {"name":"nivetha","googlepaynum":9150544355,"type":"personal","account":"current account"},
           {"name":"nourin","googlepaynum":7806906745,"type":"personal","account":"saving  account"},
           {"name":"padma","googlepaynum":9150961045,"type":"personal","account":"saving  account"},
           {"name":"panisha","googlepaynum":9676520865,"type":"personal","account":"saving  account"},
           {"name":"parimala","googlepaynum":7358470300,"type":"business","account":"current account"},
           {"name":"parveen","googlepaynum":8838105667,"type":"personal","account":"saving  account"},
           {"name":"pavithra","googlepaynum":6369772429,"type":"personal","account":"saving  account"},
           {"name":"philip","googlepaynum":9790830981,"type":"personal","account":"saving  account"},
           {"name":"pinky","googlepaynum":9489300189,"type":"personal","account":"saving  account"},
           {"name":"pooja","googlepaynum":8610129526,"type":"personal","account":"saving  account"},
           {"name":"prathi","googlepaynum":7397347695,"type":"personal","account":"current account"},
           {"name":"praveen","googlepaynum":9500079580,"type":"personal","account":"saving  account"},
           {"name":"preethi","googlepaynum":7708374654,"type":"personal","account":"saving  account"},
           {"name":"prem","googlepaynum":9344028505,"type":"personal","account":"saving  account"},
           {"name":"priya","googlepaynum":6369143345,"type":"personal","account":"current account"},
           {"name":"ragul","googlepaynum":9894190843,"type":"personal","account":"saving  account"},
           {"name":"rajesh","googlepaynum":7401790602,"type":"personal","account":"saving  account"},
           {"name":"ramya","googlepaynum":9840430478,"type":"personal","account":"saving  account"},
           {"name":"regina","googlepaynum":9840860014,"type":"personal","account":"current account"},
           {"name":"reshma","googlepaynum":7448729790,"type":"personal","account":"saving  account"},
           {"name":"rohini","googlepaynum":6380874698,"type":"personal","account":"current account"},
           {"name":"sabitha","googlepaynum":9361447138,"type":"personal","account":"saving  account"},
           {"name":"sagarika","googlepaynum":7358701090,"type":"personal","account":"saving  account"},
           {"name":"sameera","googlepaynum":6382718022,"type":"personal","account":"saving  account"},
           {"name":"sandhiya","googlepaynum":6383138140,"type":"personal","account":"current account"},
           {"name":"sangeetha","googlepaynum":7904104077,"type":"personal","account":"saving  account"},]
            

for i in googlepay:                                                                                                             #LOOPING
    for j,k in i.items():
        print(f"{j}:{k}")

   
        
        

    

