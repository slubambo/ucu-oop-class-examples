from story import Comedy, TalentShow, audition
print("=== EXTENSION 1: COMEDY DUO ===")
comedy = Comedy("Blair and Lawrence")

print("Expected duration: 2 minutes")
print("Actual duration:", comedy.duration())

print("\nAudition:")
audition([comedy])

print("\nNormal booking:")
show = TalentShow("Blair", 2)
print(show.book(comedy))

print("Expected acts: 1")
print("Actual acts:", show.act_count)

print("Expected minutes left: 0")
print("Actual minutes left:", show.clock.remaining)

print("\nBoundary case: another comedy act has no available time")
another_comedy = Comedy("The Late Comedians")
print(show.book(another_comedy))

print("Expected acts: 1")
print("Actual acts:", show.act_count)

print("Expected minutes left: 0")
print("Actual minutes left:", show.clock.remaining)