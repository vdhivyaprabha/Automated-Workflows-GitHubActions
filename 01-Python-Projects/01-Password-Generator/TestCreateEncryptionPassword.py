import unittest
from CreateEncryptionPasswords import *

class TestCreateEncryptionPassword(unittest.TestCase):

    number_of_passwords = 5
    length_of_password = 15

    def test_password_creation(self):
        password_instance = CreateEncryptionPasswords(number_of_passwords)
        generated_passwords_list = password_instance.trigger_creation(length_of_password)
        password_length = len(generated_passwords_list)
        failure_message = "Number of passwords generated should be {} instead its is :: {} ".format(number_of_passwords,password_length)
        self.assertEqual(password_length, 5,failure_message)

    def test_password_length(self):
        password_instance = CreateEncryptionPasswords(number_of_passwords)
        generated_passwords_list = password_instance.trigger_creation(length_of_password)
        is_password_valid = True
        for index in range(len(generated_passwords_list)):
            if len(generated_passwords_list[index]) != 15:
                is_password_valid = False
                break
        failure_message = "Password Length Should be 15 Characters"
        self.assertEqual(is_password_valid, True,failure_message)

if __name__ == '__main__':
    unittest.main()