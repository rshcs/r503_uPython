# `handshake`

Source: `r503u.py` (method `R503.handshake`)

## Summary

Send handshake instructions to the module, Confirmation code 0 receives if the sensor is normal

## Signature

```py
handshake()
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
result = fp.handshake()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L237](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L237)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
