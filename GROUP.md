# Later-topic extensions: Five-a-Side Final

Ch: A1, A2, A4

## A1: Values that can print, compare and add (Week 7)
- Members responsible: MAGABA AARON GIDEON M25B13/043, 
- Merged PRs: https://github.com/slubambo/ucu-oop-class-examples/pull/85 (EnergyAmount class)
- Demo command: py -3 stories/04_five_a_side_final/demo_a1_energy_amount.py
- Check command: py -3 stories/04_five_a_side_final/check_a1_energy_amount.py
- Explanation: EnergyAmount holds a non-negative whole number of energy and refuses negatives, fractions and Booleans. It has a friendly __str__ ("3,000 energy"), a developer __repr__ ("EnergyAmount(3000)"), __eq__ and __add__. Adding returns a new EnergyAmount and leaves both operands unchanged. Unsupported operand types return NotImplemented (not NotImplementedError). Match.preview_total(choices) asks each choice for effort() and returns the combined EnergyAmount without spending resources or changing history. Added custom exceptions to handle invalid energy, negative attack costs, and insufficient energy. Included a demo and five tests to check the code.

## A2:  Exception Handling
- Members responsible: Resty Abiko M25B13/044, NAPASIRI JULIET M25B13/053
- Merged PRs: https://github.com/slubambo/ucu-oop-class-examples/pull/87
- Explanation:Added MatchChoiceError, MatchRequestError, and MatchResourceError.
Implemented StrictMatch.safe_play() to validate choices and effort before calling the existing Match.play() method.
Added automated tests for missing choices, invalid effort, insufficient energy, successful actions, and preservation of match state after failures.

 

## A4: A small factory, clearer responsibilities and tests (Weeks 9-10)
- Members responsible: Martha Rita Aber  B33225
- Merged PRs: 
- Explanation:
