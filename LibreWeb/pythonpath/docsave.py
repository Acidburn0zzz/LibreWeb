# Check if Document Storage has a folder and this folder contains
# save_file, then call read function.
# Otherwise call save_file
from ast import literal_eval
from settings import save_file_name as FILE
from settings import save_dir_name as FOLDER


def save_file(smgr, doc, data, folder=FOLDER, file=FILE):
    sfa = smgr.createInstance("com.sun.star.ucb.SimpleFileAccess")
    rep_url = ('vnd.sun.star.tdoc:/{}/{}'.format(doc.RuntimeUID, folder))
    file_url = '{}/{}'.format(rep_url, file)
    pipe = smgr.createInstance("com.sun.star.io.Pipe")
    text_out = smgr.createInstance("com.sun.star.io.TextOutputStream")
    text_out.setOutputStream(pipe)
    text_out.setEncoding("UTF-8")
    # version 1.0.7
    # convert dict to string
    data = str(data)
    text_out.writeString(data)
    text_out.closeOutput()
    sfa.writeFile(file_url, pipe)
    doc.store()


def read_file(smgr, doc, folder=FOLDER, file=FILE):
    '''Read and return dict from current document'''
    text_in = smgr.createInstance("com.sun.star.io.TextInputStream")
    sfa = smgr.createInstance("com.sun.star.ucb.SimpleFileAccess")
    file_url = "vnd.sun.star.tdoc:/" + doc.RuntimeUID + "/" + FOLDER + "/" + FILE
    file_read = sfa.openFileRead(file_url)
    text_in.setInputStream(file_read)
    result = text_in.readString([], True)
    text_in.closeInput()
    # convert string to a dict
    return literal_eval(result)


def check_save_file(doc, folder=FOLDER, file=FILE):
    '''Check if save file exists'''
    if folder in doc.DocumentSubStoragesNames:
        return doc.DocumentStorage.getByName(folder).hasByName(file)
    return False
