import unittest
import os
import tempfile
import json
from flask import Flask, session
import sys
module_path = os.path.abspath("D://code_edit//CodeWalker//run_code.py")
if module_path not in sys.path:
    sys.path.append(module_path)

class FileOperationTestCase(unittest.TestCase):
    def setUp(self):
        # Create a temporary work directory for testing
        self.test_dir = tempfile.mkdtemp()
        
        # Set up Flask app with a mock session
        self.app = Flask(__name__)
        self.app.secret_key = 'test_secret_key'
        self.app.config['TEST_WORK_DIR'] = self.test_dir
        SetFunctions(self.app)
        self.client = self.app.test_client()
        
        # Add a mock session handler
        @self.app.before_request
        def add_mock_session():
            session['userName'] = 'testuser'

    def tearDown(self):
        # Remove temporary directory and its contents
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_get_file_list(self):
        # Create some test files
        test_files = ['file1.txt', 'file2.py', 'file3.json']
        for file_name in test_files:
            with open(os.path.join(self.test_dir, file_name), 'w') as f:
                f.write('test content')

        response = self.client.post('/getFileList')
        self.assertEqual(response.status_code, 200)

        file_list = json.loads(response.data)
        file_names = [file['fileName'] for file in file_list]
        self.assertCountEqual(file_names, test_files)

    def test_get_file(self):
        # Create a test file
        test_file = 'test.txt'
        test_content = 'This is a test file.'
        with open(os.path.join(self.test_dir, test_file), 'w') as f:
            f.write(test_content)

        response = self.client.post('/getFile', data={'fileName': test_file})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), test_content)

    def test_delete_file(self):
        # Create a test file
        test_file = 'delete_me.txt'
        with open(os.path.join(self.test_dir, test_file), 'w') as f:
            f.write('Delete me!')

        response = self.client.post('/deleteFile', data={'fileName': test_file})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(os.path.exists(os.path.join(self.test_dir, test_file)))

    def test_save_code(self):
        # Test saving a new file
        test_file = 'new_file.py'
        test_code = 'print("Hello, world!")'
        response = self.client.post('/saveCode', data={
            'fileName': test_file,
            'code': test_code,
            'overWrite': 'false'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'success')
        
        with open(os.path.join(self.test_dir, test_file), 'r') as f:
            self.assertEqual(f.read(), test_code)

        # Test attempting to overwrite without permission
        response = self.client.post('/saveCode', data={
            'fileName': test_file,
            'code': 'print("Overwrite attempt")',
            'overWrite': 'false'
        })
        self.assertEqual(response.data.decode('utf-8'), 'file exists')

    def test_run_code(self):
        # Create a Python script
        test_file = 'test_script.py'
        test_code = 'print("Running test script.")'
        with open(os.path.join(self.test_dir, test_file), 'w') as f:
            f.write(test_code)

        response = self.client.post('/runCode', data={'fileName': test_file})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Running test script.', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
