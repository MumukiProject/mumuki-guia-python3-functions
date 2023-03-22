class Test(unittest.TestCase):

  def test_Rosario_is_not_longer_than_Bahia_Blanca(self):
    self.assertFalse(is_longer_than("Rosario", "Bahía Blanca"))

  def test_Valle_de_Uco_is_longer_than_La_Punta(self):
    self.assertTrue(is_longer_than("Valle de Uco", "La Punta"))