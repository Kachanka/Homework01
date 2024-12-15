from string_utils import StringUtils

string_utils = StringUtils()

#positive test_capitilize
cap = string_utils.capitilize("mebel'")
assert cap == ("Mebel'")

cap = string_utils.capitilize("mebel+")
assert cap == ("Mebel+")

cap = string_utils.capitilize("mebel.")
assert cap == ("Mebel.")

#negative test_capitilize
cap = string_utils.capitilize("Mebel")
assert cap == ("Mebel")

#positive test_trim
tr = string_utils.trim("     gonka")
assert tr == ("gonka")

tr = string_utils.trim("     +gonka")
assert tr == ("+gonka")

tr = string_utils.trim("    1 gonka")
assert tr == ("1 gonka")

tr = string_utils.trim("     gonka1")
assert tr == ("gonka1")

tr = string_utils.trim("     gonka 1")
assert tr == ("gonka 1")

#pozitive test_to_list
tl = string_utils.to_list("голова,туловище,руки,ноги")
assert tl == ["голова", "туловище", "руки", "ноги"]

tl = string_utils.to_list(" голова, туловище, руки, ноги")
assert tl == [" голова", " туловище", " руки", " ноги"]

tl = string_utils.to_list("-,+,/,&")
assert tl == ["-", "+", "/", "&"]

tl = string_utils.to_list("1,2,3,4")
assert tl == ["1", "2", "3", "4"]

#negative test_to_list
tl = string_utils.to_list("-,+,/,&")
assert tl == ["-", "+", "/"]

#positive test_contains
con = string_utils.contains("Lol", "L")
assert con is True
con = string_utils.contains("Lol", "F")
assert con is False

con = string_utils.contains("3Lol", "3")
assert con is True
con = string_utils.contains("3Lol", "4")
assert con is False

con = string_utils.contains("+Lol", "+")
assert con is True
con = string_utils.contains("3Lol", "-")
assert con is False

#positive test_delete_symbol
dl = string_utils.delete_symbol("Carrot", "Car")
assert dl == ("rot")

dl = string_utils.delete_symbol("Carrot34", "Car")
assert dl == ("rot34")

dl = string_utils.delete_symbol("Carrot34", "34")
assert dl == ("Carrot")

dl = string_utils.delete_symbol("+Carrot+", "+Car")
assert dl == ("rot+")

#negative test_delete_symbol
dl = string_utils.delete_symbol("Carrot34", "Carrot34")
assert dl == ("")

#pozitive test_starts_with
sw = string_utils.starts_with("Ariel", "A")
assert sw is True
sw = string_utils.starts_with("Ariel", "1")
assert sw is False

sw = string_utils.starts_with("1Ariel", "1")
assert sw is True
sw = string_utils.starts_with("1Ariel", "A")
assert sw is False

ew = string_utils.end_with("Ariel", "l")
assert ew is True
ew = string_utils.end_with("Ariel", "A")
assert sw is False

ew = string_utils.end_with("Ariel1", "1")
assert ew is True
ew = string_utils.end_with("Ariel1", "l")
assert sw is False

ie = string_utils.is_empty("")
assert ie is True
ie = string_utils.is_empty("      ")
assert ie is True
ie = string_utils.is_empty("  ")
assert ie is True
ie = string_utils.is_empty("1")
assert ie is False
ie = string_utils.is_empty("/")
assert ie is False

#negative test_is_empty
ie = string_utils.is_empty("")
assert ie is False

#positive test_list_to_string
lts = string_utils.list_to_string([1, 2, 3])
assert lts == "1, 2, 3"

lts = string_utils.list_to_string(["Ari", "el"])
assert lts == "Ari, el"

lts = string_utils.list_to_string([-, +, /])
assert lts == "-, +, /"
#negative test_list_to_string
lts = string_utils.list_to_string(["Ari", "el"])
assert lts == "  "

lts = string_utils.list_to_string(["  "])
assert lts == "Ari, el"

