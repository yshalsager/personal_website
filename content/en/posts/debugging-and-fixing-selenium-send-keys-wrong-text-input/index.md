+++
title = "Debugging and fixing Selenium's send_keys() wrong text input"
description = "I recently faced a weird problem while working on a freelance Selenium project in Python which is: send_keys method is sending random wrong input. Here are the details of the problem, how did I debug it and how I manged to fix after hours of investigating!"
tags = ["Python",  "Development"]
date = "2020-09-28"

+++
![main](thumbnail.png?width=800px#center)

*There are many kinds of bugs you may face while programming, but without a doubt, ghost bugs are the worse!*

I recently faced a weird problem while working on a freelance [Selenium](https://www.selenium.dev/) (A portable framework for testing web applications) project in Python which is: [send_keys](https://selenium-python.readthedocs.io/api.html?highlight=execute_script#selenium.webdriver.remote.webelement.WebElement.send_keys) method is sending random wrong input. Here are the details of the problem, how did I debug it, and how I managed to fix after hours of investigating!

I have been working on a freelance Selenium web automation and scraping project and we need to move the script to a better Linux server that runs Ubuntu 20.04. After migrating I found out that Selenium text input became so random (although it works perfectly on local PCs). For example, spaces are no longer sent, numbers are mixed, some characters are dropped, and so forth.

I started to debug with [Python](https://python.org)'s [logging](https://docs.python.org/3/library/logging.html) standard module, but the log said that the correct input was being entered, which is logical since no code changes happened. Then, I tried to see if there's something wrong with [chromedriver](https://chromedriver.chromium.org/) that being used to automate Google Chrome browser, but again, version on the old and new servers was the same. I have also tried on another (third) server that runs Ubuntu 18.04 and the same bug occurred. It's Google and [stackoverflow](https://stackoverflow.com) time! I searched our beloved websites to see if any people faced this problem besides me. I found many results from 6 years ago till 5 months ago. The most interesting one was a [chromedriver](https://chromedriver.chromium.org/)'s [bug](https://bugs.chromium.org/p/chromedriver/issues/detail?id=1771) that got closed with `WontFix` status. This bug aside, the suggested solutions were:

- Using [clear()](https://selenium-python.readthedocs.io/api.html?highlight=WebElement#selenium.webdriver.remote.webelement.WebElement.clear) method of the [WebElement](https://selenium-python.readthedocs.io/api.html?highlight=WebElement#module-selenium.webdriver.remote.webelement) before sending the text input.
- Clicking the text box before sending keys.
- Using [WebDriver](https://selenium-python.readthedocs.io/api.html?highlight=execute_script#webdriver-api)'s [execute_script()](https://selenium-python.readthedocs.io/api.html?highlight=execute_script#selenium.webdriver.remote.webdriver.WebDriver.execute_script) method to execute JavaScript code that modifies the value of the input form to the required text.
- Using [sleep](https://docs.python.org/3/library/time.html?highlight=sleep#time.sleep) from `time` standard module to wait for seconds between two `send_keys()` calls.
- Changing the server's keyboard layout to `US`.
- Using [pyperclip](https://github.com/asweigart/pyperclip/) module to paste the text into the browser directly.

But surprisingly, none of the mentioned solutions above did it, so I gave up and planned to switch to Firefox's [geckodriver](https://github.com/mozilla/geckodriver) in the next day.

After starting to add `geckodriver` support, I decided to search for a solution again since the code works **perfectly** on the PC. While reading stackoverflow's solutions my eyes caught a very interesting [answer](https://stackoverflow.com/a/23411005):

> I also experienced this problem when connecting to a VM using VNC and then running the Selenium test that way.
> The VNC was actually the one dropping characters. Once I moved to a direct connection to the VM using the VirtualBox console... it worked fine. 

This sounded very logical to me, so I quickly check what is the used [VNC](https://en.wikipedia.org/wiki/Virtual_Network_Computing) on the new server (Ubuntu 20.04) and the third server (Ubuntu 18.04). It was [TightVNC](https://www.tightvnc.com/). The old server VNC was available externally from the service provider so I couldn't check what does it use.

After more quick googling I found out that [TigerVNC](https://tigervnc.org/) should be a good alternative to the current VNC server. Using apt (a package manager for Debian, Ubuntu, and related Linux distributions), I installed `tigervnc-standalone-server tigervnc-common tigervnc-xorg-extension` packages and boom! it worked like a charm.

It was a very weird problem that occurred out of the blue and I took a very long time to figure it out and fix it. Hopes this post helps you if came here for fixing this problem!
