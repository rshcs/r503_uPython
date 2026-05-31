# `soft_reset`

Source: `r503u.py` (method `R503.soft_reset`)

## Summary

Perform a soft reset of the R503 module.

## Signature

```py
soft_reset()
```

## Parameters

This method has no parameters.

## Returns

- Confirmation code integer (`0` means success).

## Details

- Performs software reset command (`0x3D`) and returns confirmation code.

## Example

```py
from r503u import R503

fp = R503()
result = fp.soft_reset()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L738](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L738)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
