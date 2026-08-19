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

    def meow(self):
        return "MEOW"

    # a decorator is a special modifier that changes a function in some way
    # decorators have the @ in front of them
    @classmethod
    def print_all_cat_names(cls):
        for cat in cls.all_cats:
            print(cat.name)
    # cls stands for the class itself
    # cls == Cat

    @classmethod
    def create_super_cat(cls, name):
        new_cat = cls(name)
        new_cat.number_of_lives = 81
        return new_cat


# all cats start with 9 lives but if they change their number_of_lives they track those seperately
octavia = Cat(name="Octavia")
octavia.number_of_lives # 9
octavia.number_of_lives -= 1
octavia.number_of_lives # 8

ursula = Cat(name="Ursula")
ursula.number_of_lives # 9