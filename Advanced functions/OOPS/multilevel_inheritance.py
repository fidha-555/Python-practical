class Grandparent:
   def feature_grandparent(self):
      print("Grandparent Feature")
class Parent(Grandparent):
   def feature_parent(self):
      print("Parent Feature")
class Child(Parent):
   def feature_child(self):
      print("Child Feature")
c = Child()
c.feature_grandparent()
c.feature_parent()
c.feature_child()

