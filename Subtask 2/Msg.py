from rich.console import Console
from time import time
import datetime
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
        return len(self._data)

    def __eq__(self, other):
        return str(self) == str(other)


    def __add__(self, other):
        if isinstance(other, BaseMsg):
            new_data = self._data + other._data
        else:
            new_data = self._data + str(other)
        return self.__class__(new_data)  # ensures same type as self




class LogMsg(BaseMsg):
    def __init__(self, data):
        super().__init__(data)
        self._timestamp: int = time() # erase dots and assign value to use it in __str__()
    def __str__(self):
        return f'[{datetime.datetime.fromtimestamp(self._timestamp)}] {self._data}' # BaseMsg-specific
    @property
    def style(self):
        return 'on yellow' # BaseMsg-specific


class WarnMsg(LogMsg):
    def __init__(self,data):
        super().__init__(data)
    def __str__(self):
        return f'[!WARN] [{datetime.datetime.fromtimestamp(self._timestamp)}] {self._data}'
    @property
    def style(self):
        return 'white on red' # BaseMsg-specific


if __name__ == '__main__':
    m1 = BaseMsg('Normal message')
    m2 = LogMsg('Log')
    m3 = WarnMsg('Warning')
    send_Msg(m1)
    send_Msg(m2)
    send_Msg(m3)