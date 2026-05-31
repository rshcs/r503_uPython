# `read_valid_template_num`

Source: `r503u.py` (method `R503.read_valid_template_num`)

## Summary

Read number of valid templates stored in module.

## Signature

```py
read_valid_template_num()
```

## Parameters

This method has no parameters.

## Returns

- num_templates (int): Number of valid templates stored.

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.read_valid_template_num()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L587](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L587)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
