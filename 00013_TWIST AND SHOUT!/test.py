
  def test_shout_miguel(self):
    self.assertEqual(shout("miguel"), "MIGUEL!")

  def test_shout_shout(self):
    self.assertEqual(shout("shout"), "SHOUT!")

  def test_shout_minuto(self):
    self.assertEqual(shout("minuto"), "MINUTO!")