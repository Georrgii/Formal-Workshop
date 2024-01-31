class Truck:
    MAKE_LEN_MIN = 2
    MAKE_LEN_MAX = 15
    MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'

    MODEL_LEN_MIN = 1
    MODEL_LEN_MAX = 15
    MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'

    WEIGHT_CAP_MIN = 1
    WEIGHT_CAP_MAX = 100
    WEIGHT_CAP_ERR = f'Weight capacity must be between {WEIGHT_CAP_MIN} and {WEIGHT_CAP_MAX}!'

    WHEELS_COUNT = 8

    def __init__(self, make, model, price, weight_capacity):
        self._validate_make(make)
        self._validate_model(model)
        self._validate_price(price)
        self._validate_weight_capacity(weight_capacity)

        self.make = make
        self.model = model
        self.price = price
        self.weight_capacity = weight_capacity
        self.wheels = Truck.WHEELS_COUNT

    def _validate_make(self, make):
        if not (Truck.MAKE_LEN_MIN <= len(make) <= Truck.MAKE_LEN_MAX):
            raise ValueError(Truck.MAKE_LEN_ERR)

    def _validate_model(self, model):
        if not (Truck.MODEL_LEN_MIN <= len(model) <= Truck.MODEL_LEN_MAX):
            raise ValueError(Truck.MODEL_LEN_ERR)

    def _validate_price(self, price):
        if not (Truck.PRICE_MIN <= price <= Truck.PRICE_MAX):
            raise ValueError(Truck.PRICE_ERR)

    def _validate_weight_capacity(self, weight_capacity):
        if not (Truck.WEIGHT_CAP_MIN <= weight_capacity <= Truck.WEIGHT_CAP_MAX):
            raise ValueError(Truck.WEIGHT_CAP_ERR)

