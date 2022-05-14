import random
def main():
  print("Keep it logically awesome")

 

  #open quotes.txt file
  f = open("quotes.txt")
  quotes = f.readlines()
  last = len(quotes)-1
  rnd = random.randint(0, last)
  f.close()
  print(quotes[0])
  print(quotes[-1])
  print(quotes[rnd])


if __name__== "__main__":
  main()
