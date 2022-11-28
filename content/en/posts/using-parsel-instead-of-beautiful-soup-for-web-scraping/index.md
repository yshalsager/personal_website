+++
title = "Using Parsel instead of Beautiful Soup for Web Scraping"
description = "For a long time, I have been using Beautiful Soup 4 to extract data from web pages' HTML markup, it's popular, easy, robust, and battle-tested library for navigating, searching, and modifying the DOM tree. But, recently I came across Parsel, another HTML parsing library which supports XPath selectors, which is missing in Beautiful Soup, and I was in need of using something that can extract data from HTML using XPath so I decided to get it a try. Here's my thought after using it!"
tags = ["Python",  "Development"]
date = "2022-11-28"

+++

[Web scraping](https://en.wikipedia.org/wiki/Web_scraping) is an automated process to extract data from web page, and since [Python](https://www.python.org/) is one the most popular programming languages it's common to see people use it for doing web scraping tasks like me :)

For a long time, I have been using [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/) to extract data from web pages' HTML markup, it's popular, easy, robust, and battle-tested library for navigating, searching, and modifying the [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) tree. But, recently I came across [Parsel](https://github.com/scrapy/parsel), another HTML parsing library which supports [XPath](https://developer.mozilla.org/en-US/docs/Web/XPath) selectors, which is missing in Beautiful Soup, and I was in need of using something that can extract data from HTML using XPath (rather than [Scrapy](https://scrapy.org/), funny enough, later I knew that Scrapy uses Parsel under the hood :D), so I decided to get it a try.

## Thoughts and Tricks After Usage

- Parsel is so powerful! it saved me much time than bs4 usually did, this is mainly because of the easy way it provides to access [DOM Node](https://developer.mozilla.org/en-US/docs/Web/API/Node) HTML, text, attributes and other values easily with a handy way to get a default value if the required data didn't exist.

- Parsel uses [lxml](https://lxml.de/) for parsing the web page, this can result in a huge performance improvement according to [selectolax's benchmark](https://github.com/rushter/selectolax#simple-benchmark) (which is an interesting library to try as well).

- Parsel is easy to use, all you need to do is to import `Selector` from `parsel` package then use `Selector(text=response.text)` to load HTML string into a selector object.

```python
# code snippet from https://parsel.readthedocs.io/en/latest/usage.html  
from parsel import Selector  
text = "<html><body><h1>Hello, Parsel!</h1></body></html>"  
selector = Selector(text=text)
```

- `.getall()` and `.get()` are equivalent for `.select()`and `.select_one()` in bs4.

- `.xpath()` and `.css()` methods can be chained! `selector.css('img').xpath('@src').getall()`

- `Selector`'s non-standard `::text` pseudo-element can be better than Beautiful Soup's `.text` because it won't be `None` even with empty text. Same goes for `::attr` vs `.get()` (without default value).

- Use `*::text` to selects all descendant text nodes of the current selector.

- If you want to use [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) (regex) to get data from a string of a selector, all you need to do is to use `.re()` and `.re_first()` methods. However, unlike using `.xpath()` or `.css()` methods, regex methods returns a list of strings so they can't be chained.

- The proper way to work with relative XPaths is to prefix the path with dot `divs.xpath('.//p')`.

- `drop()` can be used to remove elements based on a Selector, this is similar to `Tag.decompose()` in bs4, and can't be undone.

- When querying by class, consider using CSS instead of XPath.

- You can convert CSS to XPath using Parsel's `css2xpath` function.

- Because of lxml, sometimes you may get something rather that what browser show while parsing the HTML using Parsel, here is [more details](https://github.com/scrapy/parsel/issues/83) about this issue.

## Extra Resources

- [CSS cheatsheet](https://devhints.io/css) that has good summary of CSS selectors.

- [Xpath cheatsheet](https://devhints.io/xpath).

- [XPath Playground](https://scrapinghub.github.io/xpath-playground/) to try out your XPath queries.

- [XPath/CSS Equivalents](XPath/CSS%20Equivalents).
