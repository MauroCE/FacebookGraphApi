# External Modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# Internal Modules
from connect import get_graph
from config import FACEBOOK_GROUP_ID
from group import get_group_post_attachments


def send_whatsapp_msg(target, msg):
    """
    This function sends a WhatsApp message to a contact. The first time that
    you use this you will need to scan the QR code. After that, it will be
    cached.

    To see how this is done, look here:
    https://stackoverflow.com/questions/45651879/using-selenium-how-to-keep-logged-in-after-closing-driver-in-python
    Look also here:
    http://techniknow.com/whatsapp-using-python/
    :return:
    """
    # Keep logged in so we do not have to scan QR code every time
    options = Options()
    options.add_argument("user-data-dir=/tmp/tarun")
    # Connect driver to WhatsApp Web
    driver = webdriver.Chrome('./chromedriver', chrome_options=options)
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 600)
    # No idea tbh
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()
    inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    input_box = wait.until(
        ec.presence_of_element_located((By.XPATH, inp_xpath))
    )
    input_box.send_keys(msg + Keys.ENTER)
    driver.close()


if __name__ == "__main__":
    # Get the graph
    g, _ = get_graph()
    # Define some variables:
    since = '01-01-2018'
    until = '28-07-2018'
    contact = "'Mamma'"
    # Get videos from since to until
    videos = get_group_post_attachments(g, since=since, until=until)
    # If there are indeed videos, send message
    if len(videos) > 0:
        # Get name of the group
        group = g.get_object(FACEBOOK_GROUP_ID)['name']
        # Create a message. Notice that if you add \n in between, it will send
        # several messages
        string = "{} videos found in group {}.".format(len(videos), group)
        for index, video in enumerate(videos):
            string += " Link to video {}: ".format(index + 1) + video[1]
        # Send message
        send_whatsapp_msg(contact, string)
