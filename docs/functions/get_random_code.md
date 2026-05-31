# `get_random_code`

Source: `r503u.py` (method `R503.get_random_code`)

## Summary

Generate a random 32-bit integer from the sensor module.

## Signature

```py
get_random_code()
```

## Parameters

This method has no parameters.

## Returns

- random_num (int): The 32-bit random integer value if success else 99

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.get_random_code()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L749](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L749)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
