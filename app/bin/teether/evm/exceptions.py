class ExternalData(Exception):
    pass

class VMException(Exception):
    pass

class SymbolicError(Exception):
    pass


class IntractablePath(Exception):
    def __init__(self, trace=[], remainingpath=[]):
        self.trace = tuple(trace)
        self.remainingpath = tuple(remainingpath)


