#Demo File Nambuya Gloria- S26B13/102 B40321
#Extension 3: Testing the top_up method of LunchWallet class and price method of FreeBanana class

import importlib
import sys
import os
import importlib
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.insert(0, repo_root)

module = importlib.import_module("stories.01_rolex_rescue.story")   
LunchWallet = module.LunchWallet
FreeBanana = module.FreeBanana

#Check 1: Normal case
Wallet = LunchWallet(50)
input1 = Wallet.top_up(20)
print(f"input:Wallet.top_up(20)")
print(f"Expected: True and balance = 70")

#Check FreeBanana
Banana = FreeBanana()
print(f"input: FreeBanana().price")
print(f"Expected: 0")
print(f"balance: {Banana.price()}")

#check top_up with negative
Wallet = LunchWallet(50)
input2 = Wallet.top_up(-50)
print(f"input:Wallet.top_up(-50)")
print(f"Expected: False , balance stays at 50")
print(f"balance: {Wallet.balance}")








