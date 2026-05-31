# `auto_identify`

Source: `r503u.py` (method `R503.auto_identify`)

## Summary

Search and verify a fingerprint

## Signature

```py
auto_identify(security_lvl=3, start_pos=0, end_pos=199, ret_key_step=0, num_of_fp_errors=1)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `security_lvl` | `int` | `3` | See method description and examples. |
| `start_pos` | `int` | `0` | See method description and examples. |
| `end_pos` | `int` | `199` | See method description and examples. |
| `ret_key_step` | `int` | `0` | See method description and examples. |
| `num_of_fp_errors` | `int` | `1` | See method description and examples. |

## Returns

- (tuple) fp store location, match score

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.auto_identify()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L628](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L628)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
