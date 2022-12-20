TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        cls_ = DialogWindows if TYPE_OS == 1 else DialogLinux
        obj = super().__new__(cls_)
        obj.name = args[0]
        return obj
