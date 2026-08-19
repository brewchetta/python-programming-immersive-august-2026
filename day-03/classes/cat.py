class Cat:

    # class attribute
    # this is the default number of lives that every Cat starts at
    number_of_lives = 9

    all_cats = []

    def __init__(self, name):
        self.name = name
        Cat.all_cats.append(self)

    def __repr__(self):
        return f"Cat(name={self.name}, number_of_lives={self.number_of_lives})"


# all cats start with 9 lives but if they change their number_of_lives they track those seperately
octavia = Cat(name="Octavia")
octavia.number_of_lives # 9
octavia.number_of_lives -= 1
octavia.number_of_lives # 8

ursula = Cat(name="Ursula")
ursula.number_of_lives # 9