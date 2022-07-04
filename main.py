#vk

try:
    import vk_api
except ModuleNotFoundError:
    import os
    print("Installing extensions for project")
    os.system("pip install -r requirements.txt")

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll


#project files
import utils
from vkhandler import VkHandler
import keyboard
import config
#other
from datetime import datetime


vk = VkApi(config.token)
longpool = VkBotLongPoll(vk=vk, group_id=config.group_id)
vk_handler = VkHandler(vk.get_api())

print(f"Bot started at {datetime.now()}")
for event in longpool.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and utils.GetMessage(event):
        #тут прописывать логику
       pass