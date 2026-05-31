# `wakeup_pin_status`

Source: `r503u.py` (method `R503.wakeup_pin_status`)

## Summary

Wake up the pin status. Return value is 0 if finger is on the sensor or hovering above the sensor, Returns 1 if no finger is on the sensor.

## Signature

```py
wakeup_pin_status()
```

## Parameters

This method has no parameters.

## Returns

- See method implementation for exact return structure.

## Details

- if no finger is on the sensor.

## Example

```py
from r503u import R503

fp = R503()
result = fp.wakeup_pin_status()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L39](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L39)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
