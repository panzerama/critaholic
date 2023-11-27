from selenium import webdriver

# Alice opens a web browser
browser = webdriver.Firefox()

# and navigates to our site
browser.get("http://localhost:8000/")

# She sees 'Critaholic' in the browser title
assert "Critaholic" in browser.title

#

assert "Congratulations!" in browser.title
print("OK")