# Python - Variable Annotations 
### 1. **Type Annotations in Python 3**

Type annotations in Python 3 allow you to explicitly declare the data types for function arguments, return types, and variables. Although Python is dynamically typed (you don't need to declare types), type annotations were introduced to provide a way to hint at what type a variable should be.

Here's an example:

```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```

In the example above:
- `a: int` means the function expects `a` to be of type `int`.
- `b: int` means the function expects `b` to be of type `int`.
- `-> int` specifies that the return type of the function is `int`.

Type annotations **do not enforce** the types at runtime, but they help developers understand the intended types, and they can be used with external tools like **mypy** to validate the code.

### 2. **Using Type Annotations to Specify Function Signatures and Variable Types**

#### Function Signatures

You can annotate function signatures by specifying the types of parameters and the return type. For example:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

- `name: str` means the function expects the `name` argument to be a string.
- `-> str` indicates that the function returns a string.

#### Variable Annotations

You can also specify the types of variables in Python:

```python
age: int = 25
is_active: bool = True
height: float = 1.75
name: str = "John"
```

You can even use annotations without initializing the variable immediately:

```python
result: float
```

This is purely informative to tell other developers (or tools) what type is expected.

#### Complex Types

For more complex types, you can use collections from the `typing` module:

- `List[int]`: A list that contains integers.
- `Dict[str, int]`: A dictionary with string keys and integer values.
- `Tuple[int, str]`: A tuple containing an integer and a string.

Example:

```python
from typing import List, Dict

def get_student_grades() -> Dict[str, List[int]]:
    return {
        "Alice": [85, 90, 92],
        "Bob": [75, 80, 89],
    }
```

### 3. **Duck Typing**

Duck typing in Python refers to the concept that the type or class of an object is less important than the methods or behaviors that the object supports. The name comes from the phrase:

> "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

In Python, you can pass any object to a function as long as it has the necessary methods and properties to fulfill its role, regardless of the actual type of the object.

Example:

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(make_animal_speak(dog))  # Woof!
print(make_animal_speak(cat))  # Meow!
```

In the example, both `Dog` and `Cat` have a `speak()` method, so `make_animal_speak()` works for both, without needing to check their actual class. This is duck typing.

### 4. **How to Validate Code with mypy**

**mypy** is a static type checker for Python. It checks your Python code against the type annotations you've provided and ensures that your code follows the expected types.

To use `mypy`, you must install it first. You can do that with pip:

```bash
pip install mypy
```

Once installed, you can validate your code by running the `mypy` command on your Python file(s):

```bash
mypy your_script.py
```

#### Example

Consider the following Python script:

```python
def divide(a: int, b: int) -> float:
    return a / b

result = divide(10, 2)
```

Running `mypy` on this script will pass, as the types are correct.

Now, if we introduce an error:

```python
def divide(a: int, b: int) -> float:
    return a // b  # Incorrect return type (int)

result = divide(10, 2)
```

Running `mypy`:

```bash
mypy your_script.py
```

mypy would report an error because the return type is an `int`, but we declared the return type as `float`.

### **How mypy Handles Duck Typing**
mypy can sometimes struggle with duck typing, as it expects specific types rather than behaviors. However, you can use `Protocol` from the `typing` module to define what behaviors or methods an object should have, without caring about its type.

```python
from typing import Protocol

class Animal(Protocol):
    def speak(self) -> str:
        ...

def make_animal_speak(animal: Animal) -> str:
    return animal.speak()
```

In this case, as long as an object passed to `make_animal_speak` has a `speak` method, mypy will accept it, even if the object is not an instance of a specific class.

---

### Summary:

1. **Type Annotations**: Provide hints for expected variable types and function signatures but don't enforce them at runtime.
2. **Duck Typing**: Focuses on what an object *can do* rather than its type.
3. **mypy**: A tool to validate Python code against type annotations, helping ensure that your program behaves as expected.
---
