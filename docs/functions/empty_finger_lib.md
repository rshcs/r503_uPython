# `empty_finger_lib`

Source: `r503u.py` (method `R503.empty_finger_lib`)

## Summary

Empty all stored fingerprints. This function will: - Send the empty library instruction to the sensor. - Return the confirmation code response.

## Signature

```py
empty_finger_lib()
```

## Parameters

This method has no parameters.

## Returns

- Confirmation code integer.

## Details

- This function will:
- - Send the empty library instruction to the sensor.
- - Return the confirmation code response.

## Example

```py
from r503u import R503

fp = R503()
result = fp.empty_finger_lib()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L573](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L573)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
