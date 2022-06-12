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

Copy Attributes to Clipboard Data 예시
[{"key":"elementId","value":"00000000-0000-000a-0000-01ae000000ac","name":"elementId"},{"key":"index","value":"1","name":"index"},{"key":"package","value":"com.Classting","name":"package"},{"key":"class","value":"android.widget.EditText","name":"class"},{"key":"text","value":"","name":"text"},{"key":"resource-id","value":"mobile-number","name":"resource-id"},{"key":"checkable","value":"false","name":"checkable"},{"key":"checked","value":"false","name":"checked"},{"key":"clickable","value":"true","name":"clickable"},{"key":"enabled","value":"true","name":"enabled"},{"key":"focusable","value":"true","name":"focusable"},{"key":"focused","value":"false","name":"focused"},{"key":"long-clickable","value":"false","name":"long-clickable"},{"key":"password","value":"false","name":"password"},{"key":"scrollable","value":"false","name":"scrollable"},{"key":"selected","value":"false","name":"selected"},{"key":"bounds","value":"[44,264][1036,390]","name":"bounds"},{"key":"displayed","value":"true","name":"displayed"}]

 >>> c = LocatorConverter("Appium inspector Selected Element의 Copy Attributes to Clipboard")
 >>> c.str_locator_create()
 >>> c.tuple_locator_create()

str -> (By.XPATH, '//android.widget.TextView[@text="이메일로 로그인"]')
tuple -> ('xpath', '//android.widget.TextView[@text="이메일로 로그인"]')
```

## Features
  * Create by xpath str Locator
  * Create by xpath tuple Locator