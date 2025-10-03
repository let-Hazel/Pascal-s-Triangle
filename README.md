# Pascal's Triangle: Learning Python Basics and TDD

Welcome! This project will teach you Python fundamentals and Test-Driven Development (TDD) through building Pascal's Triangle.

## What is Pascal's Triangle?

Pascal's Triangle is a triangular array of numbers where:
- The top row is just `1`
- Each number is the sum of the two numbers directly above it
- The edges are always `1`

```
       1
      1 1
     1 2 1
    1 3 3 1
   1 4 6 4 1
  1 5 10 10 5 1
```

## Prerequisites

- Python 3.8 or higher installed
- Basic command line knowledge
- A text editor or IDE (VS Code, PyCharm, or similar)

**No external packages needed!** unittest comes built-in with Python.

## Setup

1. **Create a project directory:**
```bash
mkdir pascal_triangle_tdd
cd pascal_triangle_tdd
```

2. **Create project files:**
```bash
touch pascal_triangle.py
touch test_pascal_triangle.py
```

## Project Structure

```
pascal_triangle_tdd/
│
├── pascal_triangle.py       # Your implementation code
├── test_pascal_triangle.py  # Your test code
└── README.md               # This file
```

## What is Test-Driven Development (TDD)?

TDD is a development approach where you:
1. **Write a test** for a feature (it will fail initially - "Red")
2. **Write minimal code** to make the test pass ("Green")
3. **Refactor** your code to improve it while keeping tests passing

This cycle is called **Red-Green-Refactor**.

## Learning Path

### Phase 1: Basic Python Concepts

You'll learn:
- Functions and return values
- Lists and list operations
- Loops (for loops)
- Conditional statements (if/else)
- List indexing and slicing

### Phase 2: Testing Fundamentals

You'll learn:
- Writing test classes and methods
- Using unittest assertions
- Running tests from command line
- Understanding test output
- setUp and tearDown methods
- Edge cases and boundary conditions

### Phase 3: Building Pascal's Triangle

You'll implement functions to:
1. Generate a single row of Pascal's Triangle
2. Generate multiple rows
3. Handle edge cases (row 0, negative inputs)
4. Pretty-print the triangle

## Getting Started: Your First Test

Open `test_pascal_triangle.py` and write your first test:

```python
import unittest
from pascal_triangle import generate_row

class TestPascalTriangle(unittest.TestCase):
    
    def test_first_row(self):
        """Test that the first row of Pascal's Triangle is [1]"""
        result = generate_row(0)
        self.assertEqual(result, [1])

if __name__ == '__main__':
    unittest.main()
```

Run the test:
```bash
python test_pascal_triangle.py
```

The test will **fail** because `generate_row` doesn't exist yet. This is expected!

Now open `pascal_triangle.py` and write the minimal code to pass:

```python
def generate_row(row_num):
    """Generate a single row of Pascal's Triangle"""
    return [1]
```

Run the test again - it should pass! ✓

## Progression Steps

Follow these steps in order, writing tests first, then implementation:

### Step 1: First Two Rows
- Test and implement row 0: `[1]`
- Test and implement row 1: `[1, 1]`

### Step 2: Calculating Row Values
- Test row 2: `[1, 2, 1]`
- Test row 3: `[1, 3, 3, 1]`
- Test row 4: `[1, 4, 6, 4, 1]`

### Step 3: Edge Cases
- Test negative row numbers (should raise an error or return empty)
- Test very large row numbers

### Step 4: Multiple Rows
- Create a function `generate_triangle(num_rows)` that returns all rows up to `num_rows`

### Step 5: Pretty Printing
- Create a function to display the triangle nicely formatted

## Running Tests

```bash
# Run all tests
python test_pascal_triangle.py

# Run with verbose output
python test_pascal_triangle.py -v

# Run a specific test method
python test_pascal_triangle.py TestPascalTriangle.test_first_row

# Discover and run all tests in directory
python -m unittest discover

# Run with more detailed output
python -m unittest test_pascal_triangle -v
```

## Understanding unittest Structure

### Basic Test Class Template

```python
import unittest
from pascal_triangle import generate_row

class TestPascalTriangle(unittest.TestCase):
    
    def setUp(self):
        """Run before each test method - optional"""
        # Initialize any data needed for tests
        pass
    
    def tearDown(self):
        """Run after each test method - optional"""
        # Clean up after tests
        pass
    
    def test_something(self):
        """Each test method must start with 'test_'"""
        result = generate_row(0)
        self.assertEqual(result, [1])

if __name__ == '__main__':
    unittest.main()
```

### Key Points

- Test classes inherit from `unittest.TestCase`
- Test methods must start with `test_`
- Use `self.assert*` methods for validation
- Include `if __name__ == '__main__': unittest.main()` at the bottom

## Common unittest Assertions

```python
# Equality checks
self.assertEqual(a, b)          # a == b
self.assertNotEqual(a, b)       # a != b

# Boolean checks
self.assertTrue(x)              # bool(x) is True
self.assertFalse(x)             # bool(x) is False

# Membership checks
self.assertIn(a, b)             # a in b
self.assertNotIn(a, b)          # a not in b

# Comparison checks
self.assertGreater(a, b)        # a > b
self.assertLess(a, b)           # a < b
self.assertGreaterEqual(a, b)   # a >= b
self.assertLessEqual(a, b)      # a <= b

# Type checks
self.assertIsInstance(a, int)   # isinstance(a, int)

# Exception checks
with self.assertRaises(ValueError):
    generate_row(-1)

# List/collection checks
self.assertListEqual(a, b)      # Compare lists
```

## Test Cases to Consider

Think about what test cases you should write. Here are some ideas to get you started:

- What should the first row look like?
- What about the second row?
- How do you test rows with calculated values (rows 2, 3, 4, 5)?
- What happens with invalid inputs (negative numbers)?
- Do the rows have the correct length?
- Can you generate multiple rows at once?

Remember: Write one test at a time, make it pass, then move to the next!

## Tips for Success

1. **Write tests first** - Don't skip this! It's the core of TDD
2. **Start simple** - Begin with the easiest cases
3. **One test at a time** - Don't write multiple tests before implementing
4. **Keep tests readable** - Use descriptive names and docstrings
5. **Run tests frequently** - After every small change
6. **Use descriptive assertion messages** - Add custom messages to assertions:
   ```python
   self.assertEqual(result, expected, "Row 5 should have 6 elements")
   ```

## Understanding Test Output

When you run tests, you'll see output like:

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

- Each `.` represents a passing test
- `F` represents a failure
- `E` represents an error
- Use `-v` flag for more detailed output

## Resources

- [Python unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Pascal's Triangle - Wikipedia](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
- [TDD Explained](https://en.wikipedia.org/wiki/Test-driven_development)

## Success Criteria

You'll know you've mastered the basics when you can:
- Write test classes with multiple test methods
- Use appropriate unittest assertions
- Write tests before writing implementation code
- Generate any row of Pascal's Triangle
- Handle edge cases gracefully
- Explain what each test is validating
- Refactor code without breaking tests

## Challenge Extensions

After completing the basic project, try these challenges:

1. **Mathematical Properties**: Add tests and implementation for:
   - Sum of each row equals 2^n
   - Symmetry of rows
   - Binomial coefficients

2. **Performance**: Test and optimize for large row numbers

3. **Output Formatting**: Create a pretty-printer that centers the triangle:
   ```
          1
        1   1
      1   2   1
    1   3   3   1
   ```

4. **Interactive Mode**: Create a command-line interface to generate rows

## Next Steps

After completing this project, you can:
- Explore more TDD projects (Fibonacci, Prime Numbers, FizzBuzz)
- Learn about test coverage tools (coverage.py)
- Study test doubles (mocks, stubs) for complex scenarios
- Build a web API for Pascal's Triangle with tested endpoints

Happy coding! Remember: **Red, Green, Refactor!** 🔴 🟢 🔧