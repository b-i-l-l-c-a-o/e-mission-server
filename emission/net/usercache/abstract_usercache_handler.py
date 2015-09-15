import logging

class UserCacheHandler(object):
    @staticmethod
    def getUserCacheHandler(uuid):
        """
            Returns the current usercache handler configured in the config file,
            or the builtin cache if nothing is configured
        """
        # We put the import statement in here to avoid circular dependencies
        # It is also not needed anywhere else since this is a completely static
        # function otherwise
        import emission.net.usercache.builtin_usercache_handler as biuc
        return biuc.BuiltinUserCacheHandler(uuid)

    def __init__(self, uuid):
        self.uuid = uuid

    def moveToLongTerm(self):
        """
        Moves all messages that have arrived for the current user into long-term
        storage, after converting into a platform-independent format.
        """
        pass
