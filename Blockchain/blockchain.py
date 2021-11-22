#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 12:14:01 2021

Course Blockchain A - Z

@author: kadune
"""

import datetime
import hashlib
from flask import Flask, jsonify


class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')
