class Motorcycle:
    MAKE_LEN_MIN = 2
    MAKE_LEN_MAX = 15
    MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'

    MODEL_LEN_MIN = 1
    MODEL_LEN_MAX = 15
    MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'

    CATEGORY_LEN_MIN = 3
    CATEGORY_LEN_MAX = 10
    CATEGORY_LEN_ERR = f'Category must be between {CATEGORY_LEN_MIN} and {CATEGORY_LEN_MAX} characters long!'

    WHEELS_COUNT = 2

    def __init__(self, make, model, price, category):
        self._validate_make(make)
        self._validate_model(model)
        self._validate_price(price)
        self._validate_category(category)

        self.make = make
        self.model = model
        self.price = price
        self.category = category
        self.wheels = Motorcycle.WHEELS_COUNT

    def _validate_make(self, make):
        if not (Motorcycle.MAKE_LEN_MIN <= len(make) <= Motorcycle.MAKE_LEN_MAX):
            raise ValueError(Motorcycle.MAKE_LEN_ERR)

    def _validate_model(self, model):
        if not (Motorcycle.MODEL_LEN_MIN <= len(model) <= Motorcycle.MODEL_LEN_MAX):
            raise ValueError(Motorcycle.MODEL_LEN_ERR)

    def _validate_price(self, price):
        if not (Motorcycle.PRICE_MIN <= price <= Motorcycle.PRICE_MAX):
            raise ValueError(Motorcycle.PRICE_ERR)


    def _validate_category(self, category):
        if not (Motorcycle.CATEGORY_LEN_MIN <= len(category) <= Motorcycle.CATEGORY_LEN_MAX):
            raise ValueError(Motorcycle.CATEGORY_LEN_ERR)