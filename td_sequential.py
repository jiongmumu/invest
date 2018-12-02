def td_sequential(close, high):
    TDSL = 0
    TDSS = 0
    BuySetup = 0
    SellSetup = 0
    BuyCountdown = 0
    SellCountdown = 0

    if close[1] > close[5] and close < close[4]:
    bearishflip = 1
    bullishflip = 0
    else if close[1] < close[5] and close > close[4]:
    bullishflip = 1
    bearishflip = 0

    if close < close[4] and bearishflip:
    TDSL = TDSL + 1
    TDSS = 0
    else if close > close[4] and bullishflip:
    TDSS = TDSS + 1
    TDSL = 0

    if TDSL > 0 and TDSL < 10:
    print("#TDSL#", barindex, low - 10 * pipsize)  #

    if TDSL=9:
    L = (low < low[3] and low < low[2]) or (low[1] < low[2] and low[1] < low[3])
    bearishflip = 0
    TDSL = 0
    BuySetup = 1
    if L:
    DRAWARROWUP(barindex, low - 20 * pipsize)

    if TDSS > 0 and TDSS < 10:
    print("#TDSS#", barindex, high + 10 * pipsize)

    if TDSS=9:
    S = (high > high[2] and high > high[3]) or (high[1] > high[3] and high[1] > high[2])
    bullishflip = 0
    TDSS = 0
    SellSetup = 1
    if S:
    DRAWARROWDOWN(barindex, high + 20 * pipsize)

    if BuySetup:
    if close <= low[2]:
    BuyCountdown = BuyCountdown + 1
    print("#BuyCountdown#", barindex, low - 10 * pipsize)

    if BuyCountdown=8:
    Bar8 = barindex
    else if BuyCountdown=13: // TD Countdown perfection buy
    if low <= close[barindex - Bar8]:
    DRAWARROWUP(barindex, low - 20 * pipsize)

    BuySetup = 0
    BuyCountdown = 0

    else if SellSetup:
    if close >= high[2]:
    SellCountdown = SellCountdown + 1
    print("#SellCountdown#", barindex, high + 10 * pipsize)

    if SellCountdown=8:
    Bar8 = barindex
    else if SellCountdown=13: // TD Countdown perfection sell
    if high >= close[barindex - Bar8]:
    DRAWARROWDOWN(barindex, high + 20 * pipsize)

    SellSetup = 0
    SellCountdown = 0

    return
