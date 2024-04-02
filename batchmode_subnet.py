class SubnetMaskValidator:
    @staticmethod
    def validate_decimal(value):
        try:
            num = int(value)
            return 0 <= num <= 255
        except ValueError:
            return False

    @staticmethod
    def validate_subnet_mask(mask):
        octets = mask.split('.')
        if len(octets) != 4:
            return False, "Invalid subnet mask format. It must consist of four decimal numbers separated by periods."

        for octet in octets:
            if not SubnetMaskValidator.validate_decimal(octet):
                return False, f"Invalid octet value: {octet}. Each number must be between 0 and 255, inclusive."

        binary_mask = "".join(format(int(octet), '08b') for octet in octets)
        if '01' in binary_mask or '0' not in binary_mask:
            return False, "Invalid subnet mask. It must have a single run of 1's followed by a single run of 0's."

        return True, binary_mask

def batch_mask_validator(input_file, output_file):
    with open(input_file, 'r') as file:
        masks = file.readlines()

    results = []
    for mask in masks:
        mask = mask.strip()
        if mask:  # Skip empty lines
            is_valid, binary_mask = SubnetMaskValidator.validate_subnet_mask(mask)
            if is_valid:
                result = f"{mask} - Valid subnet mask. Binary representation: {binary_mask}\n"
            else:
                result = f"{mask} - Invalid subnet mask\n"
            results.append(result)
        

    with open(output_file, 'w') as file:
        file.writelines(results)

# Example usage with specified file paths
input_file_path = r'C:\Users\ASUS\Desktop\CHARITHA\ELEWAYTE\Mask_input.txt'
output_file_path = r'C:\Users\ASUS\Desktop\CHARITHA\ELEWAYTE\Mask_out.txt'
batch_mask_validator(input_file_path, output_file_path)
