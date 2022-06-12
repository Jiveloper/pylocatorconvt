# pylocatorconvt

## Installation

Download using pip via pypi.

```bash
$ pip install 'package' --upgrade
  or
$ pip install git+'repository'
```
(Mac/homebrew users may need to use ``pip3``)


## Quick start
```python
 >>> from pylocatorconvt.locatorconvt import LocatorConverter
 >>> c = LocatorConverter("Appium inspector Selected Element의 Copy Attributes to Clipboard")
 >>> c.str_locator_create()
 >>> c.tuple_locator_create()
```

## Features
  * Create str Locator
  * Create tuple Locator