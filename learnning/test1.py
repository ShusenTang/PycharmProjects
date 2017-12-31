# class Person:
#     """represents a person"""
#     population = 0
#
#     def __init__(self, name):
#         self.name = name
#         print '(initialing %s......)' % self.name
#         Person.population += 1
#
#     def __del__(self):
#         print '%s says byebye~' % self.name
#         Person.population -= 1
#
#         if Person.population == 0:
#             print 'I am the last one.'
#         else:
#             print 'There still %d people left.' % Person.population
#
#     def sayHi(self):
#         print 'Hello,my name is %s.' % self.name
#
#     def howMany(self):
#         if Person.population == 1:
#             print 'I am the only person here.'
#         else:
#             print 'We have %d persons here.' % Person.population
#
# tangshusen = Person('tangshusen')
# tangshusen.sayHi()
# tangshusen.howMany()
#
# wangxue = Person('wangxue')
# wangxue.sayHi()
# wangxue.howMany()
#
# del wangxue
#
# tangshusen.sayHi()
# tangshusen.howMany()
#
# del tangshusen
#
# print Person.population

class SchoolMember:
    """represents school member"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(initialized school member %s .)' % self.name
    def tell(self):
        print 'name: %s age: %s' % (self.name, self.age),

class Teacher(SchoolMember):
    """represents teacher"""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(initialized teaacher %s .)' % self.name

    def tell(self):
        SchoolMember.tell(self)
        print "salary: %d" % self.salary


class Student(SchoolMember):
    """represents student"""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(initialized student %s .)' % self.name

    def tell(self):
        SchoolMember.tell(self)
        print "marks: %d" % self.marks


t = Teacher('Mrs Tang', 35, 10000)
s = Student('Tangshusen', 20, 14021051)

print

members = [t, s]
for member in members:
    member.tell()