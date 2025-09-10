print("Welcome to the manga corner!")
genre = input("Please select genre(shonin-shojo-seinen-josei): ").lower()

if genre == ("shonin"):
	print("You have chosen the genre : Shonin")
	year = input("Please choose a year (2000-2010): ")
	if year == ("2000"):
		print("You have chosen year: 2000")
		length = input("Please choose if Long or Short: ").lower()
		if length == ("long"):
			print("Here is a list of Long Shonin Manga in the year 2000")
			print("1. Naruto\n2. Bleach\n3. One Piece")
		if length == ("short"):
			print("Here is a list of Long Shonin Manga in the year 2000")
			print("1. Death Note\n2. Hikaru no go\n3.Hana yori Dango ")
	elif year == ("2010"):
		print("You have chosen year: 2010")
		length = input("Please choose if Long or Short: ").lower()
		if length == ("long"):
			print("Here is a list of Long Shonin Manga in the year 2010")
			print("1.Shingeki no Kyojin\n2.The Promised Neverland\n3.Boku no Hero Academia")
		if length == ("short"):
			print("Here is a list of Long Shonin Manga in the year 2010")
			print("1. Tokyo Ghoul\n2. Orange\n3. The Promised Neverland\n4. Your Name\n5. Kimi ni Todoke")


elif genre == ("shojo"):
	print("You have chosen the genre : Shojo")
	year = input("Please choose a year (2000-2010): ")
	if year == ("2000"):
		print("You have chosen year: 2000")
		length = input("Please choose if Long or Short: ")
		if length == ("long"):
			print("Here is a list of Long Shojo Manga in the year 2000")
			print("1. Skip Beat!\n2. Yona of the Dawn\n3. Lovely★Complex\n4. Hana Yori Dango\n5. Natsume's Book of Friends")
		if length == ("short"):
			print("Here is a list of Long Shojo Manga in the year 2000")
			print("1. Orange\n2. Ouran High School Host Club\n3. Paradise Kiss\n4. Watashi no Ookami-kun\n5. Love So Life")

	elif year == ("2010"):
		print("You have chosen year: 2010")
		length = input("Please choose if Long or Short: ").lower()
		if length == ("long"):
			print("Here is a list of Long Shojo Manga in the year 2010")
			print("1. Yona of the Dawn (Akatsuki no Yona)\n2. Snow White with the Red Hair (Akagami no Shirayuki-hime)\n3. Kamisama Kiss (Kamisama Hajimemashita)\n4. Ao Haru Ride\n5. Strobe Edge")
		if length == ("short"):
			print("Here is a list of Long Shojo Manga in the year 2010")
			print("1. Love So Life\n2. Say I Love You\n3. Yamada-kun and the Seven Witches\n4. Honey So Sweet\n5. Kimi ni Todoke")

elif genre == ("seinen"):
	print("You have chosen the genre : Seinen")
	year = input("Please choose a year (2000-2010): ")
	if year == ("2000"):
		print("You have chosen year: 2000")
		length = input("Please choose if Long or Short: ").lower()
		if length == ("long"):
			print("Here is a list of Long Seinen Manga in the year 2000")
			print("1. Berserk\n2. Monster\n3. 20th Century Boys\n4. Vagabond\n5. Hellsing\n6. Fullmetal Alchemist\n7. Gantz\n8. Naruto\n9. Bleach\n10. One Piece")
		if length == ("short"):
			print("Here is a list of Long Seinen Manga in the year 2000")
			print("1. Death Note\n2. Great Teacher Onizuka\n3. Bakuman\n4. Black Lagoon\n5. Goodnight Punpun\n6. Planetes\n7. Azumanga Daioh\n8. Parasyte\n9. A Silent Voice\n10. Blue Flag")
	elif year == ("2010"):
		print("You have chosen year: 2010")
		length = input("Please choose if Long or Short: ")
		if length == ("long"):
			print("Here is a list of Long Seinen Manga in the year 2010")
			print("1. Attack on Titan\n2. Tokyo Ghoul\n3. One Punch Man\n4. My Hero Academia\n5. The Promised Neverland\n6. Demon Slayer\n7. Golden Kamuy\n8. Dr. Stone\n9. Hunter x Hunter\n10. JoJo's Bizarre Adventure: Steel Ball Run")
		if length == ("short"):
			print("Here is a list of Long Seinen Manga in the year 2010")
			print("1. Death Parade\n2. March Comes in Like a Lion\n3. Erased\n4. Your Lie in April\n5. Vinland Saga\n6. The Ancient Magus' Bride\n7. Miss Kobayashi's Dragon Maid\n8. The Girl from the Other Side\n9. Ajin: Demi-Human\n10. Teasing Master Takagi-san")
elif genre == ("josei"):
	print("You have chosen the genre : Josei")
	year = input("Please choose a year (2000-2010): ")
	if year == ("2000"):
		print("You have chosen year: 2000")
		length = input("Please choose if Long or Short: ").lower()
		if length == ("long"):
			print("Here is a list of Long Josei Manga in the year 2000")
			print("1. Nodame Cantabile\n2. Paradise Kiss\n3. Honey and Clover\n4. Lovely Complex\n5. Kimi wa Girlfriend\n6. Sand Chronicles\n7. Nodame Cantabile\n8. Boku wa Imouto ni Koi wo Suru\n9. Bokura no Tsuki\n10. Otomen")
		if length == ("short"):
			print("Here is a list of Long Josei Manga in the year 2000")
			print("1. Love So Life\n2. Say I Love You\n3. Yamada-kun and the Seven Witches\n4. Honey So Sweet\n5. Kimi ni Todoke\n6. Special A\n7. Anata to Koi wo Shite Mita\n8. Shiro to Kuro\n9. Tonari no Kaibutsu-kun\n10. Orange")
	elif year == ("2010"):
		print("You have chosen year: 2010")
		length = input("Please choose if Long or Short: ")
		if length == ("long"):
			print("Here is a list of Long Josei Manga in the year 2010")
			print("1. Ooku: The Inner Chambers\n2. Kuragehime (Princess Jellyfish)\n3. An Incurable Case of Love\n4. Nagi no Asukara\n5. Boku wa Hana\n6. 3D Kanojo: Real Girl\n7. Kimi wa Girlfriend\n8. Kimi no Koto ga Daidaidaidaidai Suki na 100-nin no Kanojo\n9. ReLIFE\n10. Watashi no Kawaii Daisuki na Hito")
		if length == ("short"):
			print("Here is a list of Long Josei Manga in the year 2010")
			print("1. Ouran High School Host Club\n2. Say I Love You\n3. Strobe Edge\n4. Orange\n5. Tonari no Kaibutsu-kun\n6. Hapi Mari\n7. My Senpai is Annoying\n8. Boku no Hero Academia (Josei edition)\n9. A Sign of Affection\n10. Kimi to Koi no Tochuu")
else:
    print("Invalid genre selected. Please choose from 'shonin', 'shojo', 'seinen', or 'josei'.")