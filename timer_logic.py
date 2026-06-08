WEIGHTS = {
    2: 1,    # Car
    3: 0.5,  # Bike
    5: 3,    # Bus
    7: 3,    # Truck
}
def calculate_score(vehicles, wait_time, emergency=False):#vehicles = list of class_ids[2, 2, 5, 7, 3] jaise Function WEIGHTS se khud weight nikalega!
    if len(vehicles) == 0:
        return 0
    if emergency:
        return 9999
    if wait_time > 45:
        return 8888
    total_weight = sum(WEIGHTS.get(v, 1) for v in vehicles)
    avg_weight = total_weight / len(vehicles) if vehicles else 1
    count = len(vehicles)
    score = (count * avg_weight * 1.5) + (wait_time * 2)
    return score

def get_green_time(score):
    if score ==9999:
        return 60
    elif score == 8888:
        return 45
    base_time = 15
    max_time = 60
    calculated_time = base_time + (score*0.4)
    return min(int(calculated_time), max_time)

def get_signal_color(score):
    # Task 1: Agar score 8888 se bada ya barabar (>=) hai, toh return karo "CRITICAL GREEN (Priority Queue)"
    if score>=8888:
        return  "CRITICAL GREEN (Priority Queue)"
    # Task 2: Agar score ekdam 0 hai (Empty Road), toh return karo "RED (No Traffic)"
    elif score==0:
        return "RED"
    # Task 3: Agar score 0 se bada hai aur 20 se chota ya barabar (<= 20) hai, toh return karo "YELLOW (Low Traffic Density)"
    elif score >0 and score<=20:
        return "YELLOW (Low Traffic Density)"
    else:
        return "GREEN"











