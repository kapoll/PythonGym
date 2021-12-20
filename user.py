class user:
    instances = []
    def __init__ (self, name, sex, age, height, weight):
        self.__class__.instances.append(self)
        self.id         = len(user.instances)              #creating ID form lenght of 'instances', id are shifting when deleting user 
        self.name       = name
        self.sex        = sex
        self.age        = age
        self.height     = height
        self.weight     = weight