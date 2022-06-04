from tkinter.constants import YES
from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys
import urllib.request
import tkinter as tk
from tkinter import simpledialog
import requests;
import sys
import csv
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

coinmooner = 'coinmooner.com'
freshcoins = 'www.freshcoins.io'
coinsgods = 'coinsgods.com'
cointoplist = 'cointoplist.net'
coinhunt = '100xcoinhunt.com'
nextcoin = 'nextcoin.us'
coinfind = 'coinfind.cc'
tokengems = 'tokengems.net'


maxThreads = 3
checking = "#"
def task(df_proxy, df_links):

    for index, row in df_links.iterrows():
        if not checking in row['conlinks']:
            
            #1 begin https://coinmooner.com/

            if coinmooner in row['conlinks']:
                voteCount = 0
                print(row['conlinks'])
                for proxy_address in df_proxy.proxy:
                    chrome_options = webdriver.ChromeOptions()
                    prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                                                        'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                                        'notifications': 2, 'auto_select_certificate': 2,
                                                                        'fullscreen': 2,
                                                                        'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                                        'media_stream_mic': 2, 'media_stream_camera': 2,
                                                                        'protocol_handlers': 2,
                                                                        'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                                        'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                                        'metro_switch_to_desktop': 2,
                                                                        'protected_media_identifier': 2, 'app_banner': 2,
                                                                        'site_engagement': 2,
                                                                        'durable_storage': 2}} #disable images css etc
                    chrome_options.add_experimental_option("prefs", prefs)
                    chrome_options.add_argument('--headless')
                    chrome_options.add_argument('--disable-gpu')
                    chrome_options.add_argument("disable-infobars")
                    chrome_options.add_argument("--disable-extensions")
                    chrome_options.add_argument('--no-sandbox')
                    chrome_options.add_argument('--disable-application-cache')
                    chrome_options.add_argument("--disable-dev-shm-usage")

                    chrome_options.add_argument('--proxy-server=%s' % proxy_address)
                    driver = webdriver.Chrome(options=chrome_options)
                    if voteCount == row['numbers']:
                        print('break')
                        break

                    try:
                        # driver.minimize_window()
                        driver.set_page_load_timeout(60)
                        driver.get(row['conlinks'])
                        driver.find_element_by_css_selector("button.UpvoteButton_UpvoteButton__1Y25n.UpvoteButton_large__1iYUZ").click()
                        driver.quit()
                        voteCount = voteCount + 1
                    
                        print('successfully clicked')
                        print('Votes added: ' + str(voteCount))
                        f = open("success.txt", "a")
                        f.write('\n')
                        f.write(proxy_address)
                        f.close()
                        
                    except:
                        driver.quit()
                        pass
            
            # End https://coinmooner.com/

            #2 Begin https://FreshCoins.com/

            elif freshcoins in row['conlinks']:
                voteCount = 0
                print(row['conlinks'])
                for proxy_address in df_proxy.proxy:
                    chrome_options = webdriver.ChromeOptions()
                    prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                                                        'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                                        'notifications': 2, 'auto_select_certificate': 2,
                                                                        'fullscreen': 2,
                                                                        'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                                        'media_stream_mic': 2, 'media_stream_camera': 2,
                                                                        'protocol_handlers': 2,
                                                                        'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                                        'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                                        'metro_switch_to_desktop': 2,
                                                                        'protected_media_identifier': 2, 'app_banner': 2,
                                                                        'site_engagement': 2,
                                                                        'durable_storage': 2}} #disable images css etc
                    chrome_options.add_experimental_option("prefs", prefs)
                    chrome_options.add_argument('--headless')
                    chrome_options.add_argument('--disable-gpu')
                    chrome_options.add_argument("disable-infobars")
                    chrome_options.add_argument("--disable-extensions")
                    chrome_options.add_argument('--no-sandbox')
                    chrome_options.add_argument('--disable-application-cache')
                    chrome_options.add_argument("--disable-dev-shm-usage")

                    chrome_options.add_argument('--proxy-server=%s' % proxy_address)
                    driver = webdriver.Chrome(options=chrome_options)
                    if voteCount == row['numbers']:
                        print('break')
                        break

                    try:
                        # driver.minimize_window()
                        driver.set_page_load_timeout(60)
                        driver.get(row['conlinks'])
                        driver.find_element_by_css_selector("button.chakra-button.css-yqjc9g").click()
                        driver.quit()
                        voteCount = voteCount + 1
                    
                        print('successfully clicked')
                        print('Votes added: ' + str(voteCount))
                        f = open("success.txt", "a")
                        f.write('\n')
                        f.write(proxy_address)
                        f.close()
                        
                    except:
                        driver.quit()
                        pass

            # End https://FreshCoins.com/

            #3 Begin https://coinsgods.com/

            elif coinsgods in row['conlinks']:
                voteCount = 0
                print(row['conlinks'])
                for proxy_address in df_proxy.proxy:
                    chrome_options = webdriver.ChromeOptions()
                    prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                                                        'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                                        'notifications': 2, 'auto_select_certificate': 2,
                                                                        'fullscreen': 2,
                                                                        'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                                        'media_stream_mic': 2, 'media_stream_camera': 2,
                                                                        'protocol_handlers': 2,
                                                                        'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                                        'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                                        'metro_switch_to_desktop': 2,
                                                                        'protected_media_identifier': 2, 'app_banner': 2,
                                                                        'site_engagement': 2,
                                                                        'durable_storage': 2}} #disable images css etc
                    chrome_options.add_experimental_option("prefs", prefs)
                    chrome_options.add_argument('--headless')
                    chrome_options.add_argument('--disable-gpu')
                    chrome_options.add_argument("disable-infobars")
                    chrome_options.add_argument("--disable-extensions")
                    chrome_options.add_argument('--no-sandbox')
                    chrome_options.add_argument('--disable-application-cache')
                    chrome_options.add_argument("--disable-dev-shm-usage")

                    chrome_options.add_argument('--proxy-server=%s' % proxy_address)
                    driver = webdriver.Chrome(options=chrome_options)
                    if voteCount == row['numbers']:
                        print('break')
                        break

                    try:
                        # driver.minimize_window()
                        driver.set_page_load_timeout(60)
                        driver.get(row['conlinks'])
                        driver.find_element_by_id("singlevote").click()
                        driver.quit()
                        voteCount = voteCount + 1
                    
                        print('successfully clicked')
                        print('Votes added: ' + str(voteCount))
                        f = open("success.txt", "a")
                        f.write('\n')
                        f.write(proxy_address)
                        f.close()
                        
                    except:
                        driver.quit()
                        pass

            #End https://coinsgods.com/

            #4 Begin https://cointoplist.net/

            elif cointoplist in row['conlinks']:
                voteCount = 0
                print(row['conlinks'])
                for proxy_address in df_proxy.proxy:
                    chrome_options = webdriver.ChromeOptions()
                    prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                                                        'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                                        'notifications': 2, 'auto_select_certificate': 2,
                                                                        'fullscreen': 2,
                                                                        'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                                        'media_stream_mic': 2, 'media_stream_camera': 2,
                                                                        'protocol_handlers': 2,
                                                                        'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                                        'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                                        'metro_switch_to_desktop': 2,
                                                                        'protected_media_identifier': 2, 'app_banner': 2,
                                                                        'site_engagement': 2,
                                                                        'durable_storage': 2}} #disable images css etc
                    chrome_options.add_experimental_option("prefs", prefs)
                    chrome_options.add_argument('--headless')
                    chrome_options.add_argument('--disable-gpu')
                    chrome_options.add_argument("disable-infobars")
                    chrome_options.add_argument("--disable-extensions")
                    chrome_options.add_argument('--no-sandbox')
                    chrome_options.add_argument('--disable-application-cache')
                    chrome_options.add_argument("--disable-dev-shm-usage")

                    chrome_options.add_argument('--proxy-server=%s' % proxy_address)
                    driver = webdriver.Chrome(options=chrome_options)
                    if voteCount == row['numbers']:
                        print('break')
                        break

                    try:
                        # driver.minimize_window()
                        driver.set_page_load_timeout(60)
                        driver.get(row['conlinks'])
                        driver.find_element_by_css_selector("button.vote-btn").click()
                        driver.quit()
                        voteCount = voteCount + 1
                    
                        print('successfully clicked')
                        print('Votes added: ' + str(voteCount))
                        f = open("success.txt", "a")
                        f.write('\n')
                        f.write(proxy_address)
                        f.close()
                        
                    except:
                        driver.quit()
                        pass

            #End https://cointoplist.net/

            #5 Begin https://100xcoinhunt.com/

            elif coinhunt in row['conlinks']:
                voteCount = 0
                print(row['conlinks'])
                for proxy_address in df_proxy.proxy:
                    chrome_options = webdriver.ChromeOptions()
                    prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                                                        'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                                        'notifications': 2, 'auto_select_certificate': 2,
                                                                        'fullscreen': 2,
                                                                        'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                                        'media_stream_mic': 2, 'media_stream_camera': 2,
                                                                        'protocol_handlers': 2,
                                                                        'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                                        'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                                        'metro_switch_to_desktop': 2,
                                                                        'protected_media_identifier': 2, 'app_banner': 2,
                                                                        'site_engagement': 2,
                                                                        'durable_storage': 2}} #disable images css etc
                    chrome_options.add_experimental_option("prefs", prefs)
                    chrome_options.add_argument('--headless')
                    chrome_options.add_argument('--disable-gpu')
                    chrome_options.add_argument("disable-infobars")
                    chrome_options.add_argument("--disable-extensions")
                    chrome_options.add_argument('--no-sandbox')
                    chrome_options.add_argument('--disable-application-cache')
                    chrome_options.add_argument("--disable-dev-shm-usage")

                    chrome_options.add_argument('--proxy-server=%s' % proxy_address)
                    driver = webdriver.Chrome(options=chrome_options)
                    if voteCount == row['numbers']:
                        print('break')
                        break

                    try:
                        # driver.minimize_window()
                        driver.set_page_load_timeout(60)
                        driver.get(row['conlinks'])
                        driver.find_element_by_id("submitvote").click()
                        driver.quit()
                        voteCount = voteCount + 1
                    
                        print('successfully clicked')
                        print('Votes added: ' + str(voteCount))
                        f = open("success.txt", "a")
                        f.write('\n')
                        f.write(proxy_address)
                        f.close()
                        
                    except:
                        driver.quit()
                        pass

            #End https://100xcoinhunt.com/


            #6 Begin https://tokengems.net/

            elif tokengems in row['conlinks']:
                voteCount = 0
                print(row['conlinks'])
                for proxy_address in df_proxy.proxy:
                    chrome_options = webdriver.ChromeOptions()
                    prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                                                        'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                                        'notifications': 2, 'auto_select_certificate': 2,
                                                                        'fullscreen': 2,
                                                                        'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                                        'media_stream_mic': 2, 'media_stream_camera': 2,
                                                                        'protocol_handlers': 2,
                                                                        'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                                        'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                                        'metro_switch_to_desktop': 2,
                                                                        'protected_media_identifier': 2, 'app_banner': 2,
                                                                        'site_engagement': 2,
                                                                        'durable_storage': 2}} #disable images css etc
                    chrome_options.add_experimental_option("prefs", prefs)
                    chrome_options.add_argument('--headless')
                    chrome_options.add_argument('--disable-gpu')
                    chrome_options.add_argument("disable-infobars")
                    chrome_options.add_argument("--disable-extensions")
                    chrome_options.add_argument('--no-sandbox')
                    chrome_options.add_argument('--disable-application-cache')
                    chrome_options.add_argument("--disable-dev-shm-usage")

                    chrome_options.add_argument('--proxy-server=%s' % proxy_address)
                    driver = webdriver.Chrome(options=chrome_options)
                    if voteCount == row['numbers']:
                        print('break')
                        break

                    try:
                        # driver.minimize_window()
                        driver.set_page_load_timeout(60)
                        driver.get(row['conlinks'])
                        time.sleep(1)
                        driver.find_element_by_css_selector("button.g-recaptcha").click()
                        driver.quit()
                        voteCount = voteCount + 1
                    
                        print('successfully clicked')
                        print('Votes added: ' + str(voteCount))
                        f = open("success.txt", "a")
                        f.write('\n')
                        f.write(proxy_address)
                        f.close()
                        
                    except:
                        driver.quit()
                        pass


            #End https://tokengems.net/

    


def main():
    executor = ThreadPoolExecutor(maxThreads)
    df_proxy= pd.read_csv("proxy.csv")
    df_link = pd.read_csv("links.csv")
    futures = []
    i = 0
    coin_link_num = int(len(df_link)/maxThreads) + 1

    for i in range(maxThreads):
        futures.append(executor.submit(task, df_proxy, df_link[i* coin_link_num: (i+1)*coin_link_num]))
    

if __name__ == "__main__":
    main()

