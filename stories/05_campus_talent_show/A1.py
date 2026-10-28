"""A1: represent stage time as a validated, printable, addable value."""

from story import AudienceWave, Dance, HeadlineDance, Poetry
from story import TalentShow as FoundationTalentShow


class StageTime:
	"""A non-negative whole number of minutes."""

	__slots__ = ("__amount",)

	def __init__(self, amount):
		if isinstance(amount, bool) or not isinstance(amount, int):
			raise TypeError("Stage time must be a whole number of minutes.")
		if amount < 0:
			raise ValueError("Stage time cannot be negative.")
		self.__amount = amount

	@property
	def amount(self):
		return self.__amount

	def __str__(self):
		return f"{self.amount:,} minutes"

	def __repr__(self):
		return f"StageTime({self.amount})"

	def __eq__(self, other):
		if not isinstance(other, StageTime):
			return NotImplemented
		return self.amount == other.amount

	def __add__(self, other):
		if not isinstance(other, StageTime):
			return NotImplemented
		return StageTime(self.amount + other.amount)


class TalentShow(FoundationTalentShow):
	"""The original show coordinator with a read-only time preview."""

	def preview_total(self, choices):
		total = StageTime(0)
		for choice in choices:
			total = total + StageTime(choice.duration())
		return total


def run_checks():
	"""Check normal, boundary, refused and non-mutating behavior."""
	first = StageTime(3000)
	same_amount = StageTime(3000)
	different_amount = StageTime(2999)

	# Equal values compare alike, while their friendly and developer displays differ.
	assert first == same_amount
	assert first != different_amount
	assert str(first) == "3,000 minutes"
	assert repr(first) == "StageTime(3000)"
	assert str(first) != repr(first)

	# Addition creates a separate value and leaves both inputs untouched.
	second = StageTime(25)
	combined = first + second
	assert combined == StageTime(3025)
	assert combined is not first and combined is not second
	assert first.amount == 3000 and second.amount == 25
	assert StageTime.__add__(first, 25) is NotImplemented
	assert StageTime.__eq__(first, 3000) is NotImplemented

	# Zero is the boundary value; the amount property cannot be assigned.
	assert StageTime(0).amount == 0
	try:
		first.amount = 2
	except AttributeError:
		pass
	else:
		raise AssertionError("amount must be read-only")

	# Negative, fractional and Boolean amounts are refused.
	for invalid_amount, error in (
		(-1, ValueError),
		(1.5, TypeError),
		(True, TypeError),
	):
		try:
			StageTime(invalid_amount)
		except error:
			pass
		else:
			raise AssertionError(f"StageTime accepted {invalid_amount!r}")

	# Preview asks different choice types for duration without booking them.
	show = TalentShow("Joel", 20)
	choices = [Dance("Mukono Movers"), Poetry("Spoken word"), AudienceWave()]
	state_before_preview = (show.clock.remaining, show.act_count)
	preview = show.preview_total(choices)
	assert preview == StageTime(11)
	assert show.preview_total([]) == StageTime(0)
	assert (show.clock.remaining, show.act_count) == state_before_preview

	print("All StageTime and preview_total checks passed.")


def main():
	"""Demonstrate the value object and its use in the talent-show story."""
	run_checks()

	three_minutes = StageTime(3)
	another_three_minutes = StageTime(3)
	four_minutes = StageTime(4)
	print("Equal values:", three_minutes == another_three_minutes)
	print("Unequal values:", three_minutes == four_minutes)
	print("Friendly value:", str(StageTime(3000)))
	print("Developer value:", repr(StageTime(3000)))
	print("Added value:", three_minutes + four_minutes)
	print("Original values remain:", three_minutes, "and", four_minutes)

	show = TalentShow("Joel", 20)
	choices = [
		Dance("Mukono Movers"),
		Poetry("Spoken word"),
		HeadlineDance("Short headline set"),
		AudienceWave(),
	]
	before_preview = (show.clock.remaining, show.act_count)
	print("Mixed-choice preview:", show.preview_total(choices))
	print("Empty preview:", show.preview_total([]))
	print("Show state unchanged:", before_preview ==
		  (show.clock.remaining, show.act_count))

	try:
		StageTime(-1)
	except ValueError as error:
		print("Invalid construction refused:", error)


if __name__ == "__main__":
	main()
