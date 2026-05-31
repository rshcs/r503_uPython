# `down_char`

Source: `r503u.py` (method `R503.down_char`)

## Summary

** Not tested with MicroPython ** Download a fingerprint template to the sensor module buffer.

## Signature

```py
down_char(img_data, buffer_id=1)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `img_data` | `list` | `required` | The fingerprint template data split into packets. |
| `buffer_id` | `int` | `1` | The buffer ID to download to. Default is 1. |

## Returns

- int: The confirmation code from the module.
- This function downloads a full fingerprint template in packets
- to the specified buffer on the sensor module.

## Details

- Download a fingerprint template to the sensor module buffer.

## Example

```py
from r503u import R503

fp = R503()
result = fp.down_char(img_data=<value>)
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L361](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L361)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
