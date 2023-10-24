tab=[]

# Customer names
client_1 ="Anas Jbara"
client_2 ="Ali Mohammed"
client_3 ="Madani Brahim"

#VAT rate and discount
TVA = 0.15
Remise = 0.02

# Generate invoices for each customer
for i in range(1,4) :
     n = int(input(f"Give the item number for customer {i}: ")) 
     for j in range(1,n+1) :
          x = int(input(f"Give the price of the item {j}: "))
          tab.append(x)
     r = sum(tab)*(1+TVA)*(1-Remise)
     print("--------------")
     print("Facture")
     print("--------------")
     print(f"The Total to be paid for the customer {i} is : ",r)
     tab.clear()