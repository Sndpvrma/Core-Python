class Bird:
    def fly(self):
        print("Most Birds can fly")

class sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")

class ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly")

obj_spr=sparrow()
obj_os=ostrich()
obj_brd=Bird()

obj_spr.fly()
obj_os.fly()
obj_brd.fly()