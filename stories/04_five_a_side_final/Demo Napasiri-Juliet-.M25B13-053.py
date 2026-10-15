from story import TrainedDribble, Match, discuss_tactics

# Action 1: tactics loop works with the new attack
print("---Action 1: describe through the tactics loop ---")
discuss_tactics([TrainedDribble("Brian")])
print("Expected:Mukono Meteors: Brian's dribble needs 15 energy points")


# Action 2 (normal scenario): enough energy points
print("---Action 2: normal scenario---")
match = Match("Brian", 35)
print(match.play(TrainedDribble("Brian")))
print("Expected energy: 20, actual:", match.energy.remaining)
print("Expected actions: 1, actual:", match.completed_actions)

# Action 3 (refused scenario): not enough energy point
print("---Action 3: refused scenario---")
tired = Match("Ruth", 10)
print(tired.play(TrainedDribble("Ruth")))
print("Expected energy: 10, actaul:", tired.energy.remaining)
print("Expected actions: 0, actual:", tired.completed_actions)
