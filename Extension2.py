
def extend(self, minutes):
    if minutes <= 0:
        return False

    self.__remaining += minutes
    return True

clock = ShowClock(8)

print(clock.remaining)  # 8

print(clock.extend(5))  # True
print(clock.remaining)  # 13

print(clock.extend(0))  # False
print(clock.remaining)  # 13

print(clock.extend(-2)) # False
print(clock.remaining)  # 13