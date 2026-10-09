"""Small automated tests for the student search and persistence helpers."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import student_manager


class StudentManagerTests(unittest.TestCase):
    def test_find_student_by_id_is_case_insensitive(self):
        students = [
            {"id": "S101", "name": "Asha", "age": 20, "marks": 82}
        ]
        self.assertEqual(
            student_manager.find_student_by_id(students, "s101"),
            students[0],
        )

    def test_find_student_returns_none_when_missing(self):
        self.assertIsNone(
            student_manager.find_student_by_id([], "S999")
        )

    def test_save_and_load_students(self):
        sample = [{"id": "S101", "name": "Asha", "age": 20, "marks": 82}]
        with tempfile.TemporaryDirectory() as temporary_folder:
            temporary_file = Path(temporary_folder) / "students.json"
            with patch.object(student_manager, "DATA_FILE", temporary_file):
                self.assertTrue(student_manager.save_students(sample))
                self.assertEqual(student_manager.load_students(), sample)

    def test_empty_json_file_is_handled(self):
        with tempfile.TemporaryDirectory() as temporary_folder:
            temporary_file = Path(temporary_folder) / "students.json"
            temporary_file.write_text("[]", encoding="utf-8")
            with patch.object(student_manager, "DATA_FILE", temporary_file):
                self.assertEqual(student_manager.load_students(), [])


if __name__ == "__main__":
    unittest.main()
