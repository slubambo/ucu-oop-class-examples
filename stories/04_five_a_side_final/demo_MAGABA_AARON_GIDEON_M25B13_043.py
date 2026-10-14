from story import LongPass, Match, discuss_tactics


#Check 1: the tacticcs loop works with the new attack.
print("---Check 1: describe through the tactics loop ---")
discuss_tactics([LongPass("Long pass to the wing")])
print("Expected: Mukono Meteors: Long pass to the wing needs 15 energy")


# Check 2 (normal case): enough energy
print("---Check 2: normal case ----")
match = Match("Brian", 35)
print(match.play(LongPass("Long pass to the wing")))
print("Expected energy: 20, actual:", match.energy.remaining)
print("Expected actions: 1, actual:", match.completed_actions)


# Check 3 (refused case): not enough energy
print("---Check 3: refused case ----")
tired = Match("Ruth", 10)
print(tired.play(LongPass("Long pass to the wing")))
print("Expected energy: 10, actual:", tired.energy.remaining)
print("Expected actions: 0, actual:", tired.completed_actions)


