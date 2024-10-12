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

### task 9:
Annotate the below function’s parameters and return values with the appropriate types
```py3
def element_length(lst):
    return [(i, len(i)) for i in lst]
```

```bash
bob@dylan:~$ cat 9-main.py 
#!/usr/bin/env python3

element_length =  __import__('9-element_length').element_length

print(element_length.__annotations__)
bob@dylan:~$ ./9-main.py 
{'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}

```


### task 100:
Augment the following code with the correct duck-typed annotations:

```py3
# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
```
```bash
bob@dylan:~$ cat 100-main.py 
#!/usr/bin/env python3

safe_first_element =  __import__('100-safe_first_element').safe_first_element

print(safe_first_element.__annotations__)
```


### task 101:
### Understanding `TypeVar` and `T` in Python

In Python's type hinting system (introduced in PEP 484), **`TypeVar`** is used to define a generic type, allowing you to write functions or classes that can work with any type. It gives flexibility to specify that certain types in your code should be related or constrained, without being too specific about what the exact type should be.

#### What is `TypeVar`?

- **`TypeVar`** is a way of defining a type placeholder that can be reused in type annotations.
- It helps make your code **generic** by indicating that the same type should be used across multiple places in a function or class.
- You can think of it as a variable for types (not values). It allows us to say, "I don't care what the exact type is, but it must be the same type everywhere this `TypeVar` is used."

The simplest syntax for defining a `TypeVar` is:
```python
from typing import TypeVar

T = TypeVar('T')
```

Here, `T` is a generic type variable. It could represent any type (like `int`, `str`, `float`, `list`, etc.). You can choose any letter or name, but by convention, `T`, `S`, `U`, etc. are used. 

#### Why is `T` used?

In the code you provided:
```python
T = TypeVar('T')
```

- **`T`** is a `TypeVar` that acts as a **placeholder for a type**. When we use `T`, it indicates that a particular type will be used consistently in certain places within a function or class.
- In other words, wherever `T` is mentioned, it refers to the same specific type, but what that type is will be determined when the function is used (or "instantiated").

#### Example: Generic Function Using `T`

```python
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    if key in dct:
        return dct[key]
    else:
        return default
```

**Breaking it down:**

1. **`T = TypeVar('T')`**: 
   - `T` is a generic type placeholder. It doesn't have a specific type assigned yet. It could be `int`, `str`, `list`, or any other type.
   
2. **`dct: Mapping[Any, T]`**: 
   - This means that the dictionary `dct` can have keys of any type (`Any`), but the values in the dictionary all have to be of the same type `T`.
   - So, if the dictionary is `{'a': 1, 'b': 2}`, then `T` would be `int`. If the dictionary is `{'a': 'apple', 'b': 'banana'}`, then `T` would be `str`.

3. **`default: Union[T, None]`**: 
   - The `default` argument can either be of type `T` (same type as the values in the dictionary) or `None`.

4. **`return: Union[T, None]`**: 
   - The function returns either a value of type `T` or `None`, depending on whether the key is found in the dictionary or not.

### How `TypeVar` Works in Practice

#### Example 1: Integer Dictionary
```python
my_dict = {"a": 1, "b": 2, "c": 3}
value = safely_get_value(my_dict, "a")
# Type of value: int (T = int in this context)
```

- When you call `safely_get_value(my_dict, "a")`, `T` is inferred to be `int` because the values in `my_dict` are integers. The return type of the function is `int`.

#### Example 2: String Dictionary
```python
my_dict = {"a": "apple", "b": "banana", "c": "cherry"}
value = safely_get_value(my_dict, "d", "default")
# Type of value: str (T = str in this context)
```

- When you call `safely_get_value(my_dict, "d", "default")`, `T` is inferred to be `str` because the values in `my_dict` are strings, and the `default` value is also a string. The return type of the function is `str`.

### `TypeVar` vs Using a Fixed Type (e.g., `int` or `str`)

Without `TypeVar`, you'd have to write separate functions for each type, like this:

```python
def safely_get_value_int(dct: Mapping[Any, int], key: Any, default: Union[int, None] = None) -> Union[int, None]:
    # similar logic, but only works for dictionaries with int values

def safely_get_value_str(dct: Mapping[Any, str], key: Any, default: Union[str, None] = None) -> Union[str, None]:
    # similar logic, but only works for dictionaries with str values
```

This would get cumbersome and repetitive. By using `TypeVar`, you can write one function that works with any type, without sacrificing type safety.
---
