# this is a part of LibreWeb project

import pickle


class LibreWebPickle:
    def __init__(self, FILE="libreweb.data"):
        '''Set your name for saved/created file'''
        self.FILE = FILE

    def save(self, my_variable):
        with open(self.FILE, "wb") as file:
            pickle.dump(my_variable, file)
            file.close()

    def read(self):
        with open(self.FILE, "rb") as file:
            return pickle.load(file)


def insert_data(storage, sheet_name, url, tag, array_nr, cell_address, insert_as):
    '''return a dict'''
    if sheet_name in storage:
        target = storage[sheet_name]
        if url in target:
            target = target[url]
            if tag in target:
                storage[sheet_name][url][tag][cell_address] = [array_nr, insert_as]
            else:
                storage[sheet_name][url][tag] = {cell_address: [array_nr, insert_as]}
        else:
            storage[sheet_name][url] = {tag: {cell_address: [array_nr, insert_as]}}
    else:
        storage[sheet_name] = {url: {tag: {cell_address: [array_nr, insert_as]}}}
    return storage
