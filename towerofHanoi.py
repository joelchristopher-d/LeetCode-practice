def towerofHanoi(discCount,fromm,mid,to):
    if discCount == 1:
        print(f"Move the {discCount} from {fromm} to {to}")
        return
    towerofHanoi(discCount-1,fromm,to,mid)
    print(f"Movee the {discCount} from {fromm} to {to}")
    towerofHanoi(discCount-1,mid,to,fromm)

towerofHanoi(3,1,2,3)
