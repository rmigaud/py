class AreTheseTwoStrings:
  def __init__(self, first_str, second_str):
    self.first_str = first_str
    self.second_str = second_str

  def anagrams(self):
    if len(self.first_str) != len(self.second_str):
      return False
    frequency_of = {}

    for letter in self.first_str:
      if letter in frequency_of.keys():
        frequency_of.update({letter : frequency_of[letter]+1})
      else:
        frequency_of.update({letter : 1})
    print(frequency_of)
    
    for letter in self.second_str:
      if letter in frequency_of.keys():
        freq = frequency_of.get(letter)
        if freq > 0:
          frequency_of.update({letter : freq-1});
        else:
          return False
      else:
        return False

    print(frequency_of)
    print("returning true")
    return True

print(AreTheseTwoStrings("1BABA","ABBA1").anagrams())