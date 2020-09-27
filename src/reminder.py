class PrefixedReminder:
    """This class acts as a base class for other types of reminders.
    Classes that subclass it should override the `self.text` property
    """
    def __init__(self, prefix="Hey, don't forget to "):
        self.prefix = prefix
        self.text = prefix + '<placeholder_text>'

class PoliteReminder(PrefixedReminder):
    """This class acts is derived from base class PrefixedReminder
    """
    def __init__(self, text):
        super().__init__()
	self.prefix = "Please "
        self.text   = text
	return(self.prefix + self.test)
