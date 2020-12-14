verifier = True
bids={}
while verifier:
    name=input(("Put a name: "))
    bid=int(input("Put a bid: "))
    bids[name]=bid
    decision=input("If you'd like to continue type yes else no :")
    if decision == "no":
        verifier = False
for names in bids:
    valu=0
    x=int(bids[names])
    if x > valu:
        valu=bid
        winner=names

print(f"{winner} is the winner")