class Test(unittest.TestCase):

  def test_11_is_not_high_noon(self):
    self.assertFalse(is_high_noon(11))

  def test_14_is_not_high_noon(self):
    self.assertFalse(is_high_noon(14))
    
  def test_12_is_high_noon(self):
    self.assertTrue(is_high_noon(12))


