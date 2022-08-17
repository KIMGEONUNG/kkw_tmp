import unittest
from unittest import TestCase
from pycomar.images.utils import gray2jet
import torch


class Tester(TestCase):

  def setup(self):
    pass

  def test_set1(self):
    x = torch.randn(10)
    self.assertRaises(Exception, gray2jet, x)


if __name__ == '__main__':
  unittest.main()
