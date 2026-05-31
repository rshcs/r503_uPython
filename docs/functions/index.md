# Function Index

Select a method to open comprehensive documentation.

| Method | Description | Source line |
| --- | --- | --- |
| [`auto_enroll`](auto_enroll.md) | Automatically register a fingerprint template. | `r503u.py:612` |
| [`auto_identify`](auto_identify.md) | Search and verify a fingerprint. | `r503u.py:628` |
| [`cancel`](cancel.md) | Cancel instruction. | `r503u.py:79` |
| [`check_sensor`](check_sensor.md) | Check whether the sensor is normal. | `r503u.py:245` |
| [`confirmation_decode`](confirmation_decode.md) | Decode confirmation code to understandable string parameter: (int) c_code - confirmation code. | `r503u.py:254` |
| [`delete_char`](delete_char.md) | Delete stored fingerprint templates. | `r503u.py:522` |
| [`down_char`](down_char.md) | ** Not tested with MicroPython ** Download a fingerprint template to the sensor module buffer. | `r503u.py:361` |
| [`down_image`](down_image.md) | ** Not tested with MicroPython ** Download image from the upper computer to the image buffer. | `r503u.py:302` |
| [`down_packet`](down_packet.md) | ** Not tested with MicroPython ** Send a downlink data packet to the sensor module. | `r503u.py:317` |
| [`empty_finger_lib`](empty_finger_lib.md) | Empty all stored fingerprints. | `r503u.py:573` |
| [`get_alg_ver`](get_alg_ver.md) | Get the algorithm version from the fingerprint sensor. | `r503u.py:725` |
| [`get_available_location`](get_available_location.md) | Provides next available location in fingerprint library. | `r503u.py:758` |
| [`get_fw_ver`](get_fw_ver.md) | Get firmware version. | `r503u.py:711` |
| [`get_image_ex`](get_image_ex.md) | Detect a finger and store it in image_buffer return 0x07 if image poor quality. | `r503u.py:403` |
| [`get_img`](get_img.md) | Detect a finger and store it in image_buffer. | `r503u.py:395` |
| [`get_random_code`](get_random_code.md) | Generate a random 32-bit integer from the sensor module. | `r503u.py:749` |
| [`handshake`](handshake.md) | Send handshake instructions to the module, Confirmation code 0 receives if the sensor is normal. | `r503u.py:237` |
| [`img2tz`](img2tz.md) | Generate character file from the original image in Image Buffer and store the file in CharBuffer 1 to 6 parameter: (int) buffer_id, 1 to 6. | `r503u.py:411` |
| [`led_control`](led_control.md) | ctrl: (int) 1 to 6 1: breathing light, 2: flashing light, 3: always on, 4: always off, 5: gradually on, 6: gradually off speed: (int) 0 to 255 color: (int) 0 to 7 cycles: (int) 0 to 255. | `r503u.py:87` |
| [`load_char`](load_char.md) | ** Not tested with MicroPython ** Load template ath the specified location of flash library to template buffer. | `r503u.py:264` |
| [`manual_enroll`](manual_enroll.md) | Manually enroll a fingerprint to the device memory. | `r503u.py:444` |
| [`match`](match.md) | Compare the recently extracted character with the templates in the ModelBuffer, providing matching result. | `r503u.py:542` |
| [`read_index_table`](read_index_table.md) | Read the fingerprint template index table. | `r503u.py:596` |
| [`read_info_page`](read_info_page.md) | Read the information page. | `r503u.py:384` |
| [`read_notepad`](read_notepad.md) | Read data from a specific notepad page in module memory. | `r503u.py:783` |
| [`read_prod_info`](read_prod_info.md) | Read product information from the fingerprint sensor. | `r503u.py:640` |
| [`read_prod_info_decode`](read_prod_info_decode.md) | Decode raw product info into a human-readable dictionary. | `r503u.py:669` |
| [`read_sys_para`](read_sys_para.md) | Status register and other basic configuration parameters. | `r503u.py:181` |
| [`read_sys_para_decode`](read_sys_para_decode.md) | Get system parameters in a decoded, human-readable format. | `r503u.py:189` |
| [`read_valid_template_num`](read_valid_template_num.md) | Read number of valid templates stored in module. | `r503u.py:587` |
| [`reg_model`](reg_model.md) | Combine info of character files in CharBuffer 1 to 6 and generate a template which is stored in CharBuffers 1 and 2 input. | `r503u.py:420` |
| [`search`](search.md) | Search the whole finger library for the template that matches the one in CharBuffer 1 or 2. | `r503u.py:550` |
| [`set_address`](set_address.md) | Set module address *Set the new address when setting the class object next time* parameter: (int) new_addr. | `r503u.py:58` |
| [`set_baud`](set_baud.md) | Set the baud rate for serial communication. | `r503u.py:99` |
| [`set_pkg_length`](set_pkg_length.md) | Set the package length for serial communication. | `r503u.py:153` |
| [`set_pw`](set_pw.md) | Set modules handshaking password. | `r503u.py:48` |
| [`set_security`](set_security.md) | Set the security level of the fingerprint sensor. | `r503u.py:127` |
| [`simplified_enroll`](simplified_enroll.md) | Simplified enrollment of fingerprints. | `r503u.py:496` |
| [`soft_reset`](soft_reset.md) | Perform a soft reset of the R503 module. | `r503u.py:738` |
| [`store`](store.md) | Store a fingerprint template to the module's flash library. | `r503u.py:430` |
| [`up_char`](up_char.md) | ** Not tested with MicroPython ** Upload the data in template buffer to the upper computer parameter: (int) timeout: timeout could vary if you change the baud rate, for 57600baud 5seconds is sufficient If you use a lower baud rate timeout may have to be increased. | `r503u.py:337` |
| [`up_image`](up_image.md) | ** Not tested with MicroPython ** Upload the image in Img_Buffer to upper computer every image contains the data around 20kilo bytes parameter: (int) timeout: timeout could vary if you change the baud rate, for 57600baud 5seconds is sufficient If you use a lower baud rate timeout may have to be increased. | `r503u.py:277` |
| [`verify_pw`](verify_pw.md) | Verify modules handshaking password. | `r503u.py:228` |
| [`wakeup_pin_status`](wakeup_pin_status.md) | Wake up the pin status. | `r503u.py:39` |
| [`write_notepad`](write_notepad.md) | Write data to the specific flash pages: 0 to 15, each page contains 32bytes of data, any data type is given to the content will be converted to the string data type before writing to the notepad. | `r503u.py:766` |
