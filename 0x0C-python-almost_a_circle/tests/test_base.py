import unittest
from models.base import Base, Rectangle


class TestBase(unittest.TestCase):
    def test_create(self):
        # Test creating instances using the create() method
        dictionary = {"id": 1, "width": 5, "height": 10}
        obj = Rectangle.create(**dictionary)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 10)

    def test_to_json_string(self):
        # Test converting a list of dictionaries to a JSON string
        dictionaries = [{"id": 1, "width": 5, "height": 10}, {"id": 2, "width": 3, "height": 7}]
        json_string = Base.to_json_string(dictionaries)
        self.assertEqual(json_string, '[{"id": 1, "width": 5, "height": 10}, {"id": 2, "width": 3, "height": 7}]')

    def test_from_json_string(self):
        # Test converting a JSON string to a list of dictionaries
        json_string = '[{"id": 1, "width": 5, "height": 10}, {"id": 2, "width": 3, "height": 7}]'
        dictionaries = Base.from_json_string(json_string)
        self.assertEqual(len(dictionaries), 2)
        self.assertEqual(dictionaries[0]["id"], 1)
        self.assertEqual(dictionaries[1]["height"], 7)

    def test_save_to_file(self):
        # Test saving instances to a file
        # Create a list of Rectangle instances
        rectangles = [Rectangle(1, 5, 10), Rectangle(2, 3, 7)]
        # Save the list to a file
        Rectangle.save_to_file(rectangles)

        # Load the instances from the file
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(loaded_rectangles[0].id, 1)
        self.assertEqual(loaded_rectangles[0].width, 5)
        self.assertEqual(loaded_rectangles[0].height, 10)
        self.assertEqual(loaded_rectangles[1].id, 2)
        self.assertEqual(loaded_rectangles[1].width, 3)
        self.assertEqual(loaded_rectangles[1].height, 7)


if __name__ == "__main__":
    unittest.main()
