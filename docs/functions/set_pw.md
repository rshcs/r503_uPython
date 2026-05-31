# `set_pw`

Source: `r503u.py` (method `R503.set_pw`)

## Summary

Set modules handshaking password

## Signature

```py
set_pw(new_pw)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `new_pw` | `int/bytes/any` | `required` | See method description and examples. |

## Returns

- See method implementation for exact return structure.

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.set_pw(new_pw=<value>)
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L48](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L48)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
