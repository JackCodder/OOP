class Router:
    """описания работы роутеров в сети"""

    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        """для присоединения объекта класса Server к роутеру"""
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server):
        """для отсоединения объекта класса Server от роутера"""
        s = self.servers.pop(server.ip, False)
        if s:
            s.router = None

    def send_data(self):
        """отправка объектов класса Data из буфера роутера соответствующим серверам"""
        for d in self.buffer:
            if d.ip in self.servers:
                self.servers[d.ip].buffer.append(d)
        self.buffer.clear()