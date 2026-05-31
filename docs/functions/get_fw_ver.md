# `get_fw_ver`

Source: `r503u.py` (method `R503.get_fw_ver`)

## Summary

Get firmware version.

## Signature

```py
get_fw_ver()
```

## Parameters

This method has no parameters.

## Returns

- (int, int): A tuple containing the confirmation code and firmware version.
- The serial number is returned in recv_data[4].
- The firmware version is returned in recv_data[5].

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.get_fw_ver()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L711](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L711)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
