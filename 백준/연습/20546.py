j_money = int(input())
h_money = j_money

stock_price = list(map(int, input().split()))
j_stock, h_stock = 0, 0
up_count, down_count = 0, 0

for i in range(len(stock_price)):
        
    if stock_price[i] <= j_money:
        while stock_price[i] <= j_money:
            j_stock += 1
            j_money -= stock_price[i]
    
    if i > 0:
        if stock_price[i-1] > stock_price[i]:
            down_count += 1
            up_count = 0
            if down_count >= 3:
                if stock_price[i] <= h_money:
                    while stock_price[i] <= h_money:
                        h_stock += 1
                        h_money -= stock_price[i]
                        
        elif stock_price[i-1] < stock_price[i]:
            up_count += 1
            down_count = 0
            if up_count >= 3:
                if h_stock != 0:
                    h_money += h_stock * stock_price[i]
                    h_stock = 0            
        else:
            down_count, up_count = 0, 0
        

if j_stock != 0:
    j_money += stock_price[-1] * j_stock
if h_stock != 0:
    h_money += stock_price[-1] * h_stock    
    
if j_money > h_money:
    print("BNP")
elif h_money > j_money:
    print("TIMING")
else:
    print("SAMESAME")