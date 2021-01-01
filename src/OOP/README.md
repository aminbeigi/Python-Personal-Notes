# Object Oriented Programming stuff

## Static and Class Methods 
* Instance methods need a class instance and can access the instance through self.
* Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.
* Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.

### When to use static methods?
* Use static methods when a particular method inside a class doesn't require access to that class.
* Flagging a method as static indicates that a method won't modify a class or instance state.