from playwright.sync_api import Page
import pytest


def test_title(page: Page):
    page.goto("http://saucedemo.com")
    assert page.title() == "Swag Labs"
