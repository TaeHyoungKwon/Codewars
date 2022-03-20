from kata_2022.clean_coders.ioc.file import Reader, Writer


def _get_mouse():
    pass


def _get_keyboard():
    pass


def _get_monitor():
    pass


def _get_printer():
    pass


def copy(self, is_mouse, is_monitor):
    if is_mouse:
        reader = _get_mouse()
    else:
        reader = _get_keyboard()

    if is_monitor:
        writer = _get_monitor()
    else:
        writer = _get_printer()

    while reader.get_char() != None:
        writer.put_char()


if __name__ == "__main__":
    copy(is_mouse=True, is_monitor=True)
