
  def test_saturday_is_weekend(self):
    self.assertTrue(is_weekend("Saturday") or is_weekend("saturday"))

  def test_sunday_is_weekend(self):
    self.assertTrue(is_weekend("Sunday") or is_weekend("sunday"))

  def test_monday_is_not_weekend(self):
    self.assertFalse(is_weekend("Monday"))

  def test_friday_is_not_weekend(self):
    self.assertFalse(is_weekend("Friday"))

