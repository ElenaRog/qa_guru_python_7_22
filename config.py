import os
from typing import Literal


from utils import file
from dotenv import load_dotenv


context = os.getenv('context', 'local_real')

if context == 'bstack':
    load_dotenv(file.abs_path_from_project('.env'))
    load_dotenv(file.abs_path_from_project('.env.bstack'))
if context == 'local_emulator':
    load_dotenv(file.abs_path_from_project('.env.local_emulator'))
if context == 'local_real':
    load_dotenv(file.abs_path_from_project('.env.local_real'))

remote_url = os.getenv('REMOTE_URL', 'http://127.0.0.1:4723/wd/hub')
deviceName = os.getenv('DEVICE_NAME')
udid = os.getenv('UDID', 'emulator-5554')
appWaitActivity = os.getenv('APP_WAIT_ACTIVITY', 'org.wikipedia.*')
app = os.getenv('APP_PATH', './app-alpha-universal-release.apk')

bstack_userName = os.getenv('BSTACK_USERNAME')
bstack_accessKey = os.getenv('BSTACK_ACCESSKEY')


def to_driver_options():
    from appium.options.android import UiAutomator2Options
    options = UiAutomator2Options()

    if deviceName:
        options.set_capability('deviceName', deviceName)

    if udid:
        options.set_capability('udid', udid)

    if appWaitActivity:
        options.set_capability('appWaitActivity', appWaitActivity)

    options.set_capability('app', (
        app if (app.startswith('/') or (context == 'bstack'))
        else file.abs_path_from_project('AndroidApp', app)
    ))

    if context == 'bstack':
        options.set_capability('platformVersion', '9.0')
        options.set_capability(
            'bstack:options', {
                'projectName': 'First Python project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack first_test',

                'userName': bstack_userName,
                'accessKey': bstack_accessKey,
            },
        )

    return options
