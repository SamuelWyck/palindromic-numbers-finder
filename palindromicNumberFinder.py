class PalindromeFinder:
    def __init__(self):
        self.last_palindrome = -1
        self.last_ordinal = -1
        self.found_palindromes = []


    def find_palindromes(self):
        palindrome_candidate = self.last_palindrome + 1
        while len(self.found_palindromes) < 10000:
            temp_candidate = palindrome_candidate
            reversed_candidate = 0

            while temp_candidate > 0:
                reversed_candidate *= 10
                digit = temp_candidate % 10
                reversed_candidate += digit
                temp_candidate = temp_candidate // 10

            if palindrome_candidate == reversed_candidate:
                self.found_palindromes.append(palindrome_candidate)
                print(palindrome_candidate)
            
            palindrome_candidate += 1
            



finder = PalindromeFinder()
finder.find_palindromes()