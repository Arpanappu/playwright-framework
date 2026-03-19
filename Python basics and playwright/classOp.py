class Car:

    def start(self):
        print("Car started")

my_car = Car()
my_car.start()


class LoginPage:

    def open_page(self):
        print("Opening login page")

    def login(self):
        print("Entering username")
        print("Entering password")
        print("Click login")


page = LoginPage()

page.open_page()
page.login()