#Write a program to create two classes for two different 
# countries that consist of three methods to
# display the following information of respective country capital, 
# language and type of country. Then, use Polymorphism to
# create a common interface for both classes.




class Turkey:
    def capital(self):
        print("ankara is the capital of turkey")
    def languge(self):
        print("turkish is turkeys languge")
    def type(self):
        print(" turkey is a republic ")
class Japan:
    def capital(self):
        print("tokyo was the second capital but before it was heorshima")
    def  languge(self):
        print(" the languge is japanese")
    def type(self):
        print(" japan is a constitutional monarchy contry")
        
Tobj=Turkey()
Jobj=Japan()
for c in (Tobj,Jobj):
    c.capital()
    c.type()
    c.languge()