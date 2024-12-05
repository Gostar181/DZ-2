class kotik:
    amount_of_kotik = 0

    def __init__(self, speed=30):
        self.speed = speed
        kotik.amount_of_kotik += 1
    def grow(self, speed=1):
        self.speed += speed

Baton = kotik()
Belyash = kotik(speed=80)
Kokos = kotik(speed=67)

Baton.grow(speed=15)
Kokos.grow(speed=35)

print(Baton.speed)
print(Belyash.speed)
print(Kokos.speed)
print(kotik.amount_of_kotik)
