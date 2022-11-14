import re
from typing import Generator

import pytest
from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://localhost:8000"
    )
    yield request_context
    request_context.dispose()


def test_main(page: Page):
    page.goto("http://localhost:8000/")
    expect(page.locator("body")).to_have_text(re.compile("World"))
