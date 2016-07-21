# coding=utf8

PRE_CONVERSION_MAP = (
	(" +", " "),("yy", "y"),("vv", "v"),("��", "�"),("y&", "y"),("�&", "�"),("�u", "u�"), ("wu", "uw"),(" ,", ","),
	(" \\|", "\\|"),("\\\\ ", ""),(" \\\\", ""),("\\\\", ""),("\n +", "\n"),(" +\n", "\n"),("\n\n\n\n\n", "\n\n"),
	("\n\n\n\n", "\n\n"),("\n\n\n", "\n\n")
)
CONVERSION_MAP = (
	# digits
	("0", "০"),("1", "১"),("2", "২"),("3", "৩"),("4", "৪"),("5", "৫"),("6", "৬"),("7", "৭"),("8", "৮"),("9", "৯"),
	
	# vowels/sorborno
	("Av", "আ"),("A", "অ"),("B", "ই"),("C", "ঈ"),("D", "উ"),("E", "ঊ"),("F", "ঋ"),("G", "এ"),("H", "ঐ"),("I", "ও"),("J", "ঔ"),
	
	# consonants / benjonborno
	("K", "ক"),("L", "খ"),("M", "গ"),("N", "ঘ"),("O", "ঙ"),("P", "চ"),("Q", "ছ"),("R", "জ"),("S", "ঝ"),("T", "ঞ"),("U", "ট"),
	("V", "ঠ"),("W", "ড"),("X", "ঢ"),("Y", "ণ"),("Z", "ত"),("_", "থ"),("`", "দ"),("a", "ধ"),("b", "ন"),("c", "প"),("d", "ফ"),
	("e", "ব"),("f", "ভ"),("g", "ম"),("h", "য"),("i", "র"),("j", "ল"),("k", "শ"),("l", "ষ"),("m", "স"),("n", "হ"),("o", "ড়"),
	("p", "ঢ়"),("q", "য়"),("r", "ৎ"),("s", "ং"),("t", "ঃ"),("u", "ঁ"),

	# kars
	("•", "ঙ্"),("v", "া"),("w", "ি"),("x", "ী"),("y", "ু"),("z", "ু"),("“", "ু"),("–", "ু"),("~", "ূ"),("ƒ", "ূ"), 
	("‚", "ূ"),("„„", "ৃ"),("„", "ৃ"),("…", "ৃ"),("†", "ে"),("‡", "ে"),("ˆ", "ৈ"),("‰", "ৈ"),("Š", "ৗ"),("\\|", "।"), 
	("\\&", "্‌"), 

	# juktoborno
	("\\^", "্ব"),("‘", "্তু"),("’", "্থ"),("‹", "্ক"),("Œ", "্ক্র"),("”", "চ্"),("—", "্ত"),("˜", "দ্"),("™", "দ্"),("š", "ন্"),
	("›", "ন্"),("œ", "্ন"),("Ÿ", "্ব"),("¡", "্ব"),("¢", "্ভ"),("£", "্ভ্র"),("¤", "ম্"),("¥", "্ম"),("¦", "্ব"),("§", "্ম"),
	("¨", "্য"),("©", "র্"),("ª", "্র"),("«", "্র"),("¬", "্ল"),("­", "্ল"),("®", "ষ্"),("¯", "স্"),("°", "ক্ক"),("±", "ক্ট"),
	("²", "ক্ষ্ণ"),("³", "ক্ত"),("´", "ক্ম"),("µ", "ক্র"),("¶", "ক্ষ"),("·", "ক্স"),("¸", "গু"),("¹", "জ্ঞ"),
	("º", "গ্দ"),("»", "গ্ধ"),("¼", "ঙ্ক"),("½", "ঙ্গ"),("¾", "জ্জ"),("¿", "্ত্র"),("À", "জ্ঝ"),("Á", "জ্ঞ"),("Â", "ঞ্চ"),
	("Ã", "ঞ্ছ"),("Ä", "ঞ্জ"),("Å", "ঞ্ঝ"),("Æ", "ট্ট"),("Ç", "ড্ড"),("È", "ণ্ট"),("É", "ণ্ঠ"),("Ê", "ণ্ড"),("Ë", "ত্ত"),
	("Ì", "ত্থ"),("Í", "ত্ম"),("Î", "ত্র"),("Ï", "দ্দ"),("Ð", "-"),("Ñ", "-"),("Ò", "\""),("Ó", "\""),("Ô", "\'"),("Õ", "\'"),
	("Ö", "্র"),("×", "দ্ধ"),("Ø", "দ্ব"),("Ù", "দ্ম"),("Ú", "ন্ঠ"),("Û", "ন্ড"),("Ü", "ন্ধ"),("Ý", "ন্স"),("Þ", "প্ট"),("ß", "প্ত"),
	("à", "প্প"),("á", "প্স"),("â", "ব্জ"),("ã", "ব্দ"),("ä", "ব্ধ"),("å", "ভ্র"),("æ", "ম্ন"),("ç", "ম্ফ"),("è", "্ন"),("é", "ল্ক"),
	("ê", "ল্গ"),("ë", "ল্ট"),("ì", "ল্ড"),("í", "ল্প"),("î", "ল্ফ"),("ï", "শু"),("ð", "শ্চ"),("ñ", "শ্ছ"),("ò", "ষ্ণ"),("ó", "ষ্ট"),
	("ô", "ষ্ঠ"),("õ", "ষ্ফ"),("ö", "স্খ"),("÷", "স্ট"),("ø", "স্ন"),("ù", "স্ফ"),("ú", "্প"),("û", "হু"),("ü", "হৃ"),
	("ý", "হ্ন"),("þ", "হ্ম")
)
PRO_CONVERSION_MAP = (("্্", "্"))
POST_CONVERSION_MAP = (
	("০ঃ", "০:"),("১ঃ", "১:"),("২ঃ", "২:"),("৩ঃ", "৩:"),("৪ঃ", "৪:"),("৫ঃ", "৫:"),("৬ঃ", "৬:"),("৭ঃ", "৭:"),("৮ঃ", "৮:"),
	("৯ঃ", "৯:"),(" ঃ", " :"),("\nঃ", "\n:"),("]ঃ", "]:"),("\\[ঃ", "\\[:"),("  ", " "),("অা", "আ"),("্‌্‌", "্‌")
)

precars = ('ি', 'ৈ', 'ে')
postcars = ('া'  ,'ো'  ,'ৌ'  ,'ৗ'  ,'ু'  ,'ূ'  ,'ী'  ,'ৃ')
benjonbornos = ('ক' , 'খ' , 'গ' , 'ঘ' , 'ঙ' , 'চ' , 'ছ' , 'জ', 'ঝ' , 'ঞ' , 'ট' , 'ঠ' , 'ড' , 'ঢ' , 'ণ' , 'ত', 'থ' , 'দ' , 'ধ' , 
	'ন' , 'প' , 'ফ' , 'ব' , 'ভ', 'ম' , 'য' , 'র' , 'ল' , 'শ' , 'ষ' , 'স' , 'হ', '়' , '়' , '়' , 'ৎ' , 'ং' , 'ঃ' , 'ঁ')

def _ischaraterin(str, index, charlist):
	if (index >= 0 and index < len(str)):
		c = str[index]
		return c in charlist
	return False

def _isbanglaprekar(str, index):
	return _ischaraterin(str, index, precars)

def _isbanglapostkar(str, index):
	return _ischaraterin(str, index, postcars)

def _isbanglakar(str, index):
	return _ischaraterin(str, index, precars) or _ischaraterin(str, index, postcars)

def _isbanglabanjonborno(str, index):
	return _ischaraterin(str, index, benjonbornos)

def _isBanglaNukta(str, index):
	return _ischaraterin(str, index, ('ঁ'))

def _isBanglaHalant(str, index):
	return _ischaraterin(str, index, ('্'))

def _isSpace(str, index):
	return _ischaraterin(str, index, (' ','\t','\n','\r'))

def _reArrangeUnicodeConvertedText(str):
	strlength = len(str)

	for i in range(0, strlength):
		# Change refs
		if (i < (strlength-1) and str[i] == 'র' and _isBanglaHalant(str, i + 1) and not _isBanglaHalant(str, i - 1)):
			j = 1
			while (True):
				if (i - j < 0):
					break
				
				if (_isbanglabanjonborno(str, i - j) and _isBanglaHalant(str, i - j - 1)):
					j += 2
				elif (j == 1 and _isbanglakar(str, i - j)):
					j += 1
				else:
					break
				
			# temp = subString(str, 0, i - j)
			temp = str[0:i-j]
			temp += str[i]
			temp += str[i+1]
			# temp += subString(str, i - j, i)
			temp += str[i-j:i]
			# temp += subString(str, i + 2, str.length())
			temp += str[i+2:strlength]
			str = temp
			i += 1
			continue
		
	

	str = _docharactermap(str, PRO_CONVERSION_MAP)
	strlength = len(str)
	for i in range(0, strlength):

		if (i < strlength-1 and str[i]=='র' and _isBanglaHalant(str,i+1) and not _isBanglaHalant(str, i-1) and _isBanglaHalant(str, i+2)):
			j = 1
			while (True):
				if (i-j < 0):
					break
				if (_isbanglabanjonborno(str, i-j) and _isBanglaHalant(str, i-j-1)):
					j += 2
				elif (j == 1 and _isbanglakar(str, i-j)):
					j+=1
				else:
					break
				
			
			# temp = subString(str, 0, i - j)
			temp = str[0: i-j]
			temp += str[i]
			temp += str[i+1]
			# temp += subString(str, i - j, i)
			temp += str[i-j:i]
			# temp += subString(str, i + 2, str.length())
			temp += str[i+2:strlength]
			str = temp
			i += 1
			continue
		
		# for 'Vowel + HALANT + Consonant' it should be 'HALANT + Consonant + Vowel'
		if (i > 0 and str[i]=='\u09CD' and (_isbanglakar(str, i - 1) or _isBanglaNukta(str, i - 1)) and i < len(str)-1):
			# temp = subString(str, 0, i - 1)
			temp = str[0:i - 1]
			temp += str[i]
			temp += str[i + 1]
			temp += str[i - 1]
			# temp += subString(str, i + 2, str.length())
			temp += str[i + 2:len(str)]
			str = temp
		

		# for 'RA (\u09B0) + HALANT + Vowel' it should be 'Vowel + RA (\u09B0) + HALANT'
		if (i > 0 and i < len(str) - 1 and str[i] == '\u09CD' and str[i-1]=='\u09B0' and str[i-2]=='\u09CD' and _isbanglakar(str, i + 1)):
			# temp = subString(str, 0, i - 1)
			temp = str[0:i-1]
			temp += str[i + 1]
			temp += str[i - 1]
			temp += str[i]
			# temp += subString(str, i + 2, str.length())
			temp += str[i + 2:len(str)]
			str = temp
		


		# Change pre-kar to post format suitable for unicode
		if (i < len(str) - 1 and _isbanglaprekar(str, i) and isSpace(str, i + 1) == False):
			temp = str[0:i]

			j = 1

			while ((i + j) < len(str) - 1 and _isbanglabanjonborno(str, i + j)):
				if ((i + j) < len(str) and _isBanglaHalant(str, i + j + 1)):
					j += 2
				else:
					break
				
			
			temp += str[i+1:i+j+1]

			l = 0
			if (str[i] == 'ে' and str[i + j + 1] == 'া'):
				temp += "ো"
				l = 1
			elif (str[i] == 'ে' and str[i + j + 1] == 'ৗ'):
				temp += "ৌ"
				l = 1
			else:
				temp += str[i]
			
			temp += str[i + j + l + 1:len(str)]
			str = temp
			i += j
		

		# nukta should be placed after kars
		if (i < len(str) - 1 and _isBanglaNukta(str, i) and _isbanglapostkar(str, i+1)):
			temp = str[0:i]
			temp += str[i + 1]
			temp += str[i]
			temp += str[i+2:len(str)]
			str = temp
		
	return str


def _docharactermap(srcstring, maplist):
	for charmap in maplist:
		srcstring = srcstring.replace(charmap[0], charmap[1])

	return srcstring


def _rearrangeunicode(srcstring):
	return srcstring


def bijoy2unicode(inputtext):
	inputtext = _docharactermap(inputtext, PRE_CONVERSION_MAP)
	inputtext = _docharactermap(inputtext, CONVERSION_MAP)
	inputtext = _reArrangeUnicodeConvertedText(inputtext)
	inputtext = _docharactermap(inputtext, POST_CONVERSION_MAP)
	return inputtext