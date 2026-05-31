# `get_image_ex`

Source: `r503u.py` (method `R503.get_image_ex`)

## Summary

Detect a finger and store it in image_buffer return 0x07 if image poor quality

## Signature

```py
get_image_ex()
```

## Parameters

This method has no parameters.

## Returns

- (int) confirmation code

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.get_image_ex()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L403](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L403)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
