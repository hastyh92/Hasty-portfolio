# Hashmap Implementations

## Project Overview
This project includes two implementations of a **hashmap** data structure in Python:

1. **Open Addressing Hashmap**
2. **Separate Chaining Hashmap**

Hashmaps are a fundamental data structure used for efficient key-value pair storage and retrieval.

---

## Files Included
- `a6_include.py`: Utility or supporting functions for the project.
- `hash_map_oa.py`: Implementation of a hashmap using **open addressing**.
- `hash_map_sc.py`: Implementation of a hashmap using **separate chaining**.

---

## Implementations
### Open Addressing (hash_map_oa.py)
- **Method**: All key-value pairs are stored in a single array. Collisions are handled by probing for the next available slot (e.g., linear probing, quadratic probing).
- **Pros**: Lower memory overhead since no extra data structures (like linked lists) are used.
- **Cons**: Performance can degrade when the load factor increases.

### Separate Chaining (hash_map_sc.py)
- **Method**: Collisions are handled using linked lists at each bucket, where each bucket stores multiple key-value pairs.
- **Pros**: Efficient handling of collisions and flexible size.
- **Cons**: Slightly higher memory usage due to additional data structures.

---

## How to Run the Code
### Prerequisites
Make sure you have Python installed (version 3.8+ recommended).

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hashmap-implementations.git
   cd hashmap-implementations
   ```
2. Run the respective Python files:
   ```bash
   python hash_map_oa.py
   python hash_map_sc.py
   ```

---

## Examples
Below is an example of how the hashmaps work:

### Open Addressing Example
```python
from hash_map_oa import HashMapOA

# Initialize and use the hashmap
hashmap = HashMapOA()
hashmap.put('key1', 'value1')
print(hashmap.get('key1'))  # Output: value1
```

### Separate Chaining Example
```python
from hash_map_sc import HashMapSC

# Initialize and use the hashmap
hashmap = HashMapSC()
hashmap.put('key1', 'value1')
print(hashmap.get('key1'))  # Output: value1
```

---

## Features
- Supports basic operations: `put()`, `get()`, `remove()`, and `size()`.
- Clear implementation of two collision handling techniques.
- Easy to test and extend.

---

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for any bugs or feature suggestions.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Author
- **Your Name**
- GitHub: [Your GitHub Profile](https://github.com/your-username)
