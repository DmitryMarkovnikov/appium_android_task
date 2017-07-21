import os
import subprocess

import datetime
import pytest
import time
from appium import webdriver

from util import load_yaml

pytest_plugins = ['tests.logger_plugin']


@pytest.fixture(autouse=True, scope="session")  # comment and run standalone server for local development
def run_appium():
    """Fixture to run on CI to run before the session appium server and terminate it after tests session is closed"""
    appium = subprocess.Popen('appium')
    assert appium.poll() is None
    time.sleep(5)  # TODO: log appium to file, remove this sleep
    yield
    appium.terminate()


@pytest.fixture(autouse=True, scope="session")
def record_video():
    """
    Fixture that starts and stops recording
    for now the scope is session, because only one test, it can be change for function and save every executed test
    """
    timestamp = datetime.datetime.now().isoformat()
    recording = subprocess.Popen(['adb', 'shell', 'screenrecord', '/sdcard/{}.mp4'.format(timestamp)])
    assert recording.poll() is None
    yield
    time.sleep(7)  # TODO: investigate how to remove sleep, without it video is 00:00 duration
    recording.terminate()
    subprocess.Popen(['adb', 'pull', '/sdcard/{}.mp4'.format(timestamp), 'videos/'])


@pytest.fixture(autouse=True, scope="function")
def driver_setup(request):
    """
    Fixture prepares webdriver with desired capabilities
    """
    run_appium()
    capabilities = {
        'platformName': 'Android',
        'deviceName': 'Android Simulator',
        'app': os.path.abspath(os.path.join(os.path.dirname(__file__), '../app/Carousell-test-engineering-app.apk')),
        'appWaitActivity': '.activities.WelcomeActivity',
    }
    url = 'http://localhost:4723/wd/hub'
    request.instance.driver = webdriver.Remote(url, capabilities)

    yield
    request.instance.driver.quit()


@pytest.fixture()
def get_registered_accounts_from_yml():
    """
    Parses yaml data and returns dictionary with registered users
    :return: dictionary with registered users
    """
    data = load_yaml('registered_users.yaml')
    return data
