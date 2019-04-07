# -*- coding: utf-8 -*-
from djitellopy import Tello
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType


def main():
    tello = Tello()
    tello.connect()

    vk_session = vk_api.VkApi(token='TOKEN')
    vk = vk_session.get_api()

    letsgo = VkKeyboard(one_time=True)
    letsgo.add_button('Начать', color=VkKeyboardColor.DEFAULT)

    keyboard_takeoff = VkKeyboard(one_time=True)
    keyboard_takeoff.add_button('Взлёт', color=VkKeyboardColor.POSITIVE)

    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Вверх', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Вниз', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Вперёд', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Влево', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Флип', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Вправо', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Проверка', color=VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button('Посадка', color=VkKeyboardColor.NEGATIVE)

    flip_keyboard = VkKeyboard(one_time=False)
    flip_keyboard.add_button('Флип вперёд', color=VkKeyboardColor.DEFAULT)
    flip_keyboard.add_line()
    flip_keyboard.add_button('Флип влево', color=VkKeyboardColor.DEFAULT)
    flip_keyboard.add_button('Флип вправо', color=VkKeyboardColor.DEFAULT)
    flip_keyboard.add_line()
    flip_keyboard.add_button('Флип назад', color=VkKeyboardColor.DEFAULT)
    flip_keyboard.add_line()
    flip_keyboard.add_button('Доступность флипа', color=VkKeyboardColor.NEGATIVE)
    flip_keyboard.add_line()
    flip_keyboard.add_button('Вернуться в меню управления', color=VkKeyboardColor.NEGATIVE)

    mainmenu_keyboard = VkKeyboard(one_time=True)
    mainmenu_keyboard.add_button('Начать', color=VkKeyboardColor.DEFAULT)
    mainmenu_keyboard.add_line()
    mainmenu_keyboard.add_button('Конец работы', color=VkKeyboardColor.DEFAULT)

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.text.lower() == 'флип':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=flip_keyboard.get_keyboard(),
                    message='Переход в меню флипов'
                )
            if event.text.lower() == 'начать':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=keyboard_takeoff.get_keyboard(),
                    message='Взлет?'
                )
            if event.text.lower() == 'конец работы':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    message='Конец работы'
                )
            if event.text.lower() == 'взлёт':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=keyboard.get_keyboard(),
                    message='Куда летим?'
                )
                tello.takeoff()
                print('Взлёт')
            if event.text.lower() == 'посадка':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=mainmenu_keyboard.get_keyboard(),
                    message='Посадка'
                )
                tello.land()
                print('Посадка')
            if event.text.lower() == 'вперёд':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=keyboard.get_keyboard(),
                    message='Полёт вперёд'
                )
                tello.move_forward(100)
                print('Вперёд')
            if event.text.lower() == 'влево':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=keyboard.get_keyboard(),
                    message='Полёт влево'
                )
                tello.move_left(100)
                print('Влево')
            if event.text.lower() == 'вправо':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=keyboard.get_keyboard(),
                    message='Полёт вправо'
                )
                tello.move_right(100)
                print('Вправо')
            if event.text.lower() == 'назад':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=keyboard.get_keyboard(),
                    message='Полёт назад'
                )
                tello.move_back(100)
                print('Назад')
            if event.text.lower() == 'проверка':
                x = tello.get_battery()
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=keyboard.get_keyboard(),
                    message='Заряд баттареи ' + x
                )
                print('Проверка')
            if event.text.lower() == 'вверх':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=keyboard.get_keyboard(),
                    message='Полёт вверх'
                )
                tello.move_up(20)
                print('Вверх')
            if event.text.lower() == 'вниз':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=keyboard.get_keyboard(),
                    message='Полёт вниз'
                )
                tello.move_down(20)
                print('Вниз')
            if event.text.lower() == 'флип назад':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=flip_keyboard.get_keyboard(),
                    message='Флип назад'
                )
                tello.flip('b')
                print('Флип назад')
            if event.text.lower() == 'флип вперёд':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=flip_keyboard.get_keyboard(),
                    message='Флип вперёд'
                )
                tello.flip('f')
                print('Флип вперёд')
            if event.text.lower() == 'флип влево':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=flip_keyboard.get_keyboard(),
                    message='Флип влево'
                )
                tello.flip('l')
                print('Флип влево')
            if event.text.lower() == 'флип вправо':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=flip_keyboard.get_keyboard(),
                    message='Флип вправо'
                )
                tello.flip('r')
                print('Флип вправо')
            if event.text.lower() == 'доступность флипа':
                x = tello.get_battery()
                if x == 'ok':
                    vk.messages.send(
                        user_id=event.user_id,
                        keyboard=flip_keyboard.get_keyboard(),
                        message='Нажмите ещё раз'
                    )
                else:
                    if int(x) > 50:
                        vk.messages.send(
                            user_id=event.user_id,
                            keyboard=flip_keyboard.get_keyboard(),
                            message='Заряд баттареи ' + x + 'Флип доступен'
                        )
                    else:
                        vk.messages.send(
                            user_id=event.user_id,
                            keyboard=flip_keyboard.get_keyboard(),
                            message='Заряд баттареи ' + x + 'Флип недоступен'
                        )
            if event.text.lower() == 'вернуться в меню управления':
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    keyboard=keyboard.get_keyboard(),
                    message='Возврат в меню управления'
                )
                print('Возврат в меню управления')
    tello.end()


if __name__ == '__main__':
    main()
