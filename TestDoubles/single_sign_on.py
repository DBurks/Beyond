import random

class SingleSignonRegistry:

    def register_new_session(self, credentials):
        """Returns an instance of SSOToken if the credentials are valid"""
        pass

    def is_valid(self, token):
        """Returns True uf the token referes to a current session"""
        pass

    def unregister(self, token):
        """Remove the given token from the current session"""
        pass

class SSOToken:
    def __init__(self):
        self.id = random.randrange(100000)

    def __eq__(self, o):
        return self.id == o.guid

    def __repr__(self):
        return str(self.id)