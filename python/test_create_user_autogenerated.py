import pytest
from playwright.sync_api import Playwright, sync_playwright, expect, Page


def test_add_employee(page: Page) -> None:
    page.goto("https://f.se1.hr.dmerej.info/")
    page.get_by_role("link", name="Reset database").click()
    page.get_by_role("button", name="Proceed").click()
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("Name")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("email@gmail.com")
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("Test address 1")
    page.locator("#id_address_line2").click()
    page.locator("#id_address_line2").fill("Test address 2")
    page.get_by_placeholder("City").click()
    page.get_by_placeholder("City").fill("City test")
    page.get_by_placeholder("Zip code").click()
    page.get_by_placeholder("Zip code").fill("75000")
    page.get_by_placeholder("Hiring date").fill("2025-01-17")
    page.get_by_placeholder("Job title").click()
    page.get_by_placeholder("Job title").fill("Test")
    page.get_by_role("button", name="Add").click()
    expect(page.get_by_role("cell", name="Name", exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name="email@gmail.com")).to_be_visible()