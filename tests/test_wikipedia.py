from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be



def test_getting_started():
    continue_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button'))
    title_text = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))

    with step('First wellcome screen'):
        title_text.should(have.text('The Free Encyclopedia'))

        continue_button.click()

    with step('Second wellcome screen'):
        title_text.should(have.text('New ways to explore'))

        continue_button.click()

    with step('Third wellcome screen'):
        title_text.should(have.text('Reading lists with sync'))

        continue_button.click()

    with step('Last wellcome screen'):
        title_text.should(have.text('Send anonymous data'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')).click()

def test_search():
    with step('Skip wellcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_open_article():
    with step('Skip wellcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))

    with step('Open first article'):
        results.first.click()

    with ((step('Verify page opened'))):
        article_header = browser.element(
            (AppiumBy.CLASS_NAME, "android.widget.TextView")
        )
        article_header.should(have.text('Appium'))
        # browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_wiki_error_text')).should(
        #     have.text('An error occurred'))
