from selenium import webdriver

# Alice opens a web browser
browser = webdriver.Firefox()

# and navigates to our site
browser.get("http://localhost:8000/")

# She sees 'Critaholic' in the browser title
assert "Critaholic" in browser.title

# And there's a text box waiting for her to enter a character name and initiative value

# After typing in the name and number she hits enter

# And sees that name and number in the table
