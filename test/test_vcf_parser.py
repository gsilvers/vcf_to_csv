"""
Tests for VCF Parser
"""
import unittest

from app.vcf_parser import VCFParser

class TestVCFParser(unittest.TestCase):

    def test_create_vcf_parser(self):
       vcf_parser = VCFParser()
       self.assertIsNotNone(vcf_parser)
       self.assertEqual(vcf_parser.vcf_dict, {})
