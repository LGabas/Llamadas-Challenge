class Call:
    def __init__(self, duration_of_call: float, type_of_call: str):
        self.duration_of_call = duration_of_call
        self.type_of_call = type_of_call

    def __str__(self):
        return f"Call Duration (minutes): {self.duration_of_call}, Call Type: {self.type_of_call}"