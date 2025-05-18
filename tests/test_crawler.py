from unittest.mock import patch
import pytest
from hn_crawler.crawler import HackerNewsCrawler

sample_html = """
<html>
  <body>
    <tr class="athing" id="1">
      <td class="title"><span class="rank">1.</span></td>
      <td class="title">
        <span class="titleline">
          <a href="https://example.com">Example Title One</a>
        </span>
      </td>
    </tr>
    <tr class="subtext" id="sub1">
      <td class="subtext">
        <span class="score">100 points</span> | 
        <a href="item?id=1">50 comments</a>
      </td>
    </tr>
    <tr class="athing" id="2">
      <td class="title"><span class="rank">2.</span></td>
      <td class="title">
        <span class="titleline">
          <a href="https://example2.com">Example Title Two</a>
        </span>
      </td>
    </tr>
    <tr class="subtext" id="sub2">
      <td class="subtext">
        <span class="score">200 points</span> | 
        <a href="item?id=2">30 comments</a>
      </td>
    </tr>
  </body>
</html>
"""



@patch("hn_crawler.crawler.requests.get")
def test_crawler_parse(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = sample_html

    crawler = HackerNewsCrawler()
    entries = crawler.parse()

    assert len(entries) == 2
    assert entries[0].title.strip() == "Example Title One"
    assert entries[1].title.strip() == "Example Title Two"
