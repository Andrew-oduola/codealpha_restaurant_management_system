from locust import HttpUser, TaskSet, task, between
import json

class MenuTasks(TaskSet):
    def on_start(self):
        # Authenticate user
        self.login()
        
 

    def login(self):
        response = self.client.post("auth/jwt/create/", json={
            "email": "ayobamioduola13@gmail.com",  
            "password": "secret"   
        })
        print(response)
        if response.status_code == 200:
            self.token = response.json()["access"]
            print(self.token)
            
            self.client.headers.update({"Authorization": f"JWT {self.token}"})
            return self.token
        else:
            print("Failed to authenticate")

    @task(2)
    def list_menu_items(self):
        """Test the endpoint to list all menu items."""
        self.client.get("api/menu/items/", 
                        auth=None,
                        headers={"Authorization": "JWT " + self.login()})

    @task(1)
    def create_menu_item(self):
        """Test the endpoint to create a new menu item."""
        menu_item_data = {
            "name": "Test Menu Item",
            "description": "A test menu item description",
            "price": 25.50,
            "category": 1,  # Replace with a valid category ID
            "available": True
        }
        self.client.post("api/menu/items/", 
                         json=menu_item_data,
                         auth=None,
                         headers={"Authorization": "JWT " + self.login()})

    @task(2)
    def search_menu_items(self):
        """Test the search functionality for menu items."""
        self.client.get("api/menu/items/?search=Test",
                        auth=None,
                        headers={"Authorization": "JWT " + self.login()})

    @task(1)
    def filter_menu_items(self):
        """Test filtering menu items by category and availability."""
        self.client.get("api/menu/items/?category=1&available=true", 
                        auth=None,
                        headers={"Authorization": "JWT " + self.login()})

    @task(1)
    def list_menu_categories(self):
        """Test the endpoint to list all menu categories."""
        self.client.get("api/menu/categories/",
                        auth=None,
                        headers={"Authorization": "JWT " + self.login()})

    @task(1)
    def create_menu_category(self):
        """Test the endpoint to create a new menu category."""
        menu_category_data = {
            "name": "Test Category",
            "description": "A test category description",
            "image": None  # Optional field
        }
        self.client.post("api/menu/categories/", 
                         json=menu_category_data,
                         auth=None,
                         headers={"Authorization": "JWT " + self.login()})

class MenuUser(HttpUser):
    tasks = [MenuTasks]
    wait_time = between(1, 5)