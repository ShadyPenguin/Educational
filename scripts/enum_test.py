import enum


class Test(enum.Enum):
    FOO = enum.auto()
    BAR = enum.auto()

    def action(self):
        if self == Test.FOO:
            print("foo")
        elif self == Test.BAR:
            print("bar")


foo = Test.FOO
foo.action()
bar = Test.BAR
bar.action()
