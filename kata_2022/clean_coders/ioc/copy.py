from kata_2022.clean_coders.ioc.file import Reader, Writer


class Copy:
    def __init__(self, reader: Reader, writer: Writer):
        self.reader = reader
        self.writer = writer

    def execute(self):
        while self.reader.get_char() != None:
            self.writer.put_char()
