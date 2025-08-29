# sample_data: nested regions -> stores -> customers -> orders -> items
from datetime import datetime

def nested_analytics(sample_data):
    nested_report = {"Regions": []}
    regions = sample_data["regions"]
    for region in regions:
        reg_name = region["name"]
        reg_dict = {"name": reg_name, "region_analytics": [], "stores": []}
        reg_analytics = {"Region_Analytics": []}
        stores_analytics = {"Stores": []}
        reg_report = {}
        store_report = {}
        stores = region["stores"]
        revenue_dict = {}
        for store in stores:
            cat_dict = {}
            category_list = []
            store_name = store["name"]
            store_dict = {"name": store_name, "Store_Analytics": {}, "customers": []}
            store_analytics = {}
            store_revenue = 0
            store_customers = store["customers"]
            cus_dict = {}
            customers_list = []
            cus_amount =len(store_customers)
            for customer in store_customers:
                customers_analytics = {}
                customer_analytics = {}
                customers_analytics["Customer Analytics"] = customer_analytics
                customer_point = customer["loyalty_points"]
                customer_analytics["Loyalty Points"] = customer_point
                customer_dict = {}
                cus_grade = 0
                total_spent = 0
                cus_id = customer["id"]
                customers_analytics["ID"] = cus_id
                cus_name = customer["name"]
                customers_analytics["Name"] = cus_name
                cus_orders = customer["orders"]
                customer_orders = len(cus_orders)
                customer_analytics["Orders Count"] = customer_orders
                cus_grade = 0
                total_spent = 0
                for order in cus_orders:
                    cus_items = order["items"]
                    for item in cus_items:
                        category_list.append(item["category"])
                        cus_grade += item["amount"]
                        total_spent += item["amount"]
                        store_revenue += item["amount"]
                if customer_orders > 0:
                    customer_average = round(total_spent/customer_orders)
                else:
                    customer_average = 0
                customer_analytics["Average Order Count"] = customer_average
                customer_analytics["Total_Spent"] = total_spent
            cus_dict[cus_name] = cus_grade
            customers_list.append(customers_analytics)
            store_dict["customers"] = customers_list
            if cus_amount > 0:
                average_cus = round(store_revenue / cus_amount)
            else:
                average_cus = 0
            if cus_dict:
                top_details = max(cus_dict.items(), key=lambda x: x[1])
                top_cus = f"{top_details[0]} with {top_details[1]} purchase"
                store_analytics["Top_Customer"] = top_cus
            for category in category_list:
                if category in cat_dict:
                    cat_dict[category] += 1
                else:
                    cat_dict[category] = 1
            if cat_dict:
                max_cat = max(cat_dict.items(), key=lambda x: x[1])
                pop_cat = f"{max_cat[0]} bought {max_cat[1]} times"
                store_analytics["Most_Popular_Catgory"] = pop_cat
            else:
                store_analytics["Most_Popular_Category"] = "No Orders"
                store_analytics["Customer_Count"] = cus_amount
                store_analytics["Average_Revenue_Per_Customer"] = average_cus
                store_analytics["Total_Revenue"] = store_revenue
            store_dict["Store_Analytics"] = store_analytics
            revenue_dict[store_name] = store_revenue
        reg_dict["stores"].append(store_dict)
        if revenue_dict:
            top_details =max(revenue_dict.items(), key=lambda x: x[1])
            top_store = top_details[0]
            top_revenue = top_details[1]
        
        reg_report["Top_Store"] = top_store
        ori_store = None
        loyalty_points = 0
        no = 0
        for store in stores:
            if store["name"] == top_store:
                customers = store["customers"]
                no = len(customers)
                for customer in customers:
                    loyalty_points += customer["loyalty_points"]
                    if no > 0:
                        average_points = round(loyalty_points / no)
                    else:
                        average_points = 0
                reg_report["Average_Loyalty_Points"] = average_points
            reg_dict["region_analytics"] = reg_report
        nested_report["Regions"].append(reg_dict)
    return nested_report  
def store_analytics(sample_data):
    store_analytics = []

    for region in sample_data["regions"]:
        stores = region["stores"]

        for store in stores:
            store_name = store["name"]
            store_details = {"Store_name": store_name}

            customers = store["customers"]
            store_details["Customers_Count"] = len(customers)

            category_dict = {}
            cus_dict = {}
            total_amount = 0
            total_items = 0

            for customer in customers:
                cus_name = customer["name"]
                cus_amount = 0
                for order in customer["orders"]:
                    for item in order["items"]:
                        # Track category count
                        category_dict[item["category"]] = category_dict.get(item["category"], 0) + 1
                        # Track revenue
                        cus_amount += item["amount"]
                        total_amount += item["amount"]
                        total_items += 1
                cus_dict[cus_name] = cus_amount

            # Determine popular category
            if category_dict:
                popular_cat = max(category_dict.items(), key=lambda x: x[1])
                store_details["Popular_Category"] = f"{popular_cat[0]} Purchased {popular_cat[1]}"
            else:
                store_details["Popular_Category"] = "No orders"

            # Determine top customer
            if cus_dict:
                top_customer = max(cus_dict.items(), key=lambda x: x[1])
                store_details["Top_Customer"] = f"{top_customer[0]} Amount_spent: {top_customer[1]}"
            else:
                store_details["Top_Customer"] = "No customers"

            # Compute average revenue
            store_details["Average_Revenue"] = total_amount / total_items if total_items > 0 else 0

            store_analytics.append(store_details)

    return store_analytics         
def individual_report(sample_data):
    customers_list = [ ]
    for data, regions in sample_data.items():
        for region in regions:
            region_name = region["name"]
            stores = region["stores"]
            for store in stores:
                store_name = store["name"]
                customers = store["customers"]
                for customer in customers:
                    name = customer["name"]
                    id = customer["id"]
                    customer_list = { "customer_name": name, "customer_id": id}
                    orders = customer["orders"]
                    new_list = []
                    No_orders = len(orders)
                    customer_list["Number_of_orders"] = No_orders
                    for order in orders:
                        items = order["items"]
                        amount = 0
                        category_list = [ ]
                        for item in items:
                            amount += item["amount"]
                            customer_list["Total_spent"] = amount
                        num = len(items)
                        AOV = round(amount/num)
                        customer_list["Average_order_value"] = AOV
                        category = item["category"]
                        category_list.append(category)
                        cat_dict = {}
                        for word in category_list:
                            if word in cat_dict:
                                cat_dict[word] += 1
                            else:
                                cat_dict[word] = 1
                        favorite = sorted(cat_dict, key = lambda x: cat_dict[x], reverse=True)
                        favourite = (f"Favorite: {favorite[0]}, Times purchased: {cat_dict[favorite[0]]}")
                        customer_list["Favourite_product_category"] = favourite
                        
                        
                        order_date = order["date"]
                        date_list = list(order_date)
                        for a in date_list:
                            if a == "-":
                                date_list.remove(a)
                                dates = "".join(str(date) for date in date_list)
                        new_list.append(dates)
                        latest_date = max(int(d) for d in new_list)
                        my_date = f"{str(latest_date)[:4]} - {str(latest_date)[4:6]} - {str(latest_date)[6:]}"
                        new_date = datetime.now()
                        today = datetime.strptime(my_date, "%Y - %m - %d")
                        if (today - new_date).days >= 60:
                            customer_list["At_Risk"] = True
                        else:
                            customer_list["At_Risk"] = False
                customers_list.append(customer_list)
        return customers_list
                    
                        
def flatten_list(sample_data):
    customers_list = [ ]
    for data, regions in sample_data.items():
        for region in regions:
            region_name = region["name"]
            stores = region["stores"]
            for store in stores:
                store_name = store["name"]
                customers = store["customers"]
                for customer in customers:
                    name = customer["name"]
                    id = customer["id"]
                    loyalty_points = customer["loyalty_points"]
                    customer_list = {"Region": region_name, "store": store_name, "customer_name": name, "customer_id": id, "Loyalty_points": loyalty_points}
                    orders = customer["orders"]
                    new_list = []
                    for order in orders:
                        items = order["items"]
                        amount = 0
                        category_list = [ ]
                        for item in items:
                            amount += item["amount"]
                            customer_list["Total_spent"] = amount
                        num = len(items)
                        AOV = round(amount/num)
                        customer_list["Average_order_value"] = AOV
                        category = item["category"]
                        category_list.append(category)
                        cat_dict = {}
                        for word in category_list:
                            if word in cat_dict:
                                cat_dict[word] += 1
                            else:
                                cat_dict[word] = 1
                        favorite = sorted(cat_dict, key = lambda x: cat_dict[x], reverse=True)
                        favourite = (f"Favorite: {favorite[0]}, Times purchased: {cat_dict[favorite[0]]}")
                        customer_list["Favourite_product_category"] = favourite
                        
                        
                        order_date = order["date"]
                        date_list = list(order_date)
                        for a in date_list:
                            if a == "-":
                                date_list.remove(a)
                                dates = "".join(str(date) for date in date_list)
                        new_list.append(dates)
                        latest_date = max(int(d) for d in new_list)
                        my_date = f"{str(latest_date)[:4]} - {str(latest_date)[4:6]} - {str(latest_date)[6:]}"    
                customers_list.append(customer_list)
        return customers_list

            
                    
                        
                        
                               










sample_data = {
    "regions": [
        {
            "name": "North",
            "stores": [
                {
                    "name": "Store A",
                    "customers": [
                        {
                            "id": "C001",
                            "name": "John Doe",
                            "loyalty_points": 120,
                            "orders": [
                                {"date": "2025-06-01", "items": [
                                    {"product": "Laptop", "category": "Electronics", "amount": 1200.0},
                                    {"product": "Mouse", "category": "Electronics", "amount": 20.0}
                                ]},
                                {"date": "2025-07-15", "items": [
                                    {"product": "Chair", "category": "Furniture", "amount": 150.0}
                                ]}
                            ]
                        },
                        {
                            "id": "C002",
                            "name": "Alice Smith",
                            "loyalty_points": 80,
                            "orders": [
                                {"date": "2025-05-10", "items": [
                                    {"product": "Desk", "category": "Furniture", "amount": 300.0}
                                ]},
                                {"date": "2025-08-01", "items": [
                                    {"product": "Lamp", "category": "Home", "amount": 45.0},
                                    {"product": "Notebook", "category": "Stationery", "amount": 5.0}
                                ]}
                            ]
                        },
                        {
                            "id": "C003",
                            "name": "Empty Orders",
                            "loyalty_points": 5,
                            "orders": []  # customer with no orders (edge case)
                        }
                    ]
                },
                {
                    "name": "Store B",
                    "customers": [
                        {
                            # customer with tie in category counts but different revenue -> tie-break by revenue
                            "id": "C004",
                            "name": "Tie Customer",
                            "loyalty_points": 40,
                            "orders": [
                                {"date": "2025-06-05", "items": [
                                    {"product": "Pen", "category": "Stationery", "amount": 2.0},
                                    {"product": "Pencil", "category": "Stationery", "amount": 1.0}
                                ]},
                                {"date": "2025-06-25", "items": [
                                    {"product": "Mug", "category": "Home", "amount": 30.0}
                                ]},
                                {"date": "2025-07-10", "items": [
                                    {"product": "Notebook", "category": "Stationery", "amount": 8.0}
                                ]},
                                {"date": "2025-07-20", "items": [
                                    {"product": "Cushion", "category": "Home", "amount": 31.0}
                                ]}
                            ]
                        }
                    ]
                },
                {
                    "name": "Store Empty",   # empty store (edge case)
                    "customers": []
                }
            ]
        },
        {
            "name": "South",
            "stores": [
                {
                    "name": "Store C",
                    "customers": [
                        {
                            "id": "C005",
                            "name": "Mark Johnson",
                            "loyalty_points": 15,
                            "orders": [
                                {"date": "2025-02-01", "items": [
                                    {"product": "Table", "category": "Furniture", "amount": 250.0}
                                ]}
                            ]
                        },
                        {
                            "id": "C006",
                            "name": "Loyal Shopper",
                            "loyalty_points": 300,
                            "orders": [
                                {"date": "2025-07-01", "items": [
                                    {"product": "Phone", "category": "Electronics", "amount": 800.0}
                                ]},
                                {"date": "2025-07-05", "items": [
                                    {"product": "Headphones", "category": "Electronics", "amount": 120.0}
                                ]},
                                {"date": "2025-08-05", "items": [
                                    {"product": "Charger", "category": "Electronics", "amount": 25.0}
                                ]}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "East",
            "stores": [
                {
                    "name": "Store D",
                    "customers": [
                        {
                            "id": "C007",
                            "name": "Old Timer",
                            "loyalty_points": 10,
                            # last purchase very old (edge case for at_risk)
                            "orders": [
                                {"date": "2024-01-01", "items": [
                                    {"product": "Radio", "category": "Electronics", "amount": 45.0}
                                ]}
                            ]
                        },
                        {
                            "id": "C008",
                            "name": "Multi Category",
                            "loyalty_points": 60,
                            "orders": [
                                {"date": "2025-08-10", "items": [
                                    {"product": "Novel", "category": "Books", "amount": 12.0},
                                    {"product": "Pen", "category": "Stationery", "amount": 3.0}
                                ]},
                                {"date": "2025-09-01", "items": [
                                    {"product": "Board Game", "category": "Toys", "amount": 35.0}
                                ]}
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}

data_list = flatten_list(sample_data)
print(data_list)
new_data = individual_report(sample_data)
print(new_data)
analytics = store_analytics(sample_data)
print(analytics)
final_result = nested_analytics(sample_data)
print(final_result)