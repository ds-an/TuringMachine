class TuringMachine:
    def __init__(self, state, head, list):
        self.state = state
        self.head = head
        self.list = list

    def getState(self):
        return self.state

    def getHead(self):
        return self.head

    def getList(self):
        return self.list

    def machineUpdate(self):
        pass

