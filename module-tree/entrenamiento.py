#!/usr/bin/env python3
"""
Inventory Management Program
This program allows the user to add, search, update, delete products,
and calculate the total inventory value using functions, collections, and lambda.
"""

def agregar_producto(inventario):
    """
    Function to add a new product to the inventory.
    
    This function prompts the user for the product name, price, and available quantity.
    It validates the input and adds the product to the inventory dictionary if it does not already exist.
    The product is stored with its name as the key and a tuple (price, quantity) as the value.
    """
    nombre = input("Ingrese el nombre del producto: ").strip()
    # Check if the product already exists in the inventory
    if nombre in inventario:
        print("El producto ya existe. Si desea modificarlo, use la opción de actualizar.\n")
        return
    try:
        # Request price and quantity from the user and convert them to float and int respectively
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
    except ValueError:
        # Handle the case when the user inputs invalid numerical values
        print("Error: Se esperaba un valor numérico para el precio y/o la cantidad.\n")
        return
    # Add the new product to the inventory dictionary
    inventario[nombre] = (precio, cantidad)
    print(f"Producto '{nombre}' agregado exitosamente.\n")

def buscar_producto(inventario):
    """
    Function to search for a product in the inventory.
    
    This function asks the user for the product name, searches for it in the inventory,
    and then displays the product's details (price and quantity) if it is found.
    Otherwise, it notifies the user that the product does not exist.
    """
    nombre = input("Ingrese el nombre del producto a buscar: ").strip()
    # If the product is found, retrieve its details
    if nombre in inventario:
        precio, cantidad = inventario[nombre]
        print(f"Producto encontrado: {nombre} - Precio: {precio}, Cantidad: {cantidad}\n")
    else:
        # Notify that the product was not found
        print("El producto no existe en el inventario.\n")

def actualizar_precio(inventario):
    """
    Function to update the price of an existing product.
    
    This function asks the user for the product name and the new price.
    If the product exists, it updates its price while keeping the quantity unchanged.
    If the product does not exist or the new price is invalid, it notifies the user.
    """
    nombre = input("Ingrese el nombre del producto a actualizar: ").strip()
    if nombre in inventario:
        try:
            # Request the new price and convert it to float
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
        except ValueError:
            # Handle the case when the user inputs an invalid price
            print("Error: Se esperaba un valor numérico para el precio.\n")
            return
        # Retrieve the current quantity and update the price while preserving the quantity
        _, cantidad = inventario[nombre]
        inventario[nombre] = (nuevo_precio, cantidad)
        print(f"Precio del producto '{nombre}' actualizado a {nuevo_precio}.\n")
    else:
        # Notify that the product does not exist in the inventory
        print("El producto no existe en el inventario.\n")

def eliminar_producto(inventario):
    """
    Function to delete a product from the inventory.
    
    This function prompts the user for the product name and removes it from the inventory dictionary
    if it exists. If the product is not found, the user is notified.
    """
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    # Check if the product exists and delete it
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado exitosamente.\n")
    else:
        print("El producto no existe en el inventario.\n")

def calcular_valor_total(inventario):
    """
    Function to calculate the total value of the inventory.
    
    This function uses a lambda function to multiply the price by the quantity for each product,
    sums up these values, and prints the total inventory value.
    """
    # Lambda function that computes the total value of the inventory
    valor_total = lambda inv: sum(precio * cantidad for precio, cantidad in inv.values())
    total = valor_total(inventario)
    print(f"El valor total del inventario es: {total}\n")

def mostrar_inventario(inventario):
    """
    Function to display all products in the inventory in a readable format.
    
    If the inventory is empty, it notifies the user; otherwise, it prints each product's name, price, and quantity.
    """
    if not inventario:
        print("El inventario está vacío.\n")
        return
    print("Inventario de productos:")
    # Iterate over the inventory items and display each one
    for nombre, (precio, cantidad) in inventario.items():
        print(f" - {nombre}: Precio: {precio}, Cantidad: {cantidad}")
    print()

def main():
    """
    Main function that displays an interactive menu for managing the inventory.
    
    The menu allows the user to perform various operations such as adding, searching, updating,
    deleting products, calculating the total inventory value, displaying the inventory, or exiting the program.
    The function runs in a loop until the user chooses to exit.
    """
    # Initialize an empty inventory dictionary to store products
    inventario = {}
    
    while True:
        # Display the menu options
        print("----- Gestión de Inventario -----")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Mostrar inventario")
        print("7. Salir")
        
        opcion = input("Seleccione una opción (1-7): ").strip()
        print()
        
        # Execute the corresponding function based on the user's choice
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            buscar_producto(inventario)
        elif opcion == "3":
            actualizar_precio(inventario)
        elif opcion == "4":
            eliminar_producto(inventario)
        elif opcion == "5":
            calcular_valor_total(inventario)
        elif opcion == "6":
            mostrar_inventario(inventario)
        elif opcion == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            # Handle invalid menu options
            print("Opción no válida, por favor seleccione una opción entre 1 y 7.\n")

if __name__ == "__main__":
    main()
