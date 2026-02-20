from observer import Observer


class MobileDisplay(Observer):
    def update(self, temp):
        print(f"Mobile temprature updated to {temp}")
