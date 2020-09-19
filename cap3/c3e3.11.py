#Make a program that request the price of the merchandise and the percentage of the discount.Show the value of the discount and the price to pay
price=float(input("Type the price of the merchandise: "))
discount=float(input("Type the percentage of the discount: "))
discvalue=price*(discount/100)
nprice=price-discvalue
print(f"The value of the discount is {discvalue}% and the price to pay is ${nprice}")