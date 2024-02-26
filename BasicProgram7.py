#python program to find total amount of money in piggy bank, the coin should be rs.5, rs.10, rs.2 and rs.1 coins.

rs1 = (int(input("Enter the Number of Rs.1 coins : ")))
rs2 = (int(input("Enter the Number of Rs.2 coins : ")))
rs5 = (int(input("Enter the number of rs.5 coins :")))
rs10 = (int(input("Enter the number of rs.10 coins : ")))

totalAmount = 1*rs1 + 2*rs2 + 5*rs5 + 10*rs10

print("Total amount found or saved in piggy bank is : ", totalAmount)