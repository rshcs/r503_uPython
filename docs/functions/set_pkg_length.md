# `set_pkg_length`

Source: `r503u.py` (method `R503.set_pkg_length`)

## Summary

Set the package length for serial communication. This function sets the package length to one of the allowed values: 32, 64, 128 (default), 256 bytes.

## Signature

```py
set_pkg_length(pkg_len=128)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `pkg_len` | `int` | `128` | The desired package length. Default is 128. |

## Returns

- conf_code (int): The confirmation code received after setting
- the package length. 0 means success.
- It maps the package lengths to index values, checks if valid,
- sends the set command, updates self.recv_size if successful,
- and returns the confirmation code response.

## Details

- This function sets the package length to one of the allowed
- values: 32, 64, 128 (default), 256 bytes.

## Example

```py
from r503u import R503

fp = R503()
result = fp.set_pkg_length()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L153](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L153)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
