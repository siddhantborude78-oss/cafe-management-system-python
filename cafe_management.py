#Hottel Menu managment system
print("::::::::::::CAFE MANAGMENT SYATEM::::::::::::")
#1.create dictionary
menu={'pizza':50,
'burger':60,
'coffee':20,
'cold_coffee':30,
't6ea':10,
'pavbhaji':60,
'misal_pav':70,
'vadapav':15,
'water_bottel':12,
'cold_drink':30,
'nonveg':200,
'milk_lassi':30
}
total_price=0 #create empty box

#create managment 
print("WELLCOME")
print(".......WELLCOME")
print("..............WELLCOME")
print("WELLCOME TO ....SHIV-KAILAS CAFE")

#menu
print("Here is menu")
print("pizza:50₹")
print("burger:60₹")
print("coffee:20₹")
print("cold_coffee:30₹")
print("Tea:10₹")
print("pavbhaji:60₹")
print("misal_pav:70₹")
print("vadapav:15₹")
print("water_bottel:12₹")
print("cold_drink:30₹")
print("nonveg:200₹")
print("milk_lassi:30₹")
print(".........<..........>")
#user input and if condition
item1=input("enter a item you want to order :").lower()
if item1 in menu:
	total_price+=menu[item1]
	print(f"your item {item1} is added your order")
else:
	print(f"your item {item1} is not available in our hottel...please enter a item in menu")
another_order=input("Do you add another item in order enter (yes/no) :").lower()
if another_order=="yes":
	item2=input("enter another item you want to add :").lower()
	if item2 in menu:
		total_price+=menu[item2]
		print(f"your item {item2}is added in your order")
	else:
		print(f"your item {item2} is not available in our hottel.  plaease enter a item in menu")	  	  
else:
	print("ohkk")
#THANK YOU.....
print(f"total cost is {total_price}...please pay ")
print ("THANK YOU...")
print("PLEASE VISIT AGAIN")
print("TACK CARE")