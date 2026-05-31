# `read_index_table`

Source: `r503u.py` (method `R503.read_index_table`)

## Summary

Read the fingerprint template index table

## Signature

```py
read_index_table(index_page=0)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `index_page` | `int` | `0` | See method description and examples. |

## Returns

- List of template indices stored in selected index page.
- Returns `99` when communication fails.

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.read_index_table()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L596](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L596)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
