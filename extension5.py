"""Demonstrate a running order for the campus talent show."""
from pathlib import Path
import sys


STORY_DIRECTORY = Path(__file__).parent / "stories" / "05_campus_talent_show"
sys.path.insert(0, str(STORY_DIRECTORY))

from story import Poetry, ShortDance, TalentShow as BaseTalentShow


class TalentShow(BaseTalentShow):
	def running_order(self):
		"""Return booked act names, count, remaining time, and an empty message."""
		names = [performance.name for performance in self._lineup]
		return {
			"acts": names,
			"count": self.act_count,
			"minutes_left": self.clock.remaining,
			"message": "No acts have been booked yet." if not names else None,
		}


def main():
	show = TalentShow("Joel", 8)
	print(show.running_order())

	print(show.book(ShortDance("Mukono Movers")))
	print(show.book(Poetry("Achen's spoken word")))
	print(show.running_order())


if __name__ == "__main__":
	main()
