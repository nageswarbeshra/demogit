# if browser_head == "headless" and browser_name == "chrome":
    #     service_obj = Service("C:/Users/nages/PycharmProjects/pythonSelenium/Resources/chromedriver-win64/chromedriver.exe")
    #     driver = webdriver.Chrome(service=service_obj,options=Chrome_option)
    #     Chrome_option.add_argument("headless")
    #     print(":", current_time, ": Test Started in Chrome Browser.....")
    #
    # elif browser_head == "withHead" and browser_name == "chrome":
    #     service_obj = Service("C:/Users/nages/PycharmProjects/pythonSelenium/Resources/chromedriver-win64/chromedriver.exe")
    #     driver = webdriver.Chrome(service=service_obj,options=Chrome_option)
    #     print(":", current_time, ": Test Started in Chrome Browser.....")
    #
    #
    # elif browser_head == "headless" and browser_name == "firefox":
    #     # Firefox_option = webdriver.FirefoxOptions()
    #     # Firefox_option.add_argument("headless")
    #     # Firefox_option.add_argument("--ignore-certificate-errors")
    #     service_obj = FirefoxService("C:/Users/nages/PycharmProjects/pythonSelenium/Resources/chromedriver-win64/geckodriver.exe")
    #     driver = webdriver.Firefox(service=service_obj,options=Firefox_option )
    #
    # elif browser_head == "withHead" and browser_name == "firefox":
    #     # Firefox_option = webdriver.FirefoxOptions()
    #     # Firefox_option.add_argument("headless")
    #     # Firefox_option.add_argument("--ignore-certificate-errors")
    #     service_obj = FirefoxService("C:/Users/nages/PycharmProjects/pythonSelenium/Resources/chromedriver-win64/geckodriver.exe")
    #     driver = webdriver.Firefox(service=service_obj,options=Firefox_option )
    #     print(":", current_time, ": Test Started in  Firefox Browser.....")
    #
    # elif browser_head == "headless" and browser_name == "IE":
    #     # service_obj = Service("C:/Users/nages/PycharmProjects/pythonSelenium/Resources/chromedriver-win64/IEDriverServer.exe")
    #     driver = webdriver.Edge()
    #     Edge_option = webdriver.EdgeOptions()
    #     Edge_option.add_argument("headless")
    #     Edge_option.add_argument("--ignore-certificate-errors")
    #     print(":", current_time, ": Test Started in  Edge Browser.....")
    #
    # elif browser_head == "withHead" and browser_name == "IE":
    #
    #     # service_obj = Service("C:/Users/nages/PycharmProjects/pythonSelenium/Resources/chromedriver-win64/IEDriverServer.exe")
    #     driver = webdriver.Edge()
    #     Edge_option = webdriver.EdgeOptions()
    #     Edge_option.add_argument("headless")
    #     Edge_option.add_argument("--ignore-certificate-errors")
    #     print(":", current_time, ": Test Started in  Edge Browser.....")
    # # chrome_options1 = webdriver.ChromeOptions()
    # # chrome_options1.add_argument("--start-maximized")
    # # chrome_options.add_argument("headless")
    #
    # driver.implicitly_wait(10)
    # driver.maximize_window()
    # request.cls.driver = driver
    # yield
    # print("\n",current_time, ": Test Completed successfully!")
    # driver.close()




    #
    # Chrom_option = webdriver.ChromeOptions()
    # Chrom_option.add_argument("headless")
    # Chrom_option.add_argument("--ignore-certificate-errors")
    #
    #
    # Firefox_option.add_argument("-headless")
    # Firefox_option.add_argument("--ignore-certificate-errors")
    #
    #
    # Edge_option.add_argument("-headless")
    # Edge_option.add_argument("--ignore-certificate-errors")
