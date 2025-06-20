from collect_data import collect_data
from tabulate_data import tabulate_data
import os

PAGE_LIMIT = 5 # set page limit here

def main():    
    PRODUCT_NAME = input("Please enter a product name: ")
    if PRODUCT_NAME == "":
        print("Please enter a valid product name")
        return

    collect = "N" # Set whether you want to collect data or not
    if not os.path.isdir(f"data/{PRODUCT_NAME}") or len(os.listdir(f"data/{PRODUCT_NAME}")) == 0:
        collect = input("No data exists. Do you want to collect data? [Y/N]: ")

    
    if collect == "Y" or collect == 'y':
        collect_status = collect_data(PRODUCT_NAME, PAGE_LIMIT=PAGE_LIMIT)
        if collect_status is False:
            print("Data collection failed")
    
    
    if not os.path.isdir(f"data/{PRODUCT_NAME}"):
        print(f"The directory for '{PRODUCT_NAME}' wasn't created. Collect Data first!")
        tabulate_status = False
    else:
        tabulate_status = tabulate_data(PRODUCT_NAME)
    
    if tabulate_status is False:
        print("Data tabulation failed")
    else:
        print("YAY! You can check the output in the results folder")

if __name__ == "__main__":
    main()