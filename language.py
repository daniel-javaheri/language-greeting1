name = input("name: ")
name = name

langfunc = input("type a language (only english, spanish or french): ")

if langfunc == "english":
    print("hello " + name)
elif langfunc == "spanish":
    print("hola " + name)
else:
    print("bonjour " + name)