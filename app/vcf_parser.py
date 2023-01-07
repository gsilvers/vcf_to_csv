"""
Module containing logic to process VCF files into a python list of dictionaries
For information on VCF files see: https://en.wikipedia.org/wiki/VCard
"""

VALID_KEYS = [
    "ADR",
    "AGENT",
    "ANNIVERSARY",
    "BDAY",
    "BEGIN",
    "CALADRURI",
    "CALURI",
    "CATEGORIES",
    "CLASS",
    "CLIENTPIDMAP",
    "EMAIL",
    "END",
    "FBURL",
    "FN",
    "GENDER",
    "GEO",
    "IMPP",
    "KEY",
    "KIND",
    "LABEL",
    "LANG",
    "LOGO",
    "MAILER",
    "MEMBER",
    "N",
    "NAME",
    "NICKNAME",
    "NOTE",
    "ORG",
    "PHOTO",
    "PRODID",
    "PROFILE",
    "RELATED",
    "REV",
    "ROLE",
    "SORT-STRING",
    "SOUND",
    "SOURCE",
    "TEL",
    "TITLE",
    "TZ",
    "UID",
    "URL",
    "VERSION",
    "XML"
]


class VCFParser:
    """
    Parses and reads a vcf file and encapsulates the data in a list
    of dictionaries. Provides some methods for easy access but the
    list is also available as a class variable self.vcf_dict.
    """

    def __init__(self):
        """
        Creates an empty VCF Parser
        """
        self.vcf_dict = {}

    def parse_vcf_file(self, file_path: str):
        """
        Read a VCF File place its data into self.vcf_dict

        :param file_path: Path to the vcf file
        """
        with open(file_path, 'r') as vcf_file:
            for line in vcf_file:
                print(line)
