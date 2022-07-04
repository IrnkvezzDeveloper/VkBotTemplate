import json

#возвращает айди пользователя отправившего сообщение
#data - event возвращаемый с longpool.listen()
#return userid
def GetUserId(data):
    return data.object.message['from_id']
#возвращает сообщение отправленое пользователем
#data - event возвращаемый longpool.listen()
#return str
def GetMessage(data):
    return data.object.message['text']

#Сравниваение сообщений 
#message - str 
#text = str
#return true or false
def IsMessageEquals(message, text):
    return message == text

#Сравнение сообщений
#data - longpool.listen() event
#text - str
#return true or false
def IsGetMessageEquals(data, text):
    return IsMessageEquals(GetMessage(data), text)

#Сравнение айди пользователя
#user - user id
#target - target user id
#return true or false
def IsUserEquals(user, target):
    return user == target

#Сравнение айди пользователя
#data - longpool.listen() event
#target - target user id
#return true or false
def IsGetUserEquals(data, target):
    return IsUserEquals(GetUserId(data), target)