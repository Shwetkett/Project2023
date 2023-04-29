# importing library
import requests


# function for scanning subdomains
def domain_scanner(domain_name,sub_domnames):
    print('-----------Scanner Started-----------')
    print('----URL after scanning subdomains----')
     
    # loop for getting URL's
    urls = []
    for subdomain in sub_domnames:
       
        # making url by putting subdomain one by one
        url = f"https://{subdomain}.{domain_name}"
         
        # using try catch block to avoid crash of
        # the program
        try:
           
            # sending get request to the url
            requests.get(url)
             
            # if after putting subdomain one by one url
            # is valid then printing the url
            urls.append(f'[+] {url}')
             
        # if url is invalid then pass it
        except requests.ConnectionError:
            pass

    return urls
    print('\n')
    print('----Scanning Finished----')
    print('-----Scanner Stopped-----')
  

        
# main function
if __name__ == '__main__':
   
    # inputting the domain name
    dom_name = input("Enter the Domain Name:")
    print('\n')
 
    # opening the subdomain text file
    with open('subDomain.txt','r') as file:
       
        # reading the file
        name = file.read()
         
        # using splitlines() function storing the
        # list of splitted strings
        sub_dom = name.splitlines()
         
    # calling the function for scanning the subdomains
    # and getting the url
    print(domain_scanner(dom_name,sub_dom))
