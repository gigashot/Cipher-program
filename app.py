import csv
with open("deciphered.csv", "a", newline="") as csv_file:
    fieldnames = ["message"]
    csv_writer = csv.writer(csv_file)
   # csv_writer.writerow({"message": "ahoj"})
import csv

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ciphered_message = []
def cipher():
    with open("deciphered.csv", "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        message = list(csv_reader) # vezme věci z cvs do listu
        
        for words in message:
            for letters in words:
                for letter in letters:
                    if letter in alphabet:
                        index = alphabet.index(letter) # bereme index písmena
                        new_index = (index + 2) % len(alphabet) # posuneme index o +2
                        new_letter = alphabet[new_index] # assigneme písmeno novému indexu 
                        #print(f"{letter} -> {new_letter}")  # testování průběhu šifry
                        ciphered_message.append(new_letter)
                        
                    else:
                        # na výjimky
                        print(letter)   

        print("Message has been ciphered and saved to ciphered.csv")
        print("if you want to share this message please share the ciphered.csv file")

        with open("ciphered.csv", "a", newline="") as csv_file:

            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow(ciphered_message)
            # print(ciphered_message) #zde zobrazujeme schovanou zprávu
            print("Message has been saved to ciphered.csv")
            return ciphered_message
    

def decipher(): # stejene jak sifrovani jen index -2
    with open("ciphered.csv", "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        message = list(csv_reader)
        deciphered_message = []
        for words in message:
            for letters in words:
                # Loop through each character in the string
                for letter in letters:
                    if letter in alphabet:
                        index = alphabet.index(letter) # bereme index písmena
                        new_index = (index - 2) % len(alphabet) # posuneme index o -2
                        new_letter = alphabet[new_index] # assigneme písmeno novému indexu 
                        # print(f"{letter} -> {new_letter}")   #testování průběhu šifry
                        deciphered_message.append(new_letter)
                        
                    else:
                        # na výjimky
                        print(letter)   

        print("Message has been deciphered")

        with open("deciphered.csv", "a", newline="") as csv_file:

            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow(deciphered_message)
            # print(deciphered_message) zde zobrazujme schovanou zprávu
            print("Message has been saved to deciphered.csv")
            return deciphered_message
        

def main():
    while True:
        print("\nwelcome to the cipher machine")
        print("1) Cipher a message")
        print("2) Decipher a message")
        print("3) Exit")
        user_input = input("Please select your choice: ")
        if user_input == "1":
            print("Would you like to enter a message or use a file?")
            print("1) Enter message")
            print("2) Use file")
            user_input = input("Please select your choice: ")
            if user_input == "1":
                print("Please enter the message you would like to cipher")
                cipher_request = input("Message: ")
                with open("deciphered.csv", "w", newline="") as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([cipher_request])
                cipher()

            elif user_input == "2":
                print("Please enter the file name")
                file_name = input("File name: ")
                with open(file_name, "r", newline="") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    message = list(csv_reader)
                    with open("deciphered.csv", "w", newline="") as csv_file:
                        csv_writer = csv.writer(csv_file)
                        csv_writer.writerow(message)
                    cipher()

        elif user_input == "2":
            print("Would you like to enter a message or use a file?")
            print("1) Enter message")
            print("2) Use file")
            user_input = input("Please select your choice: ")
            if user_input == "1":
                print("Please enter the message you would like to decipher")
                decipher_request = input("Message: ")
                with open("ciphered.csv", "w", newline="") as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([decipher_request])
                decipher()

            elif user_input == "2":
                print("Please enter the file name")
                file_name = input("File name: ")
                with open(file_name, "r", newline="") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    message = list(csv_reader)
                    with open("ciphered.csv", "w", newline="") as csv_file:
                        csv_writer = csv.writer(csv_file)
                        csv_writer.writerow(message)
                    decipher()

        elif user_input == "3":
            break
        else:
            print("Invalid input. Please enter 1/2/3.")
main()