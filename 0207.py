h, m = map(int, input().split())
time = int(input())

add_min = m + time

add_hour = add_min//60
current_h = (h + add_hour)%24

current_m = add_min%60

current_t = [current_h, current_m]

print(f"{current_h} {current_m}")