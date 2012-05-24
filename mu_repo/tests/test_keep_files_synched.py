'''
Created on 20/05/2012

@author: Fabio Zadrozny
'''
import unittest
import os.path
import shutil
from mu_repo import keep_files_synched
from mu_repo.rmtree import RmTree


#===================================================================================================
# Test
#===================================================================================================
class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.clear()


    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.clear()


    def clear(self):
        if os.path.exists('.test_temp_dir'):
            RmTree('.test_temp_dir')


    def read(self, file2):
        with open(file2, 'r') as f:
            return f.read()


    def testKeepFilesSynchedStruct(self):
        os.makedirs('.test_temp_dir')
        file1 = os.path.join('.test_temp_dir', 'f1')
        file2 = os.path.join('.test_temp_dir', 'f2')
        with open(file1, 'w') as f:
            f.write('initial')
        shutil.copyfile(file1, file2)
        s = keep_files_synched._KeepInSyncStruct(file1, file2)
        self.assertEqual('initial', self.read(file2))

        with open(file1, 'w') as f:
            f.write('second')
        s.Sync()
        self.assertEqual('second', self.read(file2))

        with open(file2, 'w') as f:
            f.write('third')
        s.Sync()
        self.assertEqual('third', self.read(file1))


    def testKeepFilesSynched(self):
        os.makedirs('.test_temp_dir')
        file1 = os.path.join('.test_temp_dir', 'f1')
        file2 = os.path.join('.test_temp_dir', 'f2')
        with open(file1, 'w') as f:
            f.write('initial')
        shutil.copyfile(file1, file2)
        keep_files_synched.KeepInSync(file1, file2)

        self.assertEqual('initial', self.read(file2))
        with open(file1, 'w') as f:
            f.write('second')
        keep_files_synched.StopSyncs()
        self.assertEqual('second', self.read(file2))




#===================================================================================================
# ain
#===================================================================================================
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testKeepFilesSynched']
    unittest.main()