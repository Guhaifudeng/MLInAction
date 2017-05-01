#!python27
# -*- coding: utf-8 -*-
'''
Example: using decision trees to predict contact lens type
1. Collect: Text file provided.
2. Prepare: Parse tab-delimited lines.
3. Analyze: Quickly review data visually to make sure it was parsed properly. The final
tree will be plotted with createPlot().
4. Train: Use createTree() from section 3.1.
5. Test: Write a function to descend the tree for a given instance.
6. Use: Persist the tree data structure so it can be recalled without building the
tree; then use it in any application.
'''

from numpy import *
def createDataSet(filename):
    fr = open(filename)
    dataSet = [inst.strip().split('\t') for inst in fr.readlines()]
    labels = ['ages', 'prescript', 'astigmatic', 'tearRate']
    return dataSet, labels
