class InterfaceNotUpException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'InterfaceNotUpException, {0} '.format(self.message)
        else:
            return 'A default interface is not up exception has been raised'


class IpNotCorrectException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'IpNotCorrectException, {0} '.format(self.message)
        else:
            return 'A default IP-address not correct exception has been raised'


class EIGRPProtoNotActiveException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'EIGRPProtoNotActiveException, {0} '.format(self.message)
        else:
            return 'A default EIGRP protocol is not active exception has been raised'


class APIError(Exception):
    """An API Error Exception"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: status={}".format(self.status)
