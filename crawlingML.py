#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Product:
    def __init__(self):
        pass

    def setCategory(self, category):
        self.categoriy = category

    def setSubCategory(self, subCategory):
        self.subCategory = subCategory

    def setDescription(self, description):
        self.desctription = description

    def addComments(self, comments):
        self.comments = self.comments


import requests as rq
from bs4 import BeautifulSoup as Bs

def getCategoriesLinks():
    pageMain = rq.get('https://www.mercadolivre.com.br/categories.html#menu=categories')
    bs = Bs(pageMain.text, 'lxml')
    h2s = bs.find('div', attrs={'class' : 'ch-box-lite ch-rightcolumn ch-clearfix'}).findAll('h2')
    return [e.find('a').get('href') for e in h2s]

def getSubCategoriesLinks(categoriesLinks):
    subCategories = []
    pagesCat = [rq.get(e) for e in categoriesLinks]
    for pageCat in pagesCat:
        if(pageCat.status_code == rq.codes.ok):
            bsCat = Bs(pageCat.text, 'lxml')
            div = bsCat.find('div', attrs={'class' : 'ui-card categories'})
            if(div != None):
                h2s = div.findAll('h2')
                subCategories.extend([e.find('a').get('href') for e in h2s])
        else:
            print('Returned with error: {}'.format(pageCat.status_code))
    return subCategories

def getProductsPages(subCategoriesLinks):
    subCategoriesPages = [rq.get(e) for e in subCategoriesLinks]
    for subCategoryPage in subCategoriesPages:
        bsSubCategory = Bs(subCategoryPage.text, 'lxml')
        h2s = bsFirstPage.find('div', attrs={'class' : 'section search-results list-view grid search-results-core results-with-variations list--has-row-logos list--has-fulfillment'}).findAll('a')
    
#def main(args):        
#    return 0

#if __name__ == '__main__':
#    import sys
#    sys.exit(main(sys.argv))
