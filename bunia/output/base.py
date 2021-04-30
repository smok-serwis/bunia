import base64


def transcode_output(data, form, dtype='binary'):
    """
    Transcode data (bytes) to target form

    :param data: binary data
    :param form: one of 'text', 'html', 'raw', 'base64', 'ascii'
    :param dtype: one of 'binary' or 'text'
    """
    if form not in ('text', 'html', 'raw', 'base64', 'ascii'):
        raise ValueError('Invalid form')
    if dtype not in ('binary', 'text'):
        raise ValueError('Invalid dtype')

    if form in ('text', 'html'):
        if dtype == 'text':
            return data
        else:
            return data.decode('utf-8')
    elif form == 'raw':
        if dtype == 'text':
            return data.encode('utf-8')
        else:
            return data
    elif form == 'base64':
        if dtype == 'text':
            data = data.encode('utf-8')
        return base64.b64encode(data).decode('utf-8')
    elif form == 'ascii':
        if dtype == 'binary':
            data = data.decode('ascii')
        return data
    else:
        raise ValueError('Invalid form!')


class Output(object):
    """
    An access to some form of output. Override and extend as needed. This is constructed
    by a Runner in response to command request.

    :ivar name: (tp.Optional[str]) - output name
    """

    def __init__(self, name=None):
        self.name = name

    def to(self, form='text'):
        """Output content in some particular form.

        It is mandatory to support 'text'.

        Possible values are 'text', 'html'. This is the last call to this objects,
        as Output can close its resources.

        :raises ValueError: form not supported
        :return: depends on form. unicode for text and html
        """
