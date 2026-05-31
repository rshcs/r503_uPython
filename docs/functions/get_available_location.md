# `get_available_location`

Source: `r503u.py` (method `R503.get_available_location`)

## Summary

Provides next available location in fingerprint library

## Signature

```py
get_available_location(index_page=0)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `index_page` | `int` | `0` | See method description and examples. |

## Returns

- See method implementation for exact return structure.

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.get_available_location()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L758](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L758)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
