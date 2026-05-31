# `auto_enroll`

Source: `r503u.py` (method `R503.auto_enroll`)

## Summary

Automatically register a fingerprint template.

## Signature

```py
auto_enroll(location_id, duplicate_id=1, duplicate_fp=1, ret_status=1, finger_leave=1)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `location_id` | `int` | `required` | The location ID to store the template. |
| `duplicate_id` | `int` | `1` | The duplicate check method. |
| `duplicate_fp` | `int` | `1` | Whether to return duplicate finger status. |
| `ret_status` | `int` | `1` | Return registration status. |
| `finger_leave` | `int` | `1` | Whether finger leaves sensor during registration. |

## Returns

- The confirmation code 0 if success

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.auto_enroll(location_id=<value>)
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L612](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L612)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
