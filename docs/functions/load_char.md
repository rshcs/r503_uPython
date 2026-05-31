# `load_char`

Source: `r503u.py` (method `R503.load_char`)

## Summary

** Not tested with MicroPython ** Load template ath the specified location of flash library to template buffer

## Signature

```py
load_char(page_id, buffer_id=1)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `page_id` | `int/bytes/any` | `required` | See method description and examples. |
| `buffer_id` | `int` | `1` | See method description and examples. |

## Returns

- See method implementation for exact return structure.

## Details

- Load template ath the specified location of flash library to template buffer

## Example

```py
from r503u import R503

fp = R503()
result = fp.load_char(page_id=<value>)
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L264](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L264)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
