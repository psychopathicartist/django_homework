from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Класс, который отвечает за обработку входящих запросов
    """

    @staticmethod
    def __get_index():
        """
        Метод для чтения html файла
        """

        with open('index.html', 'r', encoding='utf-8') as file:
            response = file.read()

        return response

    def do_GET(self):
        """
        Метод для обработки входящих GET-запросов
        """

        page_content = self.__get_index()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    # Инициализация веб-сервера
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    # Остановка веб-сервера
    webServer.server_close()
    print("Server stopped.")
