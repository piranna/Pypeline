'''
Created on 16/10/2011

@author: piranna
'''
import unittest

from pypeline import Pipeline, vectorizable


class Test(unittest.TestCase):


    def testPipeline(self):
        """Test for `Pipeline` pipe"""

        # Dumb filters for testing
        def mult2(stream):
            """Dumb filter that multiply stream data by two"""
            for data in stream:
                yield data*2

        def add3(stream):
            """Dumb filter that add three to stream data"""
            for data in stream:
                yield data+3

        # Create pipeline
        pipeline = Pipeline()
        pipeline.append(mult2)
        pipeline.append(add3)

        # Exec pipeline using xrange iterator as input data
        result = pipeline(xrange(3))

        # Check pipeline result
        self.assertListEqual(result, [3,5,7])


    def testVectorizable_stream(self):
        """Test for `vectorizable` decorator"""

        # Dumb filters for testing
        @vectorizable
        def mult2(data):
            """Dumb filter that multiply data by two"""
            return data*2

        @vectorizable
        def add3(data):
            """Dumb filter that add three to data"""
            return data+3

        # Create pipeline
        pipeline = Pipeline()
        pipeline.append(mult2)
        pipeline.append(add3)

        # Exec pipeline using xrange iterator as input data
        result = pipeline(xrange(3))

        # Check pipeline result
        self.assertListEqual(result, [3,5,7])


    def testVectorizable_data(self):
        """Test for `vectorizable` decorator"""

        # Dumb filters for testing
        @vectorizable
        def mult2(data):
            """Dumb filter that multiply data by two"""
            return data*2

        @vectorizable
        def add3(data):
            """Dumb filter that add three to data"""
            return data+3

        # Create pipeline
        pipeline = Pipeline()
        pipeline.append(mult2)
        pipeline.append(add3)

        # Exec pipeline using xrange iterator as input data
        result = pipeline(3)

        # Check pipeline result
        self.assertEqual(result, 9)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()