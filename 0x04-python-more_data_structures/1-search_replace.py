#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def replace_elem(elem):
        if elem == search:
            return replace
        else:
            return elem

    return list(map(replace_elem, my_list))
