ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

lst = list(ft_tuple)
lst[1] = "Brazil"

ft_list[1] = "World"
ft_tuple = tuple(lst)
ft_set.remove("tutu!")
ft_set.add("Sao Paulo")
ft_dict["Hello"] = "42 SP"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
