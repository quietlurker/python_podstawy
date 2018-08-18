print("String formatting: %s %s" %("black", "green"))
print("String formatting: {} {}" .format("black", "green"))

print("String formatting: {} {} {} {}" .format("black", "green", "yellow", 3))

#https://pyformat.info/
#indexes, starting with 0
print("String formatting: {0} {1} {2} {3}" .format("black", "green", "yellow", 3))

print("String formatting: {1} {2} {3} {0}" .format("black", "green", "yellow", 3))

#padding

#allign left to 10 
print("String formatting: {1:>10} {2} {3} {0}" .format("black", "green", "yellow", 3))

#pad right to 10
print("String formatting: {1:10} {2} {3} {0}" .format("black", "green", "yellow", 3))

#pad right with * if less than 10 -  :*<10
print("String formatting: {:*<10} {} {} {}" .format("black", "green", "yellow", 3))

#center (:^10)
print("String formatting: {:^10} {:*<10} {:*<10} {:*<10}" .format("black", "0123456789", "123456789", "01234567890"))

#truncate
print("String formatting: {:^10} {:*<10} {:*<10} {:.10}" .format("black", "0123456789", "123456789", "01234567890"))

#truncate and pad - all together now: {:*<10.5} - get 5 chars, pad to 10 with *
print("String formatting: {:^10} {:*<10} {:*<10.5} {:*<10.5}" .format("black", "0123456789", "123456789", "01234567890"))

#placeholders

stage1 = "Mistake Not My Current State Of Joshing Gentle Peevishness\n"
stage2 = "For The Awesome And Terrible Majesty Of The Towering Seas Of Ire\n"
stage3 = "That Are Themselves The Mere Milquetoast Shallows Fringing My Vast Oceans Of Wrath"

data = {"one": stage1, "two": stage2, "three": stage3}
print(data)
#**data - kwargs (http://book.pythontips.com/en/latest/args_and_kwargs.html) - keyword agruments
print("Mistake not:\n {one} {two} {three}" .format(**data))

