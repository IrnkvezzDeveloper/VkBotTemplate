from vk_api import VkApi
from vk_api.utils import get_random_id

#test
import keyboard
class VkHandler:
    def __init__(self, vk):
        self.vk = vk
        pass
    
    

    def SendMessage(self, userid, message, keyboard = keyboard.keyboard_null):
        self.vk.messages.send(
            user_id = userid,
            message = message,
            random_id = get_random_id(),
            keyboard = keyboard
        )

    