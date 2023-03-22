
  def test_full_name_length_Guy_Incognito(self):
    self.assertEqual(full_name_length("Guy", "Incognito"), 13)

  def test_full_name_length_John_Snow(self):
    self.assertEqual(full_name_length("John", "Snow"), 9)

  def test_full_name_length_Juana_Azurduy(self):
    self.assertEqual(full_name_length("Juana", "Azurduy"), 13)
    
  def test_contemplate_the_space(self):
    resultado = False
    try:
      resultado = [
        full_name_length("", ""),
        full_name_length("abc", "d"),
      ] == [0, 4]
    except:
      pass
    if resultado:
      self.fail("You are not contemplating space!")
