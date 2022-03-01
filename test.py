class World:
    class_variable = 'Country'

    @classmethod
    def access(cls):
        print('This is class variable accessed in class method', World.class_variable)


a = World()
# We can access class variable in class method by class name and class class variable name
a.access()
