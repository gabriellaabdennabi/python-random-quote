import random
def main():
  # print("Keep it logically awesome")



  #open quotes.txt file
  # f = open("quotes.txt")
  # quotes = f.readlines()
  # last = len(quotes)-1
  # rnd = random.randint(0, last)
  # f.close()

  # print(quotes[0])
  # print(quotes[-1])
  # print(quotes[rnd])

  #print out multiple quotes

  # for quote in quotes:
  #   print(quote.strip())


  #Write to a file
  f = open("quotes.txt","a")
  f.write("Cats are awesome and so are you\n")
  f.close()

  f = open("quotes.txt")
  quotes = f.readlines()

  print(quotes[-1])


if __name__== "__main__":
  main()
