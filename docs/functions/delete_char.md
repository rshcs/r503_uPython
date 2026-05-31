# `delete_char`

Source: `r503u.py` (method `R503.delete_char`)

## Summary

Delete stored fingerprint templates.

## Signature

```py
delete_char(page_num, num_of_temps_to_del=1)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `page_num` | `int/any` | `required` | The page number (index) to delete templates from. |
| `num_of_temps_to_del` | `int/any` | `1` | The number of templates to delete. Default is 1. |

## Returns

- Confirmation code integer.
- This function will:
- - Pack the page number and number of templates to delete into a packet.
- - Send the delete instruction packet to the sensor.
- - Return the confirmation code response from the sensor.

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.delete_char(page_num=<value>)
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L522](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L522)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
