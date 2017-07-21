## Appium android test framework based on python, pytest, appium, PO pattern


### Install

Install python

    sudo add-apt-repository ppa:jonathonf/python-3.6
    sudo apt-get update
    sudo apt-get install python3.6
    sudo apt-get install python3.6-dev

Load external dependencies

    virtualenv --python=`which python3.6` appium_tests
    pip install -r .meta/packages

Install appium

    $ npm install -g appium

### Run
    Place .apk file to app folder: f.e: ./app/Carousell-test-engineering-app.apk
    $ py.test -s -v


### Run code-style checks

    $ flake8

### Helpers

    Assuming that you've installed everything correctly, I mean you have $ANDROID_HOME leading to your android sdk
    there is a utils/bootstrap.sh script that downloads sdk and creates a virtual device to run tests.
    Because I've faced an issue while doing test task on AVD based on android 7.x:
    https://github.com/appium/appium/issues/7588
    I've decided to switch to android 6.x and create this sh script to configure environment.
    Usage example ./bootstrap.sh to download and create avd or ./bootstrap.sh -run to + run emulator

### Demo

    The demonstration of tests execution you can find in videos folder