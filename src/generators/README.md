# Generator
* We can create generator expressions without building and holding the entire object in memory before iteration.
* When the yield statement is hit, the program suspends function execution and returns the yielded value (return stops execution completely). 
* When a function is suspended, the state of that function is saved. This includes any variable bindings local to the generator, the instruction pointer, the internal stack, and any exception handling.