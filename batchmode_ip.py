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

        binary_octets = [format(int(octet), '08b') for octet in octets]
        return True, ".".join(binary_octets)

def batch_ip_validator(input_file, output_file):
    with open(input_file, 'r') as file:
        ips = file.readlines()

    results = []
    for ip in ips:
        ip = ip.strip()
        is_valid, binary_ip = IPAddressValidator.validate_ip_address(ip)
        if is_valid:
            result = f"{ip} - Valid IP address. Binary representation: {binary_ip}\n"
        else:
            result = f"{ip} - Invalid IP address\n"
        results.append(result)

    with open(output_file, 'w') as file:
        file.writelines(results)

# Example usage with specified file paths
input_file_path = r'C:\Users\KOUSHIK\Downloads\IP_input.txt'
output_file_path = r'C:\Users\KOUSHIK\Downloads\IP_out.txt'
batch_ip_validator(input_file_path, output_file_path)
