    #  code for creating an electricity bill , with the following conditions :
    #     000-100 units: Free
    #     101-200 units: ₹4
    #     201-300 units: ₹7
    #     301-400 units: ₹9
    #     401-500 units: ₹10 
    #     above 500 units: ₹15
    
def calc_bill (units):
    total =0
    units-=100
    amount = [4,7,9,10,15]      # list of the amounts needed , using the iterative statements.
    idx=0                                
    for _ in range(units):
        if units >100 :
            if idx==4:
                total += units *amount[-1]
                break
            units-=100
            total +=100*amount[idx]
            idx+=1
        else : 
            total += units * amount[idx]
            break
    return total 
    

units=int(input("What is the amount of electricity consumed: "))
if units <=100 :
        print("Your bill is Free .")
        
total= calc_bill(units)

print ("Your bill is ₹",total,". ")
        
    