import re


class EntryFilterHandler:
    @staticmethod
    def count_words(title: str) -> int:
        #   Regex - remove all char that are NOT word characters or whitespaces
        cleaned = re.sub(r"[^\w\s]", "", title)
        return len(cleaned.strip().split())

    def filter_more_than_five_words(self, entries):
        return sorted(
            [e for e in entries if self.count_words(e.title) > 5],
            key=lambda x: x.comments, reverse=True
        )

    def filter_five_or_fewer_words(self, entries):
        return sorted(
            [e for e in entries if self.count_words(e.title) <= 5],
            key=lambda x: x.points, reverse=True
        )
