from vk_api.keyboard import VkKeyboard, VkKeyboardButton, VkKeyboardColor

settings = dict(one_time=False, inline=True)

keyboard_null = VkKeyboard(**settings).get_empty_keyboard()

def GenerateTestKeyboard():
    keyboard = VkKeyboard(**settings)
    keyboard.add_callback_button("Тестовая кнопка")
    keyboard.add_callback_button("Тестовая кнопка 2")
    keyboard.add_line()
    keyboard.add_callback_button("Кнопка одна на линии")
    keyboard.add_line()
    keyboard.add_openlink_button("Открыть волшебника", "https://rt.pornhub.com")
    return keyboard.get_keyboard()