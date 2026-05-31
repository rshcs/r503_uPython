# `search`

Source: `r503u.py` (method `R503.search`)

## Summary

Search the whole finger library for the template that matches the one in CharBuffer 1 or 2

## Signature

```py
search(buff_num=1, start_id=0, para=200, timeout=10)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `buff_num` | `int` | `1` | See method description and examples. |
| `start_id` | `int` | `0` | See method description and examples. |
| `para` | `int` | `200` | See method description and examples. |
| `timeout` | `int` | `10` | See method description and examples. |

## Returns

- Tuple `(status, template_number, match_score)`.
- `status=0` means match success, `status=9` means no matching fingerprint, `99` means timeout/no response.

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.search()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L550](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L550)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
