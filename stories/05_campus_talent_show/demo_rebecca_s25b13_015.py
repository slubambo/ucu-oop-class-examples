from story import Comedy, TalentShow, audition

def main():
    print("=== COMEDY DUO ===")
    comedy = Comedy("Campus Comedy Duo")
    print("\n=== AUDITION ===")
    acts = [comedy]
    audition(acts)
    
    print("\n=== TEST 1: SUCCESSFUL BOOKING ===")

    joel = TalentShow("Joel", 8)
    print("Expected: MC Joel books Campus Comedy Duo.")
    print("Actual:", joel.book(comedy))

    print("Expected remaining minutes: 6")
    print("Actual remaining minutes:", joel.clock.remaining)

    #TEST 2: UNSUCCESSFUL BOOKING
    print("\n=== TEST 2: REFUSED BOOKING ===")
    faith = TalentShow("Faith", 1)
    
    print("Expected: Booking rejected")
    print("Actual:", faith.book(comedy))

    print("Expected remaining minutes: 1")
    print("Actual remaining minutes:", faith.clock.remaining)

if __name__ == "__main__":
    main()
