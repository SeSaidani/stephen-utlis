def make_dev_id_from_mac_array(mac: list[int], prefix: int = 0x0100) -> int:
    """
    Create a device ID from a MAC address byte array.

    When we create a device ID from a mac address we take the 6 bytes of the mac address
    and copy them to the least significant 6 bytes of the dev id.
    We use a prefix to indicate where this address has come from and to ensure that
    addresses allocated by different organisations remain unique in loco.

    Args:
        mac (list[int]): List of 6 integers representing MAC address bytes.
        prefix (int): Prefix to indicate address source (default 0x0100).

    Returns:
        int: The constructed device ID.
    """
    # Ensure prefix is treated as 16-bit
    prefix_l = prefix & 0xFFFF

    # Combine the bytes using bitwise shifts
    # Prefix moves to bits 48-63
    # MAC bytes fill bits 0-47
    dev_id = (prefix_l << 48) | \
             ((mac[0] & 0xFF) << 40) | \
             ((mac[1] & 0xFF) << 32) | \
             ((mac[2] & 0xFF) << 24) | \
             ((mac[3] & 0xFF) << 16) | \
             ((mac[4] & 0xFF) << 8) | \
        (mac[5] & 0xFF)

    return dev_id


def get_raw_id_from_dev_id(dev_id: int) -> str:
    """
    Convert a Device ID back to the raw MAC string (e.g. 'A2A2A2008B34').
    Assumes the device ID has a 16-bit prefix and 48-bit MAC.
    """
    # Mask out the prefix (top 16 bits) to keep only the lower 48 bits (MAC address)
    mac_part = dev_id & 0xFFFFFFFFFFFF

    # Convert to hex string, upper case, and pad with zeros to 12 characters
    return f"{mac_part:012X}"

# Examples:
#
# mac_bytes = [0xA2, 0xA2, 0xA2, 0x00, 0x02, 0x0F]
#
# # Create Device ID
# result = make_dev_id_from_mac_array(mac_bytes)
# print(f"Device ID: {result}")
# # Output: 72059345700422159
#
# # Convert back to Raw ID
# raw_back = get_raw_id_from_dev_id(result)
# print(f"Raw ID back: {raw_back}")
# # Output: A2A2A200020F
