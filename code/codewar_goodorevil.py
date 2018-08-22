def goodVsEvil(good, evil):
    good_dict = {
        '0' : 1,
        '1' : 2,
        '2' : 3,
        '3' : 3,
        '4' : 4,
        '5' : 10
        }
    evil_dict = {
        '0' : 1,
        '1' : 2,
        '2' : 2,
        '3' : 2,
        '4' : 3,
        '5' : 5,
        '6' : 10
        }
    good = good.split()
    evil = evil.split()
    good_value = 0
    evil_value =0
    print(good)
    print(evil)
    for i in good:
        good_value += good_dict[str(good.index(i))] * int(i)
        print(good_value)
    print(good_value)
    for j in evil:
        evil_value += evil_dict[str(evil.index(j))] * int(j)
        print(evil_value)
    print(evil_value)
    if good_value > evil_value:
        return 'Battle Result: Good triumphs over Evil'
    elif good_value < evil_value:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'
print(goodVsEvil('1 0 0 0 1 0', '0 0 0 0 0 1 0'))
