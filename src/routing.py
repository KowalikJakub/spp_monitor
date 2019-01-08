routing_dict = {
    'index': '/',
    'login': '/loginPage',
    'auth' : '/auth' 
}

class IRouteBuilder(object):
    def create(self, key):
        pass

class PrefixedRouteBuilder(IRouteBuilder):
    def __init__(self, route_prefix):
        self.route_prefix = route_prefix
    def create(self, key):
        return self.route_prefix + routing_dict[key]