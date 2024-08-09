from typing import Any


class person:
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)
        print("this is the person class")
    def PrintName(self):
        print(self.name)


p1 = person("ali")
p1.PrintName()