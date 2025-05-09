count = 99
song = " bottles of beer on the the wall!"
song1 = " Bottles of beer!"
song2 = " Take one down, pass it around!"
song3 = " bottle of beer on the the wall!"
song4 = " Bottles of beer!"
song5 = "No more bottles of beer on the wall, no more bottles of beer!"

while count > 1:
    print(str(count) + song + song1 + song2)
    count = count - 1
    print(str(count) + song)
else:
	count = 1
	print(str(count) + song3 + song4 + song2)
	print(song5)
