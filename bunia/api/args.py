class Argument(object):
    """
    Definition of an argument
    """

    def __init__(self, username, name=None, default=None, required=True, description=u''):
        """
        :param username: Name displayed to user
        :param name: Name of argument provided to run()
        :param default: default value
        :param required: Is it optional?
        :param description: description
        """
        self.description = description
        self.name = name or username
        self.username = username
        self.default = default
        self.required = required

    def clean(self, val):
        """
        Validate and convert value to target format
        :param val: value of parameter
        :type val: unicode
        :return: a value to set as value of parameter
        :raise ValueError: invalid value
        """
        return val


class DeviceArgument(object):
    """
    Argument is a valid master controller Device ID
    """
    def clean(self, val):
        from sai.devices import Device
        d = Device(val)
        if not d.exists():
            raise ValueError('Device does not exist')
        return d