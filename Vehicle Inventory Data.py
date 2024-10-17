import csv

def display_menu():
    print('Menu:\n1. Display Inventory\n2. Update Vehicle Price\n3. Sort Inventory by Make\n4. Calculate Price Change for a Make\n5. Exit')
    while True:
        try: 
            choice = int(input('Enter your choice (1-5): '))
            break
        except ValueError:
                print('Invalid choice. Please choose again')           
    return choice

import csv

def load_inventory(file_path):
    inventory = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            car = {
                f"{row['Make']}_{row['Model']}_{row['Year']}":{
                'Make': row['Make'],
                'Model': row['Model'],
                'Year': int(row['Year']),
                'Price': float(row['Price'])
            }}
            inventory.append(car)
    return inventory

def display_inventory(inventory):
    for car in inventory:
        car_key = list(car.keys())[0]  # Get the car key (Make_Model_Year)
        car_info = car[car_key]
        print(f"{car_info['Make']} {car_info['Model']} ({car_info['Year']}) ${car_info['Price']:.2f}")

def update_price(inventory, make, model, year, new_price):
    for car in inventory:
        car_key = list(car.keys())[0]  # Get the car key (Make_Model_Year)
        car_info = car[car_key]  # Get the inner dictionary containing car details
        if car_info['Make'] == make and car_info['Model'] == model and car_info['Year'] == year:
            car_info['Price'] = new_price
            print('Price updated successfully.')
            return  
    print('Vehicle not Found in Inventory!')
    

    
def sort_by_make(inventory):
    sorted_inventory = sorted(inventory, key=lambda car: car[list(car.keys())[0]]['Make'])
    for car in sorted_inventory:
        car_key = list(car.keys())[0]  # Get the car key (Make_Model_Year)
        car_info = car[car_key]  # Get the inner dictionary containing car details
        print(f"{car_info['Make']} {car_info['Model']} ({car_info['Year']}) ${car_info['Price']:.2f}")

def calculate_price_change(inventory, model):
    older_price = None
    newer_price = None
    model_found = False

    for car in inventory:
        car_key = list(car.keys())[0]  # Get the car key (Make_Model_Year)
        car_info = car[car_key]  # Get the inner dictionary containing car details
        if car_info['Model'].upper() == model and car_info['Year'] == 2022:
            older_price = car_info['Price']
            model_found = True
        elif car_info['Model'].upper() == model and car_info['Year'] == 2024:
            newer_price = car_info['Price']
            model_found = True

    if model_found and older_price is not None and newer_price is not None:
        price_change_percentage = ((newer_price - older_price) / older_price) * 100
        print(f"Vehicle: {model}, (Year: 2024)")
        print(f"Old Price: ${older_price:.2f}, New Price: ${newer_price:.2f}")
        print(f"Change: {price_change_percentage:.2f}%")
    else:
        print("Not Enough Data to Calculate Price Change!!")

def update_file(filename, inventory):
    pass

def main():
    inventory_file = 'vehicle_inventory.csv'
    inventory = load_inventory(inventory_file)
    task = 0
    while task != 5:
        task = display_menu()
        if task == 1:
            display_inventory(inventory)
            print()
        elif task == 2:
            make = input('Enter the make of the vehicle: ')
            model = input('Enter the model of the vehicle: ')
            year = int(input('Enter the year of the vehicle: '))
            new_price = float(input('Enter the new price of the vehicle: '))
            update_price(inventory, make, model, year, new_price)
            print()
        elif task == 3:
            sort_by_make(inventory)
        
            print()
        elif task == 4:
            model = input('Enter the model to calculate price change: ').upper()
            calculate_price_change(inventory, model)
            print()
        else:
            print('Exiting the program. Goodbye!')

if __name__ == "__main__":
    main()

