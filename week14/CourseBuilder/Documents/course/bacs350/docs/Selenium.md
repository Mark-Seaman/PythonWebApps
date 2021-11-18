# Selenium

Selenium is a tool that uses a browser to fetch web pages and then a
code library that extract content from the pages.


## Setup

Install the selenium package in Python

    pip install selenium

Install the webdriver (Mac)

    # Attempted commands
    brew install chromedriver
    brew cask install chromedriver
    brew cask reinstall chromedriver

    ==> Downloading https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_mac64.zip
    Already downloaded: /Users/seaman/Library/Caches/Homebrew/downloads/798661a7f1489c5d4cd35edaac0a06a20f62196e7cef7832b841378d476f6386--chromedriver_mac64.zip
    ==> Verifying SHA-256 checksum for Cask 'chromedriver'.
    ==> Uninstalling Cask chromedriver
    ==> Unlinking Binary '/usr/local/bin/chromedriver'.
    ==> Purging files for version 84.0.4147.30 of Cask chromedriver
    ==> Installing Cask chromedriver
    ==> Linking Binary 'chromedriver' to '/usr/local/bin/chromedriver'.
    🍺  chromedriver was successfully installed!

    Quick Test Fails
        Traceback (most recent call last):
          File "/Users/seaman/Sensei-2020/tool/management/commands/tst.py", line 22, in handle
            tst_command(self, options['command'])
          File "/Users/seaman/Sensei-2020/tool/management/commands/tst.py", line 48, in tst_command
            quick_test()
          File "/Users/seaman/Sensei-2020/tool/quick_test.py", line 18, in quick_test
            test_selenium_setup()
          File "/Users/seaman/Sensei-2020/tool/page.py", line 178, in test_selenium_setup
            driver = open_browser_dom()
          File "/Users/seaman/Sensei-2020/tool/page.py", line 108, in open_browser_dom
            return webdriver.Chrome(options=options)
          File "/Users/seaman/Sensei-2020/.venv/lib/python3.7/site-packages/selenium/webdriver/chrome/webdriver.py", line 73, in __init__
            self.service.start()
          File "/Users/seaman/Sensei-2020/.venv/lib/python3.7/site-packages/selenium/webdriver/common/service.py", line 98, in start
            self.assert_process_still_running()
          File "/Users/seaman/Sensei-2020/.venv/lib/python3.7/site-packages/selenium/webdriver/common/service.py", line 111, in assert_process_still_running
            % (self.path, return_code)
        selenium.common.exceptions.WebDriverException: Message: Service chromedriver unexpectedly exited. Status code was: -9


    cd /usr/local/bin
    cd /usr/local/Caskroom/chromedriver/84.0.4147.30/

    spctl --add --label 'Approved' chromedriver

    chromedriver --version
    
        ChromeDriver 84.0.4147.30 (48b3e868b4cc0aa7e8149519690b6f6949e110a8-refs/branch-heads/4147@{#310})

Implement a quick test in Python

    from selenium import webdriver

    # Open the webdriver
    driver = webdriver.Chrome()

    # Get a page
    driver.get('http://shrinking-world.com')
    print(driver.page_source)

    # Close the webdriver
    driver.quit()


Running headless on Mac

    from selenium import webdriver

    # Open the webdriver in headless mode
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('window-size=800x600')
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    # Get a page
    driver.get('http://shrinking-world.com')

    # Extract the text from the page
    print(driver.find_element_by_tag_name('body').text)

    # Close the webdriver
    driver.quit()


