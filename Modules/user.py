class User:
    def __init__(self, FN, LN, UN, Pass):
        self.__firstName = FN
        self.__lastName = LN
        self.__username = UN
        self.__password = Pass
        self.__status = False

    @property
    def firstName(self): return self.__firstName

    @firstName.setter
    def firstName(self, val): 
        self.__firstName = val

    @property
    def lastName(self): return self.__lastName

    @lastName.setter
    def lastName(self, val): 
        self.__lastName = val

    @property
    def username(self): return self.__username

    @username.setter
    def username(self, val): 
        self.__username = val

    @property
    def password(self): return self.__password

    @password.setter
    def password(self, val): 
        self.__password = val
        
    @property
    def status(self): return self.__status

    @status.setter
    def status(self, val): 
        self.__status = val