# `set_address`

Source: `r503u.py` (method `R503.set_address`)

## Summary

Set module address *Set the new address when setting the class object next time* parameter: (int) new_addr

## Signature

```py
set_address(new_addr)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `new_addr` | `int/bytes/any` | `required` | See method description and examples. |

## Returns

- (int) confirmation code => 0 [success], 1, 24, 99

## Details

- *Set the new address when setting the class object next time*
- parameter: (int) new_addr

## Example

```py
from r503u import R503

fp = R503()
result = fp.set_address(new_addr=<value>)
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L58](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L58)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
