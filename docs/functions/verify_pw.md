# `verify_pw`

Source: `r503u.py` (method `R503.verify_pw`)

## Summary

Verify modules handshaking password

## Signature

```py
verify_pw(pw=0)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `pw` | `int` | `0` | See method description and examples. |

## Returns

- See method implementation for exact return structure.

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.verify_pw()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L228](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L228)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
