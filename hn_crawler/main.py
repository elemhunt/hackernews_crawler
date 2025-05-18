import sys
from hn_crawler.crawler import HackerNewsCrawler
from hn_crawler.filterer import EntryFilterHandler
from hn_crawler.logger import UsageLogHandler


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ["filter1", "filter2"]:
        print("Usage: python -m hn_crawler.main [filter1|filter2]")
        sys.exit(1)

    crawler = HackerNewsCrawler()
    filterer = EntryFilterHandler()
    logger = UsageLogHandler()

    entries = crawler.parse()

    if sys.argv[1] == "filter1":
        result = filterer.filter_more_than_five_words(entries)
        logger.log("more_than_five_words")
    else:
        result = filterer.filter_five_or_fewer_words(entries)
        logger.log("five_or_fewer_words")

    for entry in result:
        print(entry)


if __name__ == '__main__':
    main()
