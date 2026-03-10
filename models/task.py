class Task:
    def __init__(self, description, complete=False):
        self.description = description
        self.complete = complete
        self.data ={
            "description": self.description,
            "complete": self.complete
        }