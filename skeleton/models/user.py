from skeleton.models.comment import Comment
from skeleton.models.constants.user_role import UserRole
from skeleton.models.vehicle import Vehicle


class User:
    USERNAME_LEN_MIN = 2
    USERNAME_LEN_MAX = 20
    USERNAME_LEN_ERR = f'Username must be between {USERNAME_LEN_MIN} and {USERNAME_LEN_MAX} characters long!'
    USERNAME_INVALID_SYMBOLS = 'Username contains invalid symbols!'

    PASSWORD_LEN_MIN = 5
    PASSWORD_LEN_MAX = 30
    PASSWORD_LEN_ERR = f'Password must be between {PASSWORD_LEN_MIN} and {PASSWORD_LEN_MAX} characters long!'
    PASSWORD_INVALID_SYMBOLS = 'Password contains invalid symbols!'

    LASTNAME_LEN_MIN = 2
    LASTNAME_LEN_MAX = 20
    LASTNAME_LEN_ERR = f'Lastname must be between {LASTNAME_LEN_MIN} and {LASTNAME_LEN_MAX} characters long!'

    FIRSTNAME_LEN_MIN = 2
    FIRSTNAME_LEN_MAX = 20
    FIRSTNAME_LEN_ERR = f'Firstname must be between {FIRSTNAME_LEN_MIN} and {FIRSTNAME_LEN_MAX} characters long!'

    NORMAL_ROLE_VEHICLE_LIMIT = 5

    NORMAL_USER_LIMIT_REACHED_ERR = f'You are not VIP and cannot add more than {NORMAL_ROLE_VEHICLE_LIMIT} vehicles!'
    ADMIN_CANNOT_ADD_VEHICLES_ERR = 'You are an admin and therefore cannot add vehicles!'
    YOU_ARE_NOT_THE_AUTHOR = 'You are not the author of the comment you are trying to remove!'
    THE_VEHICLE_DOES_NOT_EXIT = 'The vehicle does not exist!'

    def __init__(self, username, password, firstname, lastname, role):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.role = role
        self.vehicles = []

    def get_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.id == vehicle_id:
                return vehicle
        return None

    def add_vehicle(self, vehicle):
        if self.role == UserRole.ADMIN:
            raise Exception(User.ADMIN_CANNOT_ADD_VEHICLES_ERR)
        if self.role == UserRole.NORMAL and len(self.vehicles) >= User.NORMAL_ROLE_VEHICLE_LIMIT:
            raise Exception(User.NORMAL_USER_LIMIT_REACHED_ERR)

        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle_id):
        vehicle = self.get_vehicle(vehicle_id)
        if vehicle:
            self.vehicles.remove(vehicle)
        else:
            raise Exception(User.THE_VEHICLE_DOES_NOT_EXIT)

    def add_comment(self, vehicle_id, comment_text):
        vehicle = self.get_vehicle(vehicle_id)
        if vehicle:
            comment = Comment(comment_text, self)
            vehicle.comments.append(comment)
        else:
            raise Exception(User.THE_VEHICLE_DOES_NOT_EXIT)

    def remove_comment(self, vehicle_id, comment_id):
        vehicle = self.get_vehicle(vehicle_id)
        if vehicle:
            comment_to_remove = next((c for c in vehicle.comments if c.id == comment_id), None)
            if comment_to_remove and comment_to_remove.author == self:
                vehicle.comments.remove(comment_to_remove)
            else:
                raise Exception(User.YOU_ARE_NOT_THE_AUTHOR)
        else:
            raise Exception(User.THE_VEHICLE_DOES_NOT_EXIT)
