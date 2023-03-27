
  def test_shout_miguel(self):
    self.assertEqual(shout("shake it up, baby, now"), "SHAKE IT UP, BABY, NOW!")

  def test_shout_shout(self):
    self.assertEqual(shout("shout"), "SHOUT!")

  def test_shout_minuto(self):
    self.assertEqual(shout("twist"), "twist!")