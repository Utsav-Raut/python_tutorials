# Here are some rules for overriding:
#   The name of the method should be the same and its parameters as well
# IF the superclass method is private (prefixed with double-score), then you can't override it.

# In python super() method is used for overriding. It has the following syntax:
# super(class_namem, self).override_method_name()

class base(object):
    def base_func(self):
        print('Method of base class')

class child(base):
    def base_func(self):
        print('Method of child class')
        super(child, self).base_func()

class next_child(child):
    def base_func(self):
        print('Method of next_child class')
        super(next_child, self).base_func()

obj = next_child()
obj.base_func()