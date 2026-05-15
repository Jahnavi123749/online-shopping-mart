import datetime
import random
products = {
    1: {"name": "Laptop", "price": 50000, "stock": 5},
    2: {"name": "Mobile", "price": 20000, "stock": 10},
    3: {"name": "Headphones", "price": 2000, "stock": 15},
    4: {"name": "Keyboard", "price": 1500, "stock": 8},
    5: {"name": "Mouse", "price": 800, "stock": 20}
}
cart = {}
wishlist = []
def view_products():
    print("\n========== AVAILABLE PRODUCTS ==========")

    for pid, details in products.items():
        print(
            f"{pid}. {details['name']} | "
            f"Price: ₹{details['price']} | "
            f"Stock: {details['stock']}"
        )
def search_product():
    search = input("Enter Product Name: ").lower()

    found = False

    for details in products.values():
        if search in details["name"].lower():
            print(
                f"✅ Found: {details['name']} - ₹{details['price']}"
            )
            found = True

    if not found:
        print("❌ Product Not Found!")
def add_to_cart():
    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter Quantity: "))

    if product_id in products:

        product = products[product_id]

        if quantity <= product["stock"]:

            product_name = product["name"]

            if product_name in cart:
                cart[product_name]["quantity"] += quantity
            else:
                cart[product_name] = {
                    "price": product["price"],
                    "quantity": quantity
                }

            product["stock"] -= quantity

            print(f"✅ {product_name} Added To Cart!")

        else:
            print("❌ Insufficient Stock!")

    else:
        print("❌ Invalid Product ID!")

def remove_from_cart():

    item = input("Enter Product Name To Remove: ").title()

    if item in cart:

        quantity = cart[item]["quantity"]

        # Restore Stock
        for product in products.values():
            if product["name"] == item:
                product["stock"] += quantity

        del cart[item]

        print(f"✅ {item} Removed From Cart!")

    else:
        print("❌ Product Not Found In Cart!")
def update_quantity():

    item = input("Enter Product Name: ").title()

    if item in cart:

        new_quantity = int(input("Enter New Quantity: "))

        for product in products.values():

            if product["name"] == item:

                available = product["stock"] + cart[item]["quantity"]

                if new_quantity <= available:

                    product["stock"] = available - new_quantity
                    cart[item]["quantity"] = new_quantity

                    print("✅ Quantity Updated!")

                else:
                    print("❌ Stock Not Available!")

    else:
        print("❌ Product Not Found!")

def view_cart():

    if not cart:
        print("\n🛒 Cart Is Empty!")
        return

    print("\n========== YOUR CART ==========")

    total = 0

    for item, details in cart.items():

        subtotal = details["price"] * details["quantity"]
        total += subtotal

        print(
            f"{item} | ₹{details['price']} x "
            f"{details['quantity']} = ₹{subtotal}"
        )

    print("--------------------------------")
    print(f"Total Amount: ₹{total}")

# Function to Add Wishlist
def add_wishlist():

    item = input("Enter Product Name To Add Wishlist: ").title()

    found = False

    for product in products.values():

        if product["name"] == item:

            wishlist.append(item)
            print(f"❤️ {item} Added To Wishlist!")
            found = True

    if not found:
        print("❌ Product Not Found!")


def view_wishlist():

    if not wishlist:
        print("💔 Wishlist Is Empty!")
    else:
        print("\n❤️ YOUR WISHLIST")
        for item in wishlist:
            print("-", item)

def apply_coupon(total):

    coupon = input("Enter Coupon Code: ").upper()

    if coupon == "SAVE10":
        print("🎉 10% Discount Applied!")
        total *= 0.90

    elif coupon == "SAVE20":
        print("🎉 20% Discount Applied!")
        total *= 0.80

    else:
        print("❌ Invalid Coupon!")

    return total
def payment_method():

    print("\n========== PAYMENT METHODS ==========")
    print("1. Cash On Delivery")
    print("2. UPI")
    print("3. Credit/Debit Card")

    choice = input("Select Payment Method: ")

    if choice == "1":
        print("✅ Cash On Delivery Selected")

    elif choice == "2":
        upi = input("Enter UPI ID: ")
        print(f"✅ Payment Successful Through {upi}")

    elif choice == "3":
        card = input("Enter Last 4 Digits Of Card: ")
        print(f"✅ Payment Successful Using Card XXXX{card}")

    else:
        print("❌ Invalid Payment Method!")
def generate_bill():

    if not cart:
        print("🛒 Cart Is Empty!")
        return

    print("\n========== FINAL BILL ==========")

    order_id = random.randint(1000, 9999)

    print("Order ID :", order_id)
    print("Date :", datetime.datetime.now())

    total = 0

    for item, details in cart.items():

        subtotal = details["price"] * details["quantity"]
        total += subtotal

        print(
            f"{item} - ₹{details['price']} x "
            f"{details['quantity']} = ₹{subtotal}"
        )

    print("--------------------------------")
    print(f"Original Total : ₹{total}")

    # Coupon
    final_amount = apply_coupon(total)

    # GST
    gst = final_amount * 0.18
    final_amount += gst

    print(f"GST (18%)      : ₹{gst:.2f}")
    print(f"Final Amount   : ₹{final_amount:.2f}")

    payment_method()

    print("================================")
    print("🎉 ORDER PLACED SUCCESSFULLY!")

# Main Program
while True:

    print("\n========== ONLINE SHOPPING SYSTEM ==========")

    print("1. View Products")
    print("2. Search Product")
    print("3. Add To Cart")
    print("4. Remove From Cart")
    print("5. Update Quantity")
    print("6. View Cart")
    print("7. Add Wishlist")
    print("8. View Wishlist")
    print("9. Generate Bill")
    print("10. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        view_products()

    elif choice == "2":
        search_product()

    elif choice == "3":
        add_to_cart()

    elif choice == "4":
        remove_from_cart()

    elif choice == "5":
        update_quantity()

    elif choice == "6":
        view_cart()

    elif choice == "7":
        add_wishlist()

    elif choice == "8":
        view_wishlist()

    elif choice == "9":
        generate_bill()

    elif choice == "10":
        print("\n🙏 Thank You For Shopping!")
        break

    else:
        print("❌ Invalid Choice! Try Again.")