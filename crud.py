
products = []

while True:
 
    print("\n1. Show All Products")
    print("2. Add New Product")
    print("3. Delete a Product")
    print("4. Update Product Rating")
    print("5. Exit")
    
    option = input("Enter Option to Continue: ")

    if option == "1":
        
        if products:
            print("\n{:<5} {:<20} {:<20} {:<10} {:<20} {:<10}".format("ID", "Name", "Description", "Price", "Image", "Rating"))
            print("-" * 90)
            for product in products:
                print("{:<5} {:<20} {:<20} {:<10} {:<20} {:<10}".format(product['id'], product['name'], product['description'], product['price'], product['image'], product['rating']))
        else:
            print("\nNo products available!")
    
    elif option == "2":
      
        product = {}
        product['id'] = input("Enter Product ID: ")
        product['name'] = input("Enter Product Name: ")
        product['description'] = input("Enter Product Description: ")
        product['price'] = input("Enter Product Price: ")
        product['image'] = input("Enter Product Image: ")
        product['rating'] = input("Enter Product Rating: ")
        products.append(product)
        print(f"\nProduct '{product['name']}' added successfully!")

    elif option == "3":
        
        if products:
            prod_id = input("\nEnter the ID of the product to delete: ")
            for product in products:
                if product['id'] == prod_id:
                    products.remove(product)
                    print(f"\nProduct '{product['name']}' deleted successfully!")
                    break
            else:
                print("\nProduct not found!")
        else:
            print("\nNo products available to delete!")

    elif option == "4":
       
        if products:
            prod_id = input("\nEnter the ID of the product to update rating: ")
            for product in products:
                if product['id'] == prod_id:
                    new_rating = input(f"Enter new rating for {product['name']}: ")
                    product['rating'] = new_rating
                    print(f"\nProduct '{product['name']}' rating updated to {new_rating}!")
                    break
            else:
                print("\nProduct not found!")
        else:
            print("\nNo products available to update!")

    elif option == "5":
        
        print("Exiting...")
        break

    else:
        print("Invalid option! Please try again.")
