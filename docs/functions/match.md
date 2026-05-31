# `match`

Source: `r503u.py` (method `R503.match`)

## Summary

Compare the recently extracted character with the templates in the ModelBuffer, providing matching result.

## Signature

```py
match()
```

## Parameters

This method has no parameters.

## Returns

- (tuple) status: [0: matching, 1: error, 8: not matching], match score

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.match()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L542](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L542)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
