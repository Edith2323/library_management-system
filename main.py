class CatalogingModule:
    def __init__(self):
        self.catalog = []

    def add_item(self, title, author, media_type, isbn, description):
        item = {
            "title": title,
            "author": author,
            "media_type": media_type,
            "isbn": isbn,
            "description": description
        }
        self.catalog.append(item)
        print("Item added to catalog.")

class CirculationModule:
    def __init__(self):
        self.checked_out_items = []

    def check_out_item(self, item):
        self.checked_out_items.append(item)
        print("Item checked out successfully.")

    def return_item(self, item):
        if item in self.checked_out_items:
            self.checked_out_items.remove(item)
            print("Item returned successfully.")
        else:
            print("Item not found in checked out items.")

class UserManagement:
    def issue_library_card(self, patron_name):
        print(f"Library card issued to {patron_name}.")

    def update_contact_info(self, patron_name, new_info):
        print(f"Contact information updated for {patron_name}: {new_info}.")

class SearchAndDiscovery:
    def search_catalog(self, keyword):
        # Code for searching catalog
        pass

    def apply_filters(self, filters):
        # Code for applying filters
        pass

class DigitalResourceIntegration:
    def borrow_digital_resource(self, resource):
        # Code for borrowing digital resource
        pass

class ReportingAndAnalytics:
    def generate_reports(self):
        # Code for generating reports
        pass

# Example usage:
catalog_module = CatalogingModule()
catalog_module.add_item("Python Programming", "Guido van Rossum", "Book", "9781449355739", "A comprehensive guide to Python programming.")

circulation_module = CirculationModule()
circulation_module.check_out_item("Python Programming")
circulation_module.return_item("Python Programming")

user_management = UserManagement()
user_management.issue_library_card("Michael Musa")
user_management.update_contact_info("Michael Musa", "New email: musembi@gmail.com")

search_discovery = SearchAndDiscovery()
search_discovery.search_catalog("Python")
search_discovery.apply_filters(["Book", "Non-fiction"])

digital_resource_integration = DigitalResourceIntegration()
digital_resource_integration.borrow_digital_resource("Introduction to Machine Learning")

reporting_analytics = ReportingAndAnalytics()
reporting_analytics.generate_reports()
