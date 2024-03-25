from kanren.facts import Relation, facts
from kanren.core import var, run, conde

parent = Relation()
facts(parent, ("Slamet", "Amin"),
 ("Slamet", "Anang"),
 ("Amin", "Badu"),
 ("Amin", "Budi"),
 ("Anang", "Didi"),
 ("Anang", "Dadi"))

cucu = Relation()
facts(cucu,
 ("Slamet", "Badu"),
 ("Slamet", "Budi"),
 ("Slamet", "Didi"),
 ("Slamet", "Dadi"))

x = var()
child = "Slamet"
ayah = run(0, x, cucu(child, x))
print("\nNama ayah " + child + ": ")
for item in ayah:
 print(item)
x = var()
child = "Amin"
ayah = run(0, x, parent(child, x))
print("\nAnak " + child + ": ")
for item in ayah:
 print(item)
x = var()
child = "Anang"
ayah = run(0, x, parent(child, x))
print("\nAnak " + child + ": ")
for item in ayah:
 print(item)
x = var()
child = "Anang"
ayah = run(0, x, parent(child, x))
print("\nPonakan Amin : ")
for item in ayah:
 print(item)
child = "Amin"
ayah = run(0, x, parent(child, x))
print("\nPonakan Anang : ")
for item in ayah:
 print(item)