'''
:url (TikTok Url)
:apiKey (YourApiKey)
'''
from requests import get
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
    params = {'url': f'{input_str}', 'apiKey': 'Akbarneh'}
    res = get('https://mhankbarbar.moe/api/tiktok', params=params).json()
    print(res)
