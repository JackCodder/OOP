from Server import Server
from Router import Router
from Data import Data

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

#Тесты
# assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
# assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"

# assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"

# assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"

# assert hasattr(router, 'buffer') and hasattr(sv_to, 'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"

# router.unlink(sv_to)
# sv_from.send_data(Data("Hello", sv_to.get_ip()))
# router.send_data()
# msg_lst_to = sv_to.get_data()
# assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"

print('GOOD')