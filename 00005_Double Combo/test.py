
  def test_previous_1_is_0(self):
    self.assertEqual(previous(1), 0);

  def test_previous_10_is_9(self):
    self.assertEqual(previous(10), 9)

  def test_triple_1_is_3(self):
    self.assertEqual(triple(1), 3)

  def test_triple_3_is_9(self):
    self.assertEqual(triple(3), 9)

  def test_previous_of_triple_1_is_2(self):
    self.assertEqual(prev_of_triple(1), 2)

  def test_previous_of_triple_3_is_8(self):
    self.assertEqual(prev_of_triple(3), 8)

  def test_previous_of_triple_10_is_29(self):
    self.assertEqual(prev_of_triple(10), 29)
