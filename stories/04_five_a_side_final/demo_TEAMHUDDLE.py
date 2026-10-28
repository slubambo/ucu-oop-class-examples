from story import TeamHuddle, Match, discuss_tactics

print("--- Check 1: Tactics loop ---")
discuss_tactics([TeamHuddle()])

print("--- Check 2: Normal match ---")
match = Match("Brian", 35)
print(match.play(TeamHuddle()))
print("Expected energy: 35; Actual:", match.energy.remaining)
print("Expected actions: 1; Actual:", match.completed_actions)

print("--- Check 3: Zero-energy match ---")
tired = Match("Ruth", 0)
print(tired.play(TeamHuddle()))
print("Expected energy: 0; Actual:", tired.energy.remaining)
print("Expected actions: 1; Actual:", tired.completed_actions)