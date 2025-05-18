import sys
from hn_crawler.crawler import HackerNewsCrawler
from hn_crawler.filterer import EntryFilterHandler
from hn_crawler.logger import UsageLogHandler

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ["filter1", "filter2"]:
        print("Usage: python -m hn_crawler.main [filter1|filter2]")
        sys.exit(1)

    crawler = HackerNewsCrawler()
    filterer = EntryFilterHandler()

    request_url = "https://news.ycombinator.com/"
    response_status_code = 200
    error_message = None
    entries = []
    filtered_result = []

    try:
        entries = crawler.parse()
        if sys.argv[1] == "filter1":
            filtered_result = filterer.filter_more_than_five_words(entries)
            filter_type = "more_than_five_words"
        else:
            filtered_result = filterer.filter_five_or_fewer_words(entries)
            filter_type = "five_or_fewer_words"
    except Exception as e:
        error_message = str(e)
        response_status_code = 500

    # Log usage data
    UsageLogHandler.log(
        filter_type=filter_type if not error_message else "error",
        request_url=request_url,
        response_status_code=response_status_code,
        entries_scraped=len(entries),
        error_message=error_message,
        filter_result_count=len(filtered_result),
        results=[entry._asdict() if hasattr(entry, "_asdict") else entry.__dict__ for entry in filtered_result] if not error_message else [],
    )

    # Print results only if no error
    last_log = UsageLogHandler.fetch_last_log()
    if not error_message:
        for i, entry in enumerate(filtered_result, 1):
            logger.info(f"{i}. {entry}")

    else:
        if last_log and last_log["error_message"]:
            logger.error(f"Last recorded error: {last_log['error_message']}")
        else:
            logger.error(f"Error occurred: {error_message}")


if __name__ == '__main__':
    main()
