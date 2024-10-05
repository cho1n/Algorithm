N = int(input())
colors = list(map(str, input()))
B_count = R_count = 0
start_inx = colors[0]

for l in range(1, N):
    if start_inx == 'B' and start_inx != colors[l]:
        B_count += 1
        start_inx = 'R'
    elif start_inx == 'R' and start_inx != colors[l]:
        R_count += 1
        start_inx = 'B'
        
if colors[-1] == 'B':
    B_count += 1
else:
    R_count += 1
            

if B_count > R_count:
    print(R_count + 1)
else:
    print(B_count + 1)     