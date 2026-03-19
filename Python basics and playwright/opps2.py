class Mobile:

    def set_owner(self, name):
        self.owner = name

    def show_owner(self):
        print("Phone owner is", self.owner)


phone1 = Mobile()
phone2 = Mobile()

phone1.set_owner("Arpan")
phone2.set_owner("Rahul")

phone1.show_owner()
phone2.show_owner()