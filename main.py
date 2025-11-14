from palindromicNumberFinder import PalindromeFinder



def main():
    palindrome_finder = PalindromeFinder()
    try:
        palindrome_finder.start()
    except KeyboardInterrupt:
        print("Shutting down gracefully...")
        palindrome_finder.save_found_palindromes()
        print("Done")




if __name__ == "__main__":
    main()