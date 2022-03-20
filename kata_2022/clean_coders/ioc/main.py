from kata_2022.clean_coders.ioc.copy import Copy
from kata_2022.clean_coders.ioc.io_driver import Monitor, Mouse

if __name__ == "__main__":
    monitor = Monitor()
    mouse = Mouse()

    c = Copy(reader=mouse, writer=monitor)
    c.copy()
