def cancel_last(self):
    if not self.acts:
        return False


    last_act = self.acts.pop()
    self.clock.reserve(-last_act.duration())
    return True


clock = ShowClock(8)
show = TalentShow(clock)

show.book(HeadlineDance("Joel"))
show.book(Poetry("Joel"))

print(clock.remaining)

print(show.cancel_last())
print(clock.remaining)

print(show.cancel_last())
print(clock.remaining)

print(show.cancel_last())
print(clock.remaining) 