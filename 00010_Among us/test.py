
  def test_is_between_10_1_10_is_False(self):
    self.assertFalse(is_between(10, 1, 10))

  def test_is_between_4_4_9_is_False(self):
    self.assertFalse(is_between(4, 4, 9))

  def test_is_between_12_1_10_is_False(self):
    self.assertFalse(is_between(12, 1, 10))

  def test_is_between_200_54_112_is_False(self):
    self.assertFalse(is_between(200, 54, 112))

  def test_is_between_67_0_100_is_True(self):
    self.assertTrue(is_between(67, 0, 100))

  def test_is_between_2_0_100_is_True(self):
    self.assertTrue(is_between(2, 0, 100))

  def test_is_out_of_range_0_1_10_is_False(self):
    self.assertTrue(is_out_of_range(0, 1, 10))

  def test_is_out_of_range_12_1_10_is_True(self):
    self.assertTrue(is_out_of_range(12, 1, 10))

  def test_is_out_of_range_200_54_112_is_True(self):
    self.assertTrue(is_out_of_range(200, 54, 112))

  def test_is_out_of_range_67_0_100_is_False(self):
    self.assertFalse(is_out_of_range(67, 0, 100))

  def test_is_out_of_range_2_0_100_is_False(self):
    self.assertFalse(is_out_of_range(2, 0, 100))
