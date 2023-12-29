import requests as req
from bs4 import BeautifulSoup
from utils import write_csv

def scrape_amazon_deals() -> None:
    """
    Scrapes product information from an Amazon deals page and writes the data to a CSV file.

    This function performs the following steps:
    1. Sends a GET request to the specified Amazon deals page.
    2. Parses the HTML content of the page using BeautifulSoup.
    3. Extracts product information (product name, discount percentage, discount price, actual price) from the HTML.
    4. Writes the extracted data to a CSV file using the 'write_csv' function.

    Note:
    - The script is specifically designed for an Amazon deals page structure.
    - The 'write_csv' function is assumed to be defined in an external 'utils' module.

    :return: None
    """
    try:
        # Send a GET request to the Amazon deals page
        page = req.get('https://www.amazon.com/deal/9ed8bf39/?_encoding=UTF8&_encoding=UTF8&showVariations=true&ref_=dlx_gate_dd_dcl_tlt_9ed8bf39_dt_pd_gw_unk')

        # Check if the request was successful (status code 200)
        page.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(page.content, "html.parser")

        # Find all product elements on the page
        contents = soup.find_all('li', class_='a-list-normal a-spacing-none no-margin-right overflow-hidden octopus-response-li-width')

        # If no product elements are found, print a message and return early
        if not contents:
            print("No product elements found on the page.")
            return

        # Extract information for each product and write to CSV
        for product in contents:
            product_name = product.find('a', class_='a-size-base a-color-base a-link-normal a-text-normal').text
            discount_percentage = product.find('span', class_='a-size-medium a-color-price octopus-widget-saving-percentage').text
            discount_price = product.find('span', class_='a-offscreen').text
            actual_price = product.find('span', class_='a-size-mini a-color-tertiary octopus-widget-strike-through-price a-text-strike').text

            # Data to write in CSV
            data = {
                'product_name': product_name,
                'discount_price': discount_price,
                'actual_price': actual_price,
                'discount_percentage': discount_percentage,
            }

            # Write the data to CSV
            write_csv(data)

    except req.RequestException as req_err:
        print(f"Request to Amazon failed: {req_err}")

    except KeyboardInterrupt:
        print("Keyboard interruption detected. Exiting gracefully.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    # Execute the scrape_amazon_deals function
    scrape_amazon_deals()
