from kata_2022.clean_coders.ioc.file import Reader, Writer


class KeyBoard(Reader):
    def get_char(self):
        pass


class Mouse(Reader):
    def get_event(self):
        pass


class Printer(Writer):
    def put_char(self):
        pass


class Monitor(Writer):
    def put_char(self):
        pass
