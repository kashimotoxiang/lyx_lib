# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

class Mask():
    mask = None
    i_matrix = None
    o_matrix = None
    header = None

    def __init__ ( self, i_matrix, o_matrix, header ):
        self.i_matrix = i_matrix
        self.o_matrix = o_matrix
        self.header = header
        self.mask = i_matrix == o_matrix

    def get_column ( self, column_name ):
        i_column = self.i_matrix[column_name]
        o_column = self.o_matrix[column_name]
        return i_column, o_column

    def get_mask_index ( self, field_name, mode ):
        if mode == 'cf':
            index = self.mask.index[~self.mask[field_name]].tolist()
        elif mode == 'ct':
            index = self.mask.index[self.mask[field_name]].tolist()
        elif mode == 'lf':
            # TODO
            index = self.mask.index[~self.mask.loc[field_name]].tolist()
        elif mode == 'ct':
            # TODO
            index = self.mask.index[self.mask.loc[field_name]].tolist()
        else:
            raise ('please input correct mode name')
        return index
