"""
link: https://www.reddit.com/r/dailyprogrammer/comments/nucsik/20210607_challenge_393_easy_making_change/

The country of Examplania has coins that are worth 1, 5, 10, 25, 100, and 500 currency units. At the Zeroth Bank of
Examplania, you are trained to make various amounts of money by using as many ¤500 coins as possible, then as many ¤100
coins as possible, and so on down.

For instance, if you want to give someone ¤468, you would give them four ¤100 coins, two ¤25 coins, one ¤10 coin, one ¤5
coin, and three ¤1 coins, for a total of 11 coins.

Write a function to return the number of coins you use to make a given amount of change.

```
change(0) => 0
change(12) => 3
change(468) => 11
change(123456) => 254
```

(This is a repost of Challenge #65 [easy], originally posted by u/oskar_s in June 2012.)
"""
from typing import Tuple


# I added the coin_types argument to have a functional solution using recursion
def change(amount: int, coin_types: Tuple[int, ...]) -> int:
    return (
        amount
        if len(coin_types) == 1
        else amount // coin_types[0]
        + change(amount=amount % coin_types[0], coin_types=coin_types[1:])
    )


def challenge():
    coin_types: Tuple[int, ...] = 500, 100, 25, 10, 5, 1
    print(change(amount=0, coin_types=coin_types))
    print(change(amount=12, coin_types=coin_types))
    print(change(amount=468, coin_types=coin_types))
    print(change(amount=123456, coin_types=coin_types))


challenge()
