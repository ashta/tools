import re
import sys
# The case where odds are given as fractions

def readOdds(inputOdds):

    if '/' in inputOdds:
        [numer, denom] = list(map(float, inputOdds.split('/')))
        payout = 100 + (numer*100/denom)
        print("The payout on a $100 bet is ${:.2f}".format(payout))

    elif '+' or '-' in inputOdds:
        if '+' in inputOdds:
            odds = float(inputOdds[1:])
            payout = 100 + odds
            print("The payout on a $100 bet is ${:.2f}".format(payout))
        elif '-' in inputOdds:
            odds = float(inputOdds[1:])
            payout = 100 + 100*(100/odds)
            print("The payout on a $100 bet is ${:.2f}".format(payout))


if __name__ == "__main__":
    readOdds(sys.argv[1])
