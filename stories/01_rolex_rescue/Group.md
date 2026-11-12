# GROUP.md: The Rolex Rescue

## Members(Quick Group)

Member              GitHub        Reg.number 

Feta Jordan  Jordancode-cyber S26B13/131 
Nambuya Gloria  NambuyaGloria S26B13/102 
Atukunda lynn atukundalynn  S26B13/123 
Ankunda Claire  ClaireAnkunda  S26B13/130


## Later-topic options chosen (recorded before coding)

**A1, A2 and A4.**

| Option | Topic | Member responsible | PR |

| A1 | Values that can print, compare and add (Week 7) | atukundalynn | https://github.com/Jordancode-cyber/ucu-oop-class-examples/pull/9 |
| A2 | Errors the story can explain (Week 8) | NambuyaGloria | https://github.com/Jordancode-cyber/ucu-oop-class-examples/pull/10 |
| A4 | Factory, clearer responsibilities and tests (Weeks 9-10) | Jordancode-cyber | https://github.com/Jordancode-cyber/ucu-oop-class-examples/pull/11 |

The three options are independent. A1 gives the story a money value, A2 adds
strict buying with named errors, and A4 creates choices through a factory.
Any of them works without the other two.

---

## A1: Values that can print, compare and add

- **Members responsible:** atukundalynn
- **PR:** https://github.com/Jordancode-cyber/ucu-oop-class-examples/pull/9
- **Demo command:** `py -3 .\stories\01_rolex_rescue\demo_a1.py`
- **Check command:** `py -3 .\stories\01_rolex_rescue\test_a1.py`
- **Explanation:** `LunchMoney` is a value object for UGX. It accepts only
  non-negative whole numbers (negatives, fractions and Booleans are refused)
  and has a read-only `amount` property. `__str__` gives the friendly display,
  `__repr__` the developer display, `__eq__` compares amounts, and `__add__`
  returns a NEW `LunchMoney` without changing either original. For an
  unsupported operand these methods return `NotImplemented`. `LunchBreak`
  gets `preview_total(choices)`, which sums the `price()` of each choice as a
  `LunchMoney`. An empty list gives zero, and a preview never spends money or
  changes history.
- **Cases covered:** normal (display, equality, addition, unchanged operands),
  boundary (zero amount, empty preview) and invalid/refused (bad amounts,
  unsupported operands).

## A2: Errors the story can explain

- **Members responsible:** NambuyaGloria
- **PR:** https://github.com/Jordancode-cyber/ucu-oop-class-examples/pull/10
- **Demo command:** [exact command, using try / specific except / finally]
- **Check command:** [exact command for the test file in the PR]
- **Explanation:** Three custom exceptions derive from `Exception`:
  `LunchChoiceError` (no choice, `None`), `LunchRequestError` (an invalid
  quote such as negative, fractional or Boolean) and `LunchResourceError`
  (valid quote, not enough UGX). `StrictLunchBreak.safe_buy(choice)` checks
  all of this BEFORE spending or recording anything, then delegates to the
  original `LunchBreak.buy()`. `StrictLunchBreak` has-a `LunchBreak`
  (composition), so validation stays separate from buying and the original
  `LunchBreak` is unchanged. A zero-cost choice such as `HomePackedLunch` is
  valid and is not confused with a missing choice. A broken `price()` is not
  hidden; its error propagates to the caller. `bool` is rejected explicitly
  because `True` is an `int` in Python.
- **Cases covered:** the three exception types, each proving the balance and
  completed count are unchanged after failure, plus a successful purchase.

## A4: A small factory, clearer responsibilities and tests

- **Members responsible:** Jordancode-cyber
- **PR:** https://github.com/Jordancode-cyber/ucu-oop-class-examples/pull/11
- **Demo command:** `python3 a4_demo_advanced_ext.py` (Windows: `py -3 a4_demo_advanced_ext.py`)
- **Test command (from the main repository folder):**
  `py -3 -m unittest discover -s stories/01_rolex_rescue -p "test_*.py"`
  (macOS/Linux: `python3 -m unittest discover -s stories/01_rolex_rescue -p "test_*.py"`)
- **Explanation:** `create_choice(key, **settings)` in `a4_later_topics.py`
  creates `Rolex`, `Kikomando` and `HomePackedLunch`. Unknown keys and invalid
  settings (such as negative egg counts or wrong types) raise `ValueError` or
  `TypeError`. Callers use the returned object's existing interface, so the
  coordinator needs no branch per class.
- **Single Responsibility:** [state which responsibility moved, for example
  "choice creation moved out of `main()` into the factory, while resource
  spending stays in `LunchWallet`", and why]
- **Tests:** [list the at least six `unittest` tests and the file name]

---

## Who contributed what

| Member | Branch | Later-topic PR | Contribution |

Jordancode-cyber - A4 factory, demo and tests
NambuyaGloria - A2 exceptions, `safe_buy` and tests
atukundalynn - A1 `LunchMoney`, `preview_total` and tests 
Ankunda Claire - Group.md file

## PR review comments

Every PR needs useful comments from all the other members before merge.

| PR | Commented by |
| #9 | [Atukunda Lynn,Nambuya Gloria, Ankunda Claire, Feta Jordan, Asango Joan] 
| #10 | [Atukunda Lynn,Nambuya Gloria, Ankunda Claire, Feta Jordan, Asango Joan] 
| #11 |  [Atukunda Lynn,Nambuya Gloria, Ankunda Claire, Feta Jordan, Asango Joan] 
