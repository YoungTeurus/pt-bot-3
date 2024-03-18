class ConsoleOutputter:
    # fixme: Временное решение, нужно сделать очередь сообщений на вывод, чтобы они не перекрывали друг друга
    #   Плюс нормально работать с вводом
    @staticmethod
    def toConsole(text: str):
        print(text)
