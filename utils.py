import os
import csv

def write_csv(data, file_name='product.csv'):
    """
    Writes product information to a CSV file.

    This function checks if the specified CSV file exists. If the file does not exist,
    it creates a new CSV file with a header row. It then appends the provided product
    information to the CSV file.

    :param data: A dictionary containing product information.
     Keys: 'product_name', 'discount_price', 'actual_price', 'discount_percentage'.
    :type data: dict

    :param file_name: The name of the CSV file to write to (default is 'product.csv').
    :type file_name: str, optional

    :return: None
    """
    try:
        # Check if the provided data is a dictionary
        if not isinstance(data, dict):
            raise ValueError("The 'data' parameter must be a dictionary.")

        # Ensure that the provided file_name is a string
        if not isinstance(file_name, str):
            raise ValueError("The 'file_name' parameter must be a string.")

        is_exists_file = os.path.isfile(file_name)

        # If the file does not exist, create a new file with a header row
        if not is_exists_file:
            with open(file_name, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['product_name', 'discount_price', 'actual_price', 'discount_percentage'])

        # Append the product information to the CSV file
        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([data['product_name'], data['discount_price'], data['actual_price'], data['discount_percentage']])

    except Exception as e:
        # Handle any unexpected exceptions and print an error message
        print(f"Error writing to CSV: {e}")