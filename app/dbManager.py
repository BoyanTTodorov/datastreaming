# Importing libraries
# abc abstract classes
from abc import ABC, abstractmethod
# sqlite3 will be our database
import sqlite3

# Base class for dbManager with ABC - Abstract Class it cannot be instantiated directly
class baseDbManager(ABC):
    """
    Base dbManager class that will centralize subclasses,
    reduce redundancy, and handle errors.
    """
    # Creating a base class and initializing it
    def __init__(self, dbname=None, *args, **kwargs):
        super().__init__()
        # Saving dbname as base because all instances will need it
        self.dbname = dbname

    def _connect(self):
        """
        Establish a connection to sqlite3 for _execute_query method    
        """
        return sqlite3.connect(self.dbname)
    
    def _execute_query(self, query, *args, commit=False):
        """
        Execute query method needed for each CRUD operation
        """
        try:
            print(f"Executing query: {query}")
            connection = self._connect()
            curs = connection.cursor()
            curs.execute(query, *args, commit)
            if commit:
                connection.commit()
            result = curs.fetchall()
            connection.close()
            return result
        except Exception as e:
            print(f"An error occurred: {e}")

    # Base CRUD methods
    @abstractmethod
    def create(self, query, *args, **kwargs):
        pass

    @abstractmethod
    def read(self, query, *args, **kwargs):
        pass 

    @abstractmethod
    def update(self, query, *args, **kwargs):
        pass

    @abstractmethod
    def delete(self, query, *args, **kwargs):
        pass

# dbManager class that inherits from baseDbManager
class dbManager(baseDbManager):
    # Initializing the class
    def __init__(self, dbname=None, *args, **kwargs):
        # Initialize superclass
        super().__init__(dbname, *args, **kwargs)
    # Base CRUD operations using base _execute_query method
    def create(self, query, *args, **kwargs):
        return self._execute_query(query, *args, commit=True)

    def read(self, query, *args, **kwargs):
        return self._execute_query(query, *args)

    def update(self, query, *args, **kwargs):
        return self._execute_query(query, *args, commit=True)

    def delete(self, query, *args, **kwargs):
        return self._execute_query(query, *args, commit=True)
