#vk
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import vk_api

#project files
import utils
from vkhandler import VkHandler
import keyboard

#other
from datetime import datetime

token = '63f2c1c371af7de4014655ee11f3d1f51718f4f707e17f7eebedfad96a6b4e7857dba4427d608abff5df7'

vk = vk_api.VkApi(token=token)
longpool = VkBotLongPoll(vk=vk, group_id="213782343")
vk_handler = VkHandler(vk.get_api())

print(f"Bot started at {datetime.now()}")
for event in longpool.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and utils.GetMessage(event):
        #тут прописывать логику
       pass