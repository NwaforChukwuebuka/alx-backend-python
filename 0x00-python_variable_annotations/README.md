# Variable Annotations in Python 3

This project is focused on mastering variable and type annotations in Python 3. It contains a series of tasks designed to familiarize you with type-annotated functions, complex types, and duck typing.

## Learning Objectives

By the end of this project, you should be able to:
- Understand and implement type annotations in Python 3.
- Use type annotations to specify function signatures and variable types.
- Apply duck typing and validate code using MyPy.

## Tasks

### 0. Basic Annotations - Add
**File**: `0-add.py`

Implement a type-annotated function `add` that takes two floats, `a` and `b`, as arguments and returns their sum as a float.

### 1. Basic Annotations - Concat
**File**: `1-concat.py`

Implement a type-annotated function `concat` that takes two strings, `str1` and `str2`, as arguments and returns a concatenated string.

### 2. Basic Annotations - Floor
**File**: `2-floor.py`

Implement a type-annotated function `floor` which takes a float `n` as an argument and returns the floor of the float.

### 3. Basic Annotations - To String
**File**: `3-to_str.py`

Implement a type-annotated function `to_str` that takes a float `n` as an argument and returns the string representation of the float.

### 4. Define Variables
**File**: `4-define_variables.py`

Define and annotate the following variables with the specified values:
- `a`: an integer with a value of `1`.
- `pi`: a float with a value of `3.14`.
- `i_understand_annotations`: a boolean with a value of `True`.
- `school`: a string with a value of `"Holberton"`.

### 5. Complex Types - List of Floats
**File**: `5-sum_list.py`

Implement a type-annotated function `sum_list` which takes a list `input_list` of floats as an argument and returns their sum as a float.

### 6. Complex Types - Mixed List
**File**: `6-sum_mixed_list.py`

Implement a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.

### 7. Complex Types - String and Int/Float to Tuple
**File**: `7-to_kv.py`

Implement a type-annotated function `to_kv` that takes a string `k` and an int or float `v` as arguments and returns a tuple. The first element of the tuple is the string `k`. The second element is the square of the int/float `v` and should be annotated as a float.

### 8. Complex Types - Functions
**File**: `8-make_multiplier.py`

Implement a type-annotated function `make_multiplier` that takes a float `multiplier` as an argument and returns a function that multiplies a float by `multiplier`.

### 9. Let's Duck Type an Iterable Object
**File**: `9-element_length.py`

Annotate the function `element_length` shown below with the appropriate types:

```python
def element_length(lst):
    return [(i, len(i)) for i in lst]
```

### 10. Duck Typing - First Element of a Sequence
**File**: `100-safe_first_element.py`

Augment the following code with the correct duck-typed annotations:

```python
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
```

### 11. More Involved Type Annotations
**File**: `101-safely_get_value.py`

Include type annotations for the following function:

```python
def safely_get_value(dct, key, default=None):
    if key in dct:
        return dct[key]
    else:
        return default
```

### 12. Type Checking
**File**: `102-type_checking.py`

Validate the code below with MyPy and apply any necessary changes:

```python
def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
```

---
