from rolepermissions.roles import AbstractUserRole

class People(AbstractUserRole):
    available_permissions = {
        'make_transfer': True,
        'receive_tranfer': True
    }

class Company(AbstractUserRole):
    available_permissions = {
        'make_transfer': False,
        'receive_tranfer': True
    }
