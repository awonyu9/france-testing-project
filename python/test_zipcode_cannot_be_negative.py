def test_zipcode_cannot_be_negative(page):
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("Test User")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("testuser@gmail.com")
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("123 Main Street")
    page.get_by_role("textbox", name="City").click()
    page.get_by_role("textbox", name="City").fill("Test City")
    page.get_by_role("spinbutton", name="Zip code").click()
    page.get_by_role("spinbutton", name="Zip code").fill("-12345")
    
    page.get_by_role("button", name="Add").click()
    
    error_message = page.locator("span.error:has-text('Invalid ZIP code')")  
    assert error_message.is_visible(), "Error message for invalid ZIP code was not displayed."
    assert page.url.endswith("/add_employee"), "Form was submitted with an invalid ZIP code."