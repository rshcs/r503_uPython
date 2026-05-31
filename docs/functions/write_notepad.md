# `write_notepad`

Source: `r503u.py` (method `R503.write_notepad`)

## Summary

Write data to the specific flash pages: 0 to 15, each page contains 32bytes of data, any data type is given to the content will be converted to the string data type before writing to the notepad.

## Signature

```py
write_notepad(page_no, content)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `page_no` | `int/any` | `required` | (int) 1 - 15, page number |
| `content` | `int/any` | `required` | (any) data to write to the flash |

## Returns

- See method implementation for exact return structure.

## Details

- the content will be converted to the string data type before writing to the notepad.

## Example

```py
from r503u import R503

fp = R503()
result = fp.write_notepad(page_no=<value>, content=<value>)
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L766](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L766)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
