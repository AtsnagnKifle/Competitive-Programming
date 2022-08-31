def countingValleys(steps, path):
    # Write your code here
    # UDDDUDUU
    sea_lvl = 0
    tot_val = 0
    for char in path:
        if char == "U":
            sea_lvl += 1
        else:
            if not sea_lvl:
                tot_val += 1
                sea_lvl -= 1
            else:
                sea_lvl -= 1

    return tot_val
