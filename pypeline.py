'''
Copyright (C) 2011 Jesus Leganes "piranna", piranna@gmail.com

This module is part of pypeline and is released under the BSD License:
http://www.opensource.org/licenses/bsd-license.php.

Created on 15/10/2011

@author: piranna
'''

from types import GeneratorType


def vectorizable(func):
    """Decorator that allow vectorization on a callable object"""

    def wrapper(stream):
        try:
            return [func(data) for data in stream]
        except TypeError:
            return func(stream)

    return wrapper


class Pipeline(list):
    """Pipe to content filters and process them sequentially

    This pipe allow to content filters inside it and process them sequentially
    using the output data of one of them as the input data of the next one.
    Having the same calling restrictions that the filters, it's easy to use it
    inside anothers pipeline objects as if it were a simple filter.
    """

    def __call__(self, stream):
        """Run the pipeline

        Return a static (non generator) version of the result
        """

        # Run the stream over all the filters on the pipeline
        for filt in self:
            stream = filt(stream)

        # If last filter return a generator, staticalize it inside a list
        if isinstance(stream, GeneratorType):
            return list(stream)
        return stream


class Tee(set):
    """Pipe that split the data stream to several pipes"""

    def __call__(self, stream):
        for data in stream:



            while self._toSend:
                self._toSend.pop()(data)