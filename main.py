#vk
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import vk_api

#project files
import utils
from vkhandler import VkHandler
import keyboard
import config
#other
from datetime import datetime


vk = vk_api.VkApi(config.token)
longpool = VkBotLongPoll(vk=vk, group_id=config.group_id)
vk_handler = VkHandler(vk.get_api())

print(f"Bot started at {datetime.now()}")
for event in longpool.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and utils.GetMessage(event):
        #тут прописывать логику
       pass