a = [1, 2, 3]
b = a
a.append(4)       # 最常见的原地修改操作
print(f"{b =}\n"
      f"{a =}\n"
      f"{id(a) = }, {id(b) = }, {id(a) == id(b)}\n"
      f"{a is b = }")

c = {"a": 1}
d = c
c["b"] = 2
c.update({"c": 3})
c.setdefault("d", 4)
del c["a"]
print(f"\n{d =}\n"
      f"{c =}\n"
      f"{id(c) = }, {id(d) = }, {id(c) == id(d)}\n"
      f"{c is d = }")
