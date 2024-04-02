class IPAddressValidator:
    @staticmethod
    def validate_decimal(value):
        try:
            num = int(value)
            return 0 <= num <= 255
        except ValueError:
            return False

    @staticmethod
    def validate_ip_address(ip):
        octets = ip.split('.')
        if len(octets) != 4:
            return False, "Invalid IP address format. It must consist of four decimal numbers separated by periods."

        for octet in octets:
            if not IPAddressValidator.validate_decimal(octet):
                return False, f"Invalid octet value: {octet}. Each number must be between 0 and 255, inclusive."

        binary_ip = ".".join(format(int(octet), '08b') for octet in octets)
        return True, binary_ip

class SubnetMaskValidator:
    @staticmethod
    def validate_subnet_mask(mask):
        binary_mask = "".join(format(int(octet), '08b') for octet in mask.split('.'))
        if '01' in binary_mask or '0' not in binary_mask:
            return False, "Invalid subnet mask. It must have a single run of 1's followed by a single run of 0's."

        return True, binary_mask

def main():
    ip_address = input("Enter IP address: ")
    is_valid_ip, binary_ip = IPAddressValidator.validate_ip_address(ip_address)
    if is_valid_ip:
        print(f"Valid IP address. Binary representation: {binary_ip}")
    else:
        print(binary_ip)

    subnet_mask = input("Enter subnet mask: ")
    is_valid_mask, binary_mask = SubnetMaskValidator.validate_subnet_mask(subnet_mask)
    if is_valid_mask:
        print(f"Valid subnet mask. Binary representation: {binary_mask}")
    else:
        print(binary_mask)

if __name__ == "__main__":
    main()
