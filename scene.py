class Scene():
    def __init__(self):
        pass

    def draw(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def events(self):
        raise NotImplementedError

    def load_data(self):
        raise NotImplementedError
    
    def quit(self):
        raise NotImplementedError


