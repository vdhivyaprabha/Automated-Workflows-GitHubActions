import random

"""
This class is intended to generate passwords using two primary input parameters, how many characters should be included in the password 
and number of passowords required by the user. Once that is initialized the program would be able to generate the passwords with the 
required length. 
"""
class CreateEncryptionPasswords:

    characters_used = "abcdefghijklmnopqrstuvwxyz"
    
    def __init__(self, number_of_passwords):
      self.number_of_passwords = number_of_passwords

    """
        This function is intended to generate the password by accepting the password length as input parameter and 
        the characters used to create the password will be retrived from the the class level object.
    """
    def generate_credentials(self,password_length):
        alphabet = self.characters_used
        for element in password_length:
            generated_password = ""
            for iteartion_element in range(element):
                next_letter_index = random.randrange(len(alphabet))
                generated_password = generated_password + alphabet[next_letter_index]
            generated_password = self.replace_with_number(generated_password)
            generated_password = self.replace_with_uppercase(generated_password)
        return generated_password

    """
        This function is intended to do a Floor division on two element , the first element would be the numerator element
        and the seconf element will be a denominator element.
    """
    def floor_division(self,num_element,denom_element):
        return num_element//denom_element

    def replace_with_number(self,generated_password):
        for iteartion_element in range(random.randrange(1,3)):
            replace_index = random.randrange(self.floor_division(len(generated_password),2)) 
            generated_password = generated_password[0:replace_index] + str(random.randrange(10)) + generated_password[replace_index+1:]
            return generated_password

    """
        This function is intended to convert the creadentail value to the upper cacse letters.
    """
    def replace_with_uppercase(self,credential_value):
        for iteartion_element in range(random.randrange(1,3)):
            replace_index = random.randrange(self.floor_division(len(credential_value),2),len(credential_value))  
            credential_value = credential_value[0:replace_index] + credential_value[replace_index].upper() + credential_value[replace_index+1:]
            return credential_value

    
    def trigger_creation(self,length_of_password):
        passwordLengths = []
        generated_passwords_list = []
        for element in range(self.number_of_passwords):
            passwordLengths.append(length_of_password)
            generated_passwords = self.generate_credentials(passwordLengths)
            generated_passwords_list.append(generated_passwords)
        return generated_passwords_list


# Input Parameters Passed to create the password, This can be extended to get from the user and processed.
number_of_passwords = 5
length_of_password = 15

# Creation of the object to trigger the creation of credentials.
password_instance = CreateEncryptionPasswords(number_of_passwords)
generated_passwords_list = password_instance.trigger_creation(length_of_password)
print(generated_passwords_list)