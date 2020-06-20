from ninjarmmpy.system import SystemMixin
from ninjarmmpy.auth import NinjaAuthentication


class Client(SystemMixin):
    NINJA_API_US_BASE_URL = 'https://api.ninjarmm.com'
    NINJA_API_EU_BASE_URL = 'https://eu-api.ninjarmm.com'

    
    def __init__(self, AccessKeyID: str, SecretAccessKey: str, Europe=False):
        self.key = AccessKeyID
        self.secret = SecretAccessKey
        self.base_url = self.NINJA_API_US_BASE_URL if not Europe else self.NINJA_API_EU_BASE_URL
