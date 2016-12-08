class Connection:
    def __init__(self, unique,ip, hostname):
        self.ip = ip
        self.hostname = hostname
        self.unique = unique

    def __str__(self):
        return str({"ip":self.ip, "hostname": self.hostname, "unique": self.unique})