# icsd-queryer
A python module to query data from the ICSD using a [Selenium WebDriver](http://selenium-python.readthedocs.io/).

Requires ChromeDriver for Selenium. On a Mac,

```
brew tap homebrew/cask
brew cask install chromedriver
```
Tested on ChromeDriver 2.29.
Compatible with ICSD Version 4.2.0 (build 20190513-1424) - Data Release 2019.1

## Testing

Store previously crawled files in `icsd-queryer/expected`.
Then run,

```
nosetests tests/*  --with-coverage    --cover-package .  --nocapture
```

Some of the tests randomly pick up expected files and compared them with newly obtained data.
