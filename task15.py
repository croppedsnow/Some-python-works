from typing import List

from pandas.util.version import Infinity


def hello(name: str = None) -> str:
    if (name == None) or (name == ""):
        return "Hello!"
    else:
        return "Hello, " + name + "!"


def int_to_roman(num: int) -> str:
    s = "M" * (num // 1000)
    num -= (num // 1000) * 1000
    spis9 = ["IX", "XC", "CM"]
    spis4 = ["IV", "XL", "CD"]
    spis5 = ["V", "L", "D"]
    spis1 = ["I", "X", "C"]
    for i in range(2, -1, -1):
        if num // 10 ** i == 9:
            s += spis9[i]
            num -= 9 * 10 ** i
        elif num // (5 * 10 ** i) == 1:
            s += spis5[i]
            num -= 5 * 10 ** i
        if num // 10 ** i == 4:
            s += spis4[i]
            num -= 4 * 10 ** i
        else:
            s += spis1[i] * (num // 10 ** i)
            num -= (num // 10 ** i) * 10 ** i
    return s


def longest_common_prefix(strs_input: List[str]) -> str:
    if len(strs_input) == 0:
        return ""
    ret_s = strs_input[0].lstrip()
    for i in range(1, len(strs_input)):
        next_s = strs_input[i].lstrip()
        t = min(len(ret_s), len(next_s))
        for j in range(0, t):
            if ret_s[j] != next_s[j]:
                t = j
                break
        ret_s = ret_s[:t]
        if ret_s == "":
            return ""
    return ret_s




def primes() -> int:
    spis_primes = []
    p = 2
    while True:
        flag = 1
        for i in range(0, len(spis_primes)):
            if p % spis_primes[i] == 0:
                flag = 0
        if flag:
            spis_primes.append(p)
        else:
            p += 1
            continue
        yield p
        p += 1


class BankCard:
    def __init__(self, total_sum: int, balance_limit: int = -1):
        self.total_sum = total_sum
        self.balance_limit = balance_limit

    def __call__(self, sum_spent):
        if sum_spent > self.total_sum:
            print("Not enough money to spend sum_spent dollars.")
            raise ValueError("Not enough money to spend sum_spent dollars.")
        else:
            self.total_sum -= sum_spent
            print(f"You spent {sum_spent} dollars.")

    @property
    def balance(self):
        if self.balance_limit == 0:
            print("Balance check limits exceeded.")
            raise ValueError("Balance check limits exceeded.")
        self.balance_limit -= 1
        return self.total_sum

    def __repr__(self):
        return "To learn the balance call balance."

    def put(self, sum_put: int):
        self.total_sum += sum_put
        print(f"You put {sum_put} dollars.")

    def __add__(self, other):
        if self.balance_limit < 0 or other.balance_limit < 0:
            bal_limit = -1
        else:
            bal_limit = max(self.balance_limit, other.balance_limit)
        return BankCard(self.total_sum + other.total_sum, bal_limit)


