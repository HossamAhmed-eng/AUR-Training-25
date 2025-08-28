from time import time
from rich.console import Console
console = Console()
def send_Msg(msg):
    if isinstance(msg, BaseMsg):
        console.print(msg, style=msg.style)
    else:
        print(msg)


class BaseMsg:
    def __init__(self, data: str):
        self._data = data
    
    @property
    def style(self):
        return '' # BaseMsg-specific
        
    @property
    def data(self):
        return self._data
    
    def __str__(self):
        return self._data # BaseMsg-specific
    
    def __len__(self):
        ... # erase this line and implement method
    
    def __eq__(self, other):
        ... # erase this line and implement method
    
    def __add__(self, other):
        ... # erase this line and implement method


class LogMsg(BaseMsg):
    def __init__(self, data):
        super().__init__(data)
        self._timestamp: int = ... # erase dots and assign value to use it in __str__()


class WarnMsg(LogMsg):
    ... # erase this line and reimplement specified methods


if __name__ == '__main__':
    m1 = BaseMsg('Normal message')
    m2 = LogMsg('Log')
    m3 = WarnMsg('Warning')
    send_Msg(m1)
    send_Msg(m2)
    send_Msg(m3)