# Pronto
# https://a2oj.com/p?ID=127

n,m = input("Enter board dimensions").split(",")

n=int(n)
m=int(m)

if(n%2==0 or m%2==0): # Pronto is played on a rectangular board of n x m dimensions, with pieces of 2x2 dimensions.
    # So, either n or m has to be even so that the player who starts can also win the game
    print("I can win :)")
else:
    print("Maybe :(")
