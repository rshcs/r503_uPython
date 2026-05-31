# `read_notepad`

Source: `r503u.py` (method `R503.read_notepad`)

## Summary

Read data from a specific notepad page in module memory.

## Signature

```py
read_notepad(page_no)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `page_no` | `int` | `required` | The page number to read, 0-15 |

## Returns

- status (int): Status code, -1 if invalid page
- data (bytearray): Data read from the page

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.read_notepad(page_no=<value>)
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L783](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L783)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
