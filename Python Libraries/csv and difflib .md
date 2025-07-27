
# `csv` and `difflib` Modules

This guide introduces how to work with CSV files and perform fuzzy string matching using Python’s built-in libraries: `csv` and `difflib`. Examples use culturally familiar names such as **Srinivasa** and **Sowmya**.

---

## Part 1: Working with the `csv` Module

### Reading a CSV File

```python
import csv

with open('people.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

Assume `people.csv` contains:

```
Name,Age
Srinivasa,30
Sowmya,28
Raghavendra,35
```

**Output:**

```
['Name', 'Age']
['Srinivasa', '30']
['Sowmya', '28']
['Raghavendra', '35']
```

---

### Reading with `DictReader`

```python
with open('people.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'], row['Age'])
```

**Output:**

```
Srinivasa 30  
Sowmya 28  
Raghavendra 35
```

---

### Writing to a CSV File

```python
with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Srinivasa', '30'])
    writer.writerow(['Sowmya', '28'])
```

This creates a file `output.csv` with the content:

```
Name,Age
Srinivasa,30
Sowmya,28
```

---

## Part 2: Using `difflib` for Fuzzy Matching

### Getting Close Matches

```python
import difflib

name = "Srinivas"
possible_names = ["Srinivasa", "Sowmya", "Sridhar", "Sumanth"]

matches = difflib.get_close_matches(name, possible_names, n=2, cutoff=0.6)
print(matches)
```

**Output:**

```
['Srinivasa']
```

- `n=2` means return at most 2 matches  
- `cutoff=0.6` means match score must be at least 60%

---

### Comparing String Similarity

```python
from difflib import SequenceMatcher

name1 = "Sowmya"
name2 = "Soumya"

ratio = SequenceMatcher(None, name1, name2).ratio()
print(ratio)
```

**Output:**

```
0.833
```

This indicates that the strings are 83.3% similar.

---

## Summary

- The `csv` module allows reading/writing tabular data from/to CSV files.
- The `difflib` module enables fuzzy comparison of strings, useful for finding similar inputs.
