# `confirmation_decode`

Source: `r503u.py` (method `R503.confirmation_decode`)

## Summary

Decode confirmation code to understandable string parameter: (int) c_code - confirmation code

## Signature

```py
confirmation_decode(c_code)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `c_code` | `int/bytes/any` | `required` | See method description and examples. |

## Returns

- (str) decoded confirmation code

## Details

- parameter: (int) c_code - confirmation code

## Example

```py
from r503u import R503

fp = R503()
result = fp.confirmation_decode(c_code=<value>)
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L254](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L254)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
