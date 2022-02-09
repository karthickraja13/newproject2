        #############  FUNCTION CALLIING  ########

def sub():
	print("welcome to my tutorial")
sub()
       
       ######### argument #########
def sub1(sub):
       	print(sub+"this a comman subject")
sub1("tamil\t")
sub1("english\t")

       ######### number function ########

def sub(key,valus):
   print(key+""+valus)
sub("name:","raja")
sub("age:","23")


    ###########  Arbitrary argument *args   #############
def sub(*name):
    print(name[2])
sub("karthick","mohan","mani","prathi")        

      ###########   keyword argument ###########
def sub(name,subject,amount):
	print(name)
sub(name="karthick",subject="python",amount=2000)      


           ##########  **kwargs  ########

def name(**list):
        print(list["lname"])
name(fname="karthick",lname="mayavan") 


      #############  default parameter  ###############

def name(namelist="raja"):

	print(namelist)

name("karthick")
name("prathi")
name()


            #########  passing a list as an argument  ###########

def subject(lit):
	for x in lit:
		print(x)
data=["raja","ram","karthick","mohan"]
subject(data)   

    ###############  return ############
def list(name):
        return 4 * name
print(list(1))   
print(list(5))
print(list(78))
print(list(23))