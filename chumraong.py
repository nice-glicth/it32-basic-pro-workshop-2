
quality = int(input("จำนวนปืน ") )
cost = int(input("ราคาต้นทุนต่อปืน :") )
sell = int(input("ราคาขายต่อปืน :") )

cost_price = ( quality * cost )
sell_price = ( quality * sell )
income = ( sell_price - cost_price )
boss = ( income * 0.2 )

Hanchman= int(input("จำนวนลูกน้อง ") )

hanchman = ( income - boss ) / Hanchman



print("Cost Price:", cost_price)
print("Sell Price:", sell_price)
print("รายได้ลูกน้อง:", hanchman)
print("Boss:", boss)
print("Profit:", income)


