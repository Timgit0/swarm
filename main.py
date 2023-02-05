from tkinter import *  # library tkinter
from random import randint as rt  # random
from math import *  # math

root = Tk()
root.geometry('1200x700')
c = Canvas(root, width=1100, height=600, bg='blue')
c.place(x=50, y=50)  # some tkinter things


class Main:
    def __init__(self):
        self.pause = False
        self.starting_number_of_bugs = 5
        self.iter = 2
        self.file = 'results' + str(self.iter) + '.txt'


The = Main()
bugs, resources, queens = [], [], []  # creating the massive for units


class Resource:
    def __init__(self, x, y, r, resource):
        self.x = x
        self.y = y
        self.r = r
        self.resource = resource
        resources.append(self)

    def my_anime(self):
        a, b = rt(-2, 2) / 5, rt(-2, 2) / 5
        self.x += a
        self.y += b
        c.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill="dark green")
        self.r = self.resource / 15 + 10
        if self.resource <= 0:
            resources.remove(self)


class Queen:
    def __init__(self, x, y, r, resource):
        self.x = x
        self.y = y
        self.r = r
        self.resource = resource
        queens.append(self)

    def my_anime(self):
        a, b = rt(-2, 2) / 5, rt(-2, 2) / 5
        self.x += a
        self.y += b
        c.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill="yellow")
        self.resource -= 1
        self.r = self.resource / 15 + 10
        if self.resource < 0:
            queens.remove(self)


class Bug:
    def __init__(self, x, y, dx, dy, r, to_queen, to_resource, max_speed, max_shout_radius, time, bug_type):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.time = time
        self.to_resource = to_resource
        self.to_queen = to_queen
        self.max_shout_radius = max_shout_radius
        self.target = "resources"
        self.max_speed = max_speed
        self.type = "bug"
        self.color1 = "yellow"
        self.color2 = "dark green"
        if bug_type == 15:
            self.type = "scout"

            self.color1 = "gray"
            self.color2 = "gray"
        elif bug_type == 14:
            self.type = "long liver"
            self.time *= 2
            self.max_speed *= 3 / 4
            self.max_shout_radius *= 3 / 4

            self.color1 = "pink"
            self.color2 = "purple"
            self.r *= 1.5
        elif bug_type == 13:
            self.type = "scout"
            self.max_speed *= 1 / 10
            self.max_shout_radius *= 3 / 2

            self.color1 = "red"
            self.color2 = "red"
            self.r *= 1.5
        elif bug_type == 12:
            self.type = "runner"
            self.max_speed *= 2
            self.time *= 3 / 4

            self.color1 = "orange"
            self.color2 = "dark orange"

        '''
        elif bug_type == 11:
            self.type = "smart"

            self.color1 = "white"
            self.color2 = "black"
            self.r *= 5 '''
        bugs.append(self)

    def become_queen(self):
        bugs.remove(self)
        Queen(self.x, self.y, 15, self.time / 10)

    def shout(self):
        for bug in bugs:
            distance = ((self.x - bug.x) ** 2 + (self.y - bug.y) ** 2) ** 0.5
            if distance > self.max_shout_radius or distance == 0:
                continue
            if bug.to_queen > self.to_queen + self.max_shout_radius:
                bug.to_queen = self.to_queen + self.max_shout_radius
                if bug.target == "queen" and bug.type != "scout" and bug.type != "smart":
                    bug.dx = (self.x - bug.x) * bug.max_speed / distance
                    bug.dy = (self.y - bug.y) * bug.max_speed / distance
                    c.create_line(self.x, self.y, bug.x, bug.y, fill="black")
                else:
                    c.create_line(self.x, self.y, bug.x, bug.y, fill="red")
            if bug.to_resource > self.to_resource + self.max_shout_radius:
                bug.to_resource = self.to_resource + self.max_shout_radius
                if bug.target == "resources" and bug.type != "scout" and bug.type != "smart":
                    bug.dx = (self.x - bug.x) * bug.max_speed / distance
                    bug.dy = (self.y - bug.y) * bug.max_speed / distance
                    c.create_line(self.x, self.y, bug.x, bug.y, fill="black")
                else:
                    c.create_line(self.x, self.y, bug.x, bug.y, fill="red")

    def check_resources(self):
        for resource in resources:
            distance = ((self.x - resource.x) ** 2 + (self.y - resource.y) ** 2) ** 0.5
            if distance < self.r + resource.r:
                self.to_resource = 0
                if self.target == "resources":
                    self.target = "queen"
                    resource.resource -= 1
                    self.dx, self.dy = -self.dx, - self.dy

    def check_queen(self):
        for queen in queens:
            distance = ((self.x - queen.x) ** 2 + (self.y - queen.y) ** 2) ** 0.5
            if distance < self.r + queen.r:
                self.to_queen = 0
                if self.target == "queen":
                    self.target = "resources"
                    queen.resource += 1
                    self.dx, self.dy = -self.dx, - self.dy
                    if not rt(0, 9):
                        Bug(rt(0, 1100), rt(0, 600), rt(-5, 5), rt(-5, 5), 2, inf, inf, rt(5, 15), 50, rt(300, 500),
                            rt(0, 15))

    def my_anime(self):
        able_to_queen = True
        for queen in queens:
            if ((self.x - queen.x) ** 2 + (self.y - queen.y) ** 2) ** 0.5 < 400:
                able_to_queen = False
        if able_to_queen:
            self.become_queen()

        self.check_resources()
        self.check_queen()
        self.shout()

        self.to_queen += self.max_speed
        self.to_resource += self.max_speed

        a, b = rt(-2, 2) / 5, rt(-2, 2) / 5
        self.x += self.dx + a
        self.y += self.dy + b
        if self.target == "queen":
            c.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color2)
        else:
            c.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color1)

        if self.x < 0 or self.x > 1100:
            self.dx *= -1
        if self.y < 0 or self.y > 600:
            self.dy *= -1
        self.time -= 1
        if self.time <= 0 and self in bugs:
            bugs.remove(self)


for _ in range(int(The.starting_number_of_bugs)):
    Bug(rt(0, 1100), rt(0, 600), rt(-5, 5), rt(-5, 5),
        2, inf, inf, rt(5, 15), 50, rt(3000, 5000), rt(0, 15))


def tick():
    if not The.pause:
        c.delete("all")
        for j in bugs + resources + queens:
            j.my_anime()
        if not rt(0, 9) and len(resources) < 10:
            Resource(rt(0, 1100), rt(0, 600), 10, rt(100, 500))
        if len(bugs) + len(queens) == 0:
            with open(The.file, "a") as writer:
                writer.write(str(int(The.starting_number_of_bugs)) + " failed" + "\n")
            The.starting_number_of_bugs += 1
            for _ in range(int(The.starting_number_of_bugs)):
                Bug(rt(0, 1100), rt(0, 600), rt(-5, 5), rt(-5, 5),
                    2, inf, inf, rt(5, 15), 50, rt(3000, 5000), rt(0, 15))
        if len(bugs) + len(queens) >= The.iter * The.starting_number_of_bugs + 1:
            while bugs:
                bugs.pop()
            while queens:
                queens.pop()
            while resources:
                resources.pop()
            with open(The.file, "a") as writer:
                writer.write(str(int(The.starting_number_of_bugs)) + " success" + "\n")
            The.starting_number_of_bugs += 1
            for _ in range(int(The.starting_number_of_bugs)):
                Bug(rt(0, 1100), rt(0, 600), rt(-5, 5), rt(-5, 5),
                    2, inf, inf, rt(5, 15), 50, rt(3000, 5000), rt(0, 15))
        L.configure(text=('The number of alive bugs and queens: ' + str(len(bugs) + len(queens)) +
                          '   The sub iteration: ' + str(The.starting_number_of_bugs) +
                          '   The greate iteration: ' + str(The.iter)))
        if The.starting_number_of_bugs >= 150:
            The.starting_number_of_bugs = 5
            The.iter += 1
            The.file = 'results' + str(The.iter) + '.txt'
            if The.iter >= 10:
                The.iter = 2
    root.after(1, tick)


def key(event):
    if event.char == "q" or event.char == "Q":
        root.destroy()
    if event.keycode == 32:
        The.pause = not The.pause


L = Label(text=('The number of alive bugs and queens: ' + str(len(bugs) + len(queens)) +
                '   The sub iteration: ' + str(The.starting_number_of_bugs) +
                '   The greate iteration: ' + str(The.iter)))
L.pack()
root.configure(background='green')
root.bind('<Key>', key)

tick()
root.mainloop()
