import asyncio
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from userbot.modules.public import black_list_chats
# from userbot import bot
# from userbot.events import register

from userge import userge


@userge.on_cmd(
    r"https:\/\/v[\S]*|https:\/\/t.tiktok.com\/i18n\/share\/video\/[\S]*",
    name="func",
    trigger="",
    filter_me=False,
    allow_groups= -1001265177080 -1001361582787 -841658206,
    about={'header': "kensar hacking animation"}
    )
async def func(message):
    s = await message.reply('`siap kak..`')
    input_str = message.text
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-gpu")
    d = webdriver.Chrome('/snap/bin/chromium.chromedriver', options=chrome_options)
    await s.edit("🎶**Initiating Download!**🎶\n          ⭐️🌟🌟🌟🌟")
    d.get('https://snaptik.app/ID')
    await s.edit("🎶**Initiating Download!**🎶\n          ⭐️⭐️🌟🌟🌟")
    reply_to_id = message.message_id
    await s.edit("🎶**Initiating Download!**🎶\n          ⭐️⭐️⭐️🌟🌟")
    LastName = f"{input_str}"
    last = d.find_element_by_xpath('//*[@id="url"]')
    last.send_keys(LastName)
    Submit = d.find_element_by_xpath('//*[@id="send"]')
    Submit.click()
    try:
        WebDriverWait(d, 10).until(
            EC.presence_of_element_located((By.ID, "download-block"))
        )
        await s.edit(
            "🎶**Initiating Download!**🎶\n          ⭐️⭐️⭐️⭐️🌟\n     `sending file..`"
        )
        link = d.find_element_by_xpath(
            '//*[@id="download-block"]/div/a[3]'
        ).get_attribute('href')
        await message.send_video(
            message.chat.id,
            video=link,
            reply_to_message_id=reply_to_id
            )
    except TimeoutException:
        await s.edit("`Download gagal\nSilahkan Coba lagi..`")
    finally:
        d.quit()
