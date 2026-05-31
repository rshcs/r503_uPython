# `get_alg_ver`

Source: `r503u.py` (method `R503.get_alg_ver`)

## Summary

Get the algorithm version from the fingerprint sensor.

## Signature

```py
get_alg_ver()
```

## Parameters

This method has no parameters.

## Returns

- (int, int): A tuple containing the algorithm version.
- The confirmation code is returned as the first tuple value.
- The algorithm version is returned as the second tuple value.

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.get_alg_ver()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L725](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L725)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
