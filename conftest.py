import pytest
import os

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)

        if page:
            # folder create if not exists
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            # take screenshot
            file_name = f"screenshots/{item.name}.png"
            page.screenshot(path=file_name)