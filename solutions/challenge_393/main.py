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

import click
from typing import Tuple


def change(amount: int) -> int:
    coin_types: Tuple = 500, 100, 25, 10, 5, 1
    coins: int = 0
    for coin_type in coin_types:
        coins += amount // coin_type
        amount = amount % coin_type
    return coins


@click.command()
@click.argument("amount", type=int)
def main(amount: int):
    print(change(amount=amount))


if __name__ == "__main__":
    main()
