
  def test_loves_reading_25_is_true(self):
    self.assertTrue(loves_reading(25))
  
  def test_loves_reading_80_is_true(self):
    self.assertTrue(loves_reading(80))
  
  def test_loves_reading_1_is_false(self):
    self.assertFalse(loves_reading(1))
  
  def test_loves_reading_15_is_false(self):
    self.assertFalse(loves_reading(15))
