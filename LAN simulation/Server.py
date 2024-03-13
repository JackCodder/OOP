class Server:
    """описания работы серверов в сети"""

    server_ip = 1

    def __init__(self):
        self.buffer = []
        self.ip = Server.server_ip
        Server.server_ip += 1
        self.router = None

    def send_data(self, data):
        """для отправки информационного пакета data с указанным IP-адресом получателя"""
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        """возвращает список принятых пакетов"""
        b = self.buffer[:]
        self.buffer.clear()
        return b

    def get_ip(self):
        """возвращает свой IP-адрес"""
        return self.ip