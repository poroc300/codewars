#Problem "Phone Directory"
#level: 5kyu
#language: Python
#link: https://www.codewars.com/kata/56baeae7022c16dd7400086e
####################################################### INSTRUCTIONS ######################################################################
#John keeps a backup of his old personal phone book as a text file. On each line of the file he can find the phone number (formated as +X-abc-def-ghij where X stands for one or two digits), the corresponding name between < and > and the address.
#
#Unfortunately everything is mixed, things are not always in the same order; parts of lines are cluttered with non-alpha-numeric characters (except inside phone number and name).
#
#Examples of John's phone book lines:
#
#"/+1-541-754-3010 156 Alphand_St. <J Steeve>\n"
#
#" 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"
#
#"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n"
#
#Could you help John with a program that, given the lines of his phone book and a phone number returns a string for this number : "Phone => num, Name => name, Address => adress"
#
#Examples:
#
#s = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"
#
#phone(s, "1-541-754-3010") should return "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."
#It can happen that, for a few phone numbers, there are many people for a phone number -say nb- , then
#
#return : "Error => Too many people: nb"
#
#or it can happen that the number nb is not in the phone book, in that case
#
#return: "Error => Not found: nb"
####################################################### SOLUTION ##########################################################################
def phone(dr, num):
    #check if a number is associated with more than one people or if is not present
    if dr.count("+" + num) > 1:
        return "Error => Too many people: {}".format(num)
    elif dr.count(num) == 0:
        return "Error => Not found: {}".format(num)
    
    #divide the phone list by each line/entry 
    phone_book = dr.split("\n") 
    
    #get the contact information correspondent to the input number
    for entry in phone_book:
        if ("+" + num) in entry:
            contact = entry
            break
    
    #get name
    name = contact.split("<")[-1].split(">")[0]
    
    #get address
    import re
    address = re.sub(r'[/*+\n$_!,;:?]', " ", contact) #replace many non-word characters by space ("." and "-" must remain)
    
    #remove name and num from address
    address = address.replace("<"+name+">", "").replace(num, "")
    
    #get rid of white spaces
    ls_address = address.split()

    return "Phone => {}, Name => {}, Address => {}".format(num,name," ".join(ls_address))
