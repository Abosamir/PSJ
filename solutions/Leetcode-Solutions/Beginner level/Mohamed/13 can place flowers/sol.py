def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
    flowerbed.insert(0,0)
    flowerbed.append(0)

    plant = 0
    can_place = 0
    for i in flowerbed:
        if i == 0:
            plant += 1
        else:
            plant = 0
        
        if plant == 3:
            can_place += 1
            plant = 1
    
    return can_place >= n


print(canPlaceFlowers("f",[1,0,0,0,1],2))


