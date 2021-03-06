#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import pprint
from processfile.decoders.base_decoder import BaseFileDecoder
from xmlutils.xml2json import xml2json

'''This module contains the XMLFileDecoder class
   which decodes XML data'''


class XMLFileDecoder(BaseFileDecoder):

    def __init__(self, filename, logger=None):
        super(XMLFileDecoder, self).__init__(filename, logger)

    def get_employees(self):
        with open(self.filename) as xml_file:
            self.logger.info('reading XML data from %s', self.filename)
            converter = xml2json(self.filename)
            data = json.loads(converter.get_json())
            self.logger.info('reading XML data: done')
        return data["root"]["employees"]["element"]
