def html_page_creator(name, description):
    with open("page.html", "w") as page:
        page.write(
                    """<!DOCTYPE html> \n"""
                    """<html lang="en"> \n"""
                    """     <head> \n"""
                    """          <meta charset="UTF-8"> \n"""
                    """          <meta name="viewport" content= "width=device-width, initial-scale=1.0"> \n"""
                    """          <title>Document Title</title> \n"""
                    """     </head> \n"""
                    """     <body> \n"""
                                    f"              <p>My name is {name}</p>\n"
                                    f"              <p>{description}</p>\n"
                    """     </body> \n"""
                    """</html> \n"""
        )

def main():
    print("Welcome to the HTML page creator! ")
    name = input("Enter your name ")
    description = input("Tell us about yourself ")
    html_page_creator(name, description)
    print("Thanks for your response! Please check your HTML page in the folder!")

main()