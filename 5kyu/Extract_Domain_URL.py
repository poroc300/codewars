#Problem "Extract the domain name from a URL"
#level: 5kyu
#language: Python
#link: https://www.codewars.com/kata/514a024011ea4fb54200004b
####################################################### INSTRUCTIONS ######################################################################
#Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

#domain_name("http://github.com/carbonfive/raygun") == "github" 
#domain_name("http://www.zombie-bites.com") == "zombie-bites"
#domain_name("https://www.cnet.com") == "cnet"
####################################################### SOLUTION ######################################################################
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
