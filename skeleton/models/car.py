class Car:
    MAKE_LEN_MIN = 2
    MAKE_LEN_MAX = 15
    MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'

    MODEL_LEN_MIN = 1
    MODEL_LEN_MAX = 15
    MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'

    CAR_SEATS_MIN = 1
    CAR_SEATS_MAX = 10
    CAR_SEATS_ERR = f'Seats must be between {CAR_SEATS_MIN} and {CAR_SEATS_MAX}!'

    WHEELS_COUNT = 4

    def __init__(self, make, model, price, seats):
        self._validate_make(make)
        self._validate_model(model)
        self._validate_price(price)
        self._validate_seats(seats)

        self.make = make
        self.model = model
        self.price = price
        self.seats = seats
        self.wheels = Car.WHEELS_COUNT

    def _validate_make(self, make):
        if not (Car.MAKE_LEN_MIN <= len(make) <= Car.MAKE_LEN_MAX):
            raise ValueError(Car.MAKE_LEN_ERR)

    def _validate_model(self, model):
        if not (Car.MODEL_LEN_MIN <= len(model) <= Car.MODEL_LEN_MAX):
            raise ValueError(Car.MODEL_LEN_ERR)

    def _validate_price(self, price):
        if not (Car.PRICE_MIN <= price <= Car.PRICE_MAX):
            raise ValueError(Car.PRICE_ERR)

    def _validate_seats(self, seats):
        if not (Car.CAR_SEATS_MIN <= seats <= Car.CAR_SEATS_MAX):
            raise ValueError(Car.CAR_SEATS_ERR)
