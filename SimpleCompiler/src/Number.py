class Number:
    def __init__(self, value):
        self.value = value  # Valore numerico, ad esempio "5" o "10.5"

    def __repr__(self):
        return f"Number(value={self.value})"