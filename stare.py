def ways(stairs):
    if stairs < 0:
        return 0
    if stairs==0:
        return 1
    twostep =0
    onestep =0
    if stairs>=2:
        twosteps= ways (stairs-2)
