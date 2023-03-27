
  def test_shout_shake_it_up_baby_now(self):
    self.assertEqual(shout("shake it up, baby, now"), "SHAKE IT UP, BABY, NOW!")

  def test_shout_shout(self):
    self.assertEqual(shout("shout"), "SHOUT!")

  def test_shout_twist(self):
    self.assertEqual(shout("twist"), "TWIST!")