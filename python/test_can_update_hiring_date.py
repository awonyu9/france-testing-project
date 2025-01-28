def test_can_update_hiring_date(page):
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("Jane Doe")
    page.get_by_placeholder("Name").press("Tab")
    page.get_by_placeholder("Email").fill("janedoe@email.com")
    page.get_by_placeholder("Email").press("Tab")
    page.locator("#id_address_line1").fill("123 Nowhere St")
    page.locator("#id_address_line1").press("Tab")
    page.locator("#id_address_line2").press("Tab")
    page.get_by_placeholder("City").fill("Somewhere")
    page.get_by_placeholder("City").press("Tab")
    page.get_by_placeholder("Zip code").fill("50677")
    page.get_by_placeholder("Hiring date").fill("2025-01-28")
    page.get_by_placeholder("Job title").click()
    page.get_by_placeholder("Job title").fill("Coffee Person")
    page.get_by_role("button", name="Add").click()
    page.get_by_role("link", name="Edit").nth(0).click()
    page.get_by_role("link", name="Update contract").click()

    hiring_date_field = page.get_by_placeholder("Hiring date")
    assert hiring_date_field.is_enabled(), "Hiring date field is not enabled"
    assert hiring_date_field.is_editable(), "Hiring date field is not editable"
