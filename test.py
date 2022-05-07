from ChromeDriver import ChromeDriver


driver = ChromeDriver()
driver.test()
driver.client.close()
driver.client.quit()
