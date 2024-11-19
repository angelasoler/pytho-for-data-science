ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

l = list(ft_tuple)
l[1] = "Brazil"

ft_list[1] = "World"
ft_tuple = tuple(l)
ft_set.remove("tutu!")
ft_set.add("Sao Paulo")
ft_dict["Hello"] = "SP"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
