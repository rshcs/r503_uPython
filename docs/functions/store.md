# `store`

Source: `r503u.py` (method `R503.store`)

## Summary

Store a fingerprint template to the module's flash library.

## Signature

```py
store(buffer_id, page_id)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `buffer_id` | `int` | `required` | 1 for buffer1, 2 for buffer2 |
| `page_id` | `int` | `required` | Page number to store the template |

## Returns

- conf_code (int): The confirmation code received after storing.
- 0 means success.

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.store(buffer_id=<value>, page_id=<value>)
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L430](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L430)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
