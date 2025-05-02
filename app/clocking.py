from datetime import datetime
from ..db.dbManager import dbManager

class Clocking(dbManager):
    def __init__(self, dbname):
        super().__init__(dbname)
        self