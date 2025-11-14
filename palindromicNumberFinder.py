import os



class PalindromeFinder:
    def __init__(self):
        self.last_palindrome = -1
        self.last_ordinal = -1
        self.found_palindromes = []

        self.found_palindromes_file_path = os.path.abspath("./foundPalindromes.txt")
        self.last_found_palindrome_file_path = os.path.abspath('./lastPalindrome.txt')
    

    def start(self):
        self.load_last_palindrome()
        while True:
            self.find_palindromes()
            self.save_found_palindromes()

    
    def load_last_palindrome(self):
        try:
            last_palindrome_info = None
            with open(self.last_found_palindrome_file_path, "r") as file:
                last_palindrome_info = file.read()
            
            ordinal, palindrome = self.parse_palindrome_info(last_palindrome_info)
            self.last_palindrome = palindrome
            self.last_ordinal = ordinal
        except:
            self.last_palindrome = -1
            self.last_ordinal = -1
    
    

    def parse_palindrome_info(self, palindrome_info):
        info_parts = palindrome_info.split(" ")
        ordinal_index = 0
        palindrome_index = 1
        return int(info_parts[ordinal_index]), int(info_parts[palindrome_index])


    def find_palindromes(self):
        palindrome_candidate = self.last_palindrome + 1
        while len(self.found_palindromes) < 1000:
            temp_candidate = palindrome_candidate
            reversed_candidate = 0

            while temp_candidate > 0:
                reversed_candidate *= 10
                digit = temp_candidate % 10
                reversed_candidate += digit
                temp_candidate = temp_candidate // 10

            if palindrome_candidate == reversed_candidate:
                self.found_palindromes.append(palindrome_candidate)
            
            palindrome_candidate += 1
    

    def save_found_palindromes(self):
        self.last_ordinal += 1
        final_ordinal = 0
        final_palindrome = 0
        with open(self.found_palindromes_file_path, "a") as file:
            for i in range(len(self.found_palindromes)):
                ordinal = i + self.last_ordinal
                palindrome = self.found_palindromes[i]
                line = f"{ordinal} {palindrome}\n"
                file.write(line)
                final_ordinal = ordinal
                final_palindrome = palindrome
        
        with open(self.last_found_palindrome_file_path, "w") as file:
            file.write(f"{final_ordinal} {final_palindrome}")

        self.found_palindromes = []
        self.last_ordinal = final_ordinal
        self.last_palindrome = final_palindrome