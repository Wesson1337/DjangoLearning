class Item:
    def __init__(self, name: str, description: str, weight: int):
        self.name = name
        self.description = description
        self.weight = weight

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'weight': str(self.weight)
        }
