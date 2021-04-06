from application.secretary import check_document_existance,\
    get_doc_owner_name,\
    get_all_doc_owners_names,\
    remove_doc_from_shelf,\
    add_new_shelf,\
    append_doc_to_shelf,\
    delete_doc,\
    get_doc_shelf,\
    move_doc_to_shelf,\
    show_document_info,\
    show_all_docs_info,\
    add_new_doc,\
    secretary_program_start,\
    documents


import unittest

x = documents

class TestSomething(unittest.TestCase):

    def test_check_document_existance(self):
        self.assertTrue(check_document_existance('10006'), True)

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name("10006"), "Аристарх Павлов")

    def test_get_all_doc_owners_names(self):
        my_set = ["Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов", 'Elon Musk']
        my_set = set(my_set)
        self.assertSetEqual(get_all_doc_owners_names(), my_set)

    def test_remove_doc_from_shelf(self):
        self.assertIsNone(remove_doc_from_shelf("10006"))

    def test_add_new_shelf(self):
        self.assertTupleEqual(add_new_shelf('11'), ('11', True))

    def test_append_doc_to_shelf(self):
        self.assertIsNone(append_doc_to_shelf('11', '3'))

    def test_delete_doc(self):
        self.assertIsNone(delete_doc("11"))

    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf("10006"), '2')

    def test_move_doc_to_shelf(self):
        self.assertIsNone(move_doc_to_shelf("10006", '2'))

    def test_show_document_info(self):
        dictionary = {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}
        self.assertDictEqual(show_document_info(dictionary), {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"})

    def test_show_all_docs_info(self):
        global x
        self.assertListEqual(show_all_docs_info(), x)

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('Diploma', '88005553535', 'Elon Musk', '1'), '1')

    def test_secretary_program_start(self):
        self.assertIsNone(secretary_program_start('q'))



if __name__ == '__main__':
    unittest.main()
