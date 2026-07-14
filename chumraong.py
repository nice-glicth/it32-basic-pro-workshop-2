# Gun = "1000"
# Cost_price = "10000"
quality = int(input("จำนวนปืน ") )


cost_price = ( quality * 10000 )
sell_price = ( quality * 12000 )
boss = ( sell_price / 5 )

ลูกน้อง = int(input("จำนวนลูกน้อง ") )

รายได้ลูกน้อง = ( sell_price - boss ) / ลูกน้อง



print("Cost Price:", cost_price)
print("Sell Price:", sell_price)
print("รายได้ลูกน้อง:", รายได้ลูกน้อง)
print("Profit:", boss)


