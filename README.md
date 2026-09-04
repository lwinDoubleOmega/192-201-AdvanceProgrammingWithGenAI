# Day 1: Python Basics

## Goal

By the end of today, you will be able to:

- store information in variables;
- work with strings, integers, floats, and booleans;
- read keyboard input;
- convert text input into a number;
- print a calculated result;
- run a Python program from the terminal.

## Core ideas

### Variables

A variable gives a value a name:

```python
student_name = "Alex"
age = 24
temperature = 30.5
is_learning = True
```

Good variable names describe what the value means. Python convention uses
`snake_case`, such as `temperature_celsius`.

### Common data types

| Type | Example | Purpose |
| --- | --- | --- |
| `str` | `"Bangkok"` | Text |
| `int` | `25` | Whole number |
| `float` | `25.5` | Decimal number |
| `bool` | `True` | True/false state |

You can inspect a value's type with `type(value)`.

### Input and conversion

`input()` always returns text, even when the user enters a number:

```python
age_text = input("Enter your age: ")
age = int(age_text)
```

Use `float(...)` when decimal values should be accepted.

### Formatted output

An f-string can place a value inside text:

```python
city = "Bangkok"
print(f"I live in {city}.")
```

## Main exercise: temperature converter

Complete `temperature_converter.py`. It should:

1. Ask the user for their name.
2. Ask for a temperature in Celsius.
3. Convert the temperature to Fahrenheit using:

   `fahrenheit = (celsius * 9 / 5) + 32`

4. Print a friendly result containing the name, Celsius value, and Fahrenheit value.

Example interaction:

```text
What is your name? Alex
Enter a temperature in Celsius: 30
Hello Alex! 30.0°C is 86.0°F.
```

Run it from this directory with:

```bash
python3 temperature_converter.py
```

## Extra challenges

Complete these only after the main exercise works:

1. Round the Fahrenheit result to one decimal place using `round(value, 1)`.
2. Print the data type of the Celsius value.
3. Add a Boolean variable named `is_freezing` that is `True` when the Celsius
   value is zero. For now, test it using an input of `0`; conditions come later.

## Completion checklist

- [ ] The program runs without an error.
- [ ] It accepts a decimal such as `36.5`.
- [ ] The calculation is correct for `0°C` (`32°F`).
- [ ] The calculation is correct for `100°C` (`212°F`).
- [ ] Variable names use `snake_case`.
- [ ] I can explain why `float(input(...))` is needed.

