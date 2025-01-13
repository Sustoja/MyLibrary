from src.FilesAndFolders.folderwalking import *

def test_files_in_folder_tree():
    test_folder = './myfilesfolders/filesfolders'
    file_list = [str(file) for file in get_files_in_folder_tree(test_folder)]
    expected_list = {'myfilesfolders/filesfolders/A/A1.txt',
                     'myfilesfolders/filesfolders/A/A2.xml',
                     'myfilesfolders/filesfolders/B/B1.txt',
                     'myfilesfolders/filesfolders/A/C/C1.pdf'}
    assert set(file_list) == expected_list


def test_files_in_folder_tree_with_extensions():
    test_folder = './myfilesfolders/filesfolders'
    extensions = ['txT']
    file_list = [str(file) for file in get_files_in_folder_tree(test_folder, extensions)]
    expected_list = {'myfilesfolders/filesfolders/A/A1.txt', 'myfilesfolders/filesfolders/B/B1.txt'}
    assert set(file_list) == expected_list


def test_files_in_folder():
    test_folder = './myfilesfolders/filesfolders/B'
    file_list = [str(file) for file in get_files_in_folder(test_folder)]
    expected_list = {'myfilesfolders/filesfolders/B/B1.txt'}
    assert set(file_list) == expected_list


def test_files_in_folder_with_extensions():
    test_folder = './myfilesfolders/filesfolders/A'
    extensions = ['txT']
    file_list = [str(file) for file in get_files_in_folder_tree(test_folder, extensions)]
    expected_list = {'myfilesfolders/filesfolders/A/A1.txt'}
    assert set(file_list) == expected_list
