from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_current_url(driver):
  # Gets the current URl we're using
  return driver.current_url

def get_source_code(driver):
  # Gets the HTML source code of the current webpage.
  # In this exercise it is "www.google.com" since it's the starting page of Chromedriver
  return driver.page_source


def navigation():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.google.com/")
    page_title = driver.title
    print("Google title is: ", page_title)
    current_url = get_current_url(driver)
    print(f"Current URL: {current_url}")
    window_handle = driver.current_window_handle
    print(f"Window Handle 1: {window_handle}")
    driver.get("https://www.udemy.com")
    print(f"Current URL: {current_url}")
    page_title2 = driver.title
    print("Udemy title is: ", page_title2)
    window_handle2 = driver.current_window_handle
    print(f"Window Handle 2: {window_handle2}")
    time.sleep(5)

#Main function / Menu
def main():
  running = True;
  while running:
    print("\nMenu:")
    print("1. Get Current URL")
    print("2. Get Source Code")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
      navigation()
    elif choice == '2':
      # Call a new function to get the source code (optional)
      # Or directly use get_source_code(driver) here if the driver already exists

      # Example using a new function (assuming a driver is created beforehand)
      def get_source_and_quit(driver):
        source_code = get_source_code(driver)   # It opens google.
        print(source_code)  # Or process the source code here
        time.sleep(5)
        driver.quit()

      driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
      driver.maximize_window()
      driver.get("https://www.google.com/")  # You can choose any URL here
      get_source_and_quit(driver)
    elif choice == '3':
      print("Exiting...")
      running = False
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()