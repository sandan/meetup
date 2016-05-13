
# coding: utf-8

# # Objects and Exceptions
# 
# In this talk we'll dive into python objects, inheritance, and exception handling. We'll apply these concepts to write an Exception Hierarchy.

# In[6]:

# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
    
# BaseException
# +-- SystemExit
# +-- KeyboardInterrupt
# +-- GeneratorExit
# +-- Exception
#      +-- StopIteration
#      +-- StopAsyncIteration
#      +-- ArithmeticError
#      |    +-- FloatingPointError
#      |    +-- OverflowError
#      |    +-- ZeroDivisionError
#      +-- AssertionError
#      +-- AttributeError
#      +-- BufferError
#      +-- EOFError
#      +-- ImportError
#      +-- LookupError
#      |    +-- IndexError
#      |    +-- KeyError
#      +-- MemoryError
#      +-- NameError
#      |    +-- UnboundLocalError
#      +-- OSError
#      |    +-- BlockingIOError
#      |    +-- ChildProcessError
#      |    +-- ConnectionError
#      |    |    +-- BrokenPipeError
#      |    |    +-- ConnectionAbortedError
#      |    |    +-- ConnectionRefusedError
#      |    |    +-- ConnectionResetError
#      |    +-- FileExistsError
#      |    +-- FileNotFoundError
#      |    +-- InterruptedError
#      |    +-- IsADirectoryError
#      |    +-- NotADirectoryError
#      |    +-- PermissionError
#      |    +-- ProcessLookupError
#      |    +-- TimeoutError
#      +-- ReferenceError
#      +-- RuntimeError
#      |    +-- NotImplementedError
#      |    +-- RecursionError
#      +-- SyntaxError
#      |    +-- IndentationError
#      |         +-- TabError
#      +-- SystemError
#      +-- TypeError
#      +-- ValueError
#      |    +-- UnicodeError
#      |         +-- UnicodeDecodeError
#      |         +-- UnicodeEncodeError
#      |         +-- UnicodeTranslateError
#      +-- Warning
#           +-- DeprecationWarning
#           +-- PendingDeprecationWarning
#           +-- RuntimeWarning
#           +-- SyntaxWarning
#           +-- UserWarning
#           +-- FutureWarning
#           +-- ImportWarning
#           +-- UnicodeWarning
#           +-- BytesWarning
#           +-- ResourceWarning


# In[7]:

#!/usr/bin/env python3
#--------------
# ErrorsExceptions.py
# https://docs.python.org/3/tutorial/errors.html
#--------------

t = Exception("RARWRRWRWRW", "123")
raise t


# In[8]:

#!/usr/bin/env python3

#--------------
# HandlingExceptions.py
#--------------

try:
    raise SyntaxError(['foo','bar'])           # force any exception
    
except SyntaxError as inst:                    # named instance
    print("syntax error! {}".format(inst.args))
    
except IOError:                                # anonymous
    print("unhandled io error")
    
except (UnicodeDecodeError, TypeError, NameError) as e:  # tuple
    
    if isinstance(e, UnicodeDecodeError):
        print("unicode decode error")
    elif issubclass(type(e), TypeError):
        print("type error")
    else:
        print('name error')
    
except:                                        # default
    print("Unexpected exception raised")
    raise        # bare raise will re-raise the exception thrown
    
else:                                          # optional else
    print("else: executes code if no exception is raised in try")
    
finally:                                       # optional finally
    print("finally: always executed last")
    
#Note: 
# You can only catch SyntaxError if it's thrown doing an eval or exec operation or raised
# You can nest try/except-else-finally blocks in any of the try/except/else/finally clauses
# At most one except clause will be executed per try/except-else-finally block
# An except clause will catch only exceptions thrown in the try clause (even indirectly)
# An exception matches if its class is a subclass of the specified exception(s)
# The first except clause that matches will be executed


# In[9]:

def push(q, item):
    raise Exception

def assertRaises(exception, func, *args):
    """
    returns True if func(args) raises exception else False
    """
    try:
        func(*args)        # push([],'arg')
    except exception as e:
        return True
    except:
        return False
    else:
        return False

print(assertRaises(Exception, push, [], 'arg'))


# In[10]:

# exception hierarchy example

# inheritance
class TeradataException(Exception):
    pass

class RetryableError(TeradataException):
    
    def f(self):
        print('RetryableError')

class SystemError(TeradataException):
    
    def f(self):
        print('SystemError')

class DBSError(RetryableError):
    
    # override
    def f(self):
        print('DBSError')

class PDEError(SystemError):
    
    # override
    def f(self):
        print('PDEError')
        
# multiple inheritance
class TestError(PDEError, DBSError):
    pass


# 
# 
# 
# 
# 
# 
# 
# 
# 
# ![alt text](./ObjectsExceptions.png 'Exception Hierarchy')

# In[11]:

# exception resolution
try:
    raise TestError()
    
except RetryableError as e:
    e.f()

except TeradataException as tde:
    print('TeradataException')
    
except:
    print('Unhandled')
    
else:
    print('No exception thrown')


# In[4]:

# method resolution
TestError.mro()


# In[5]:

help(TestError.mro)

# The class that comes first in the list has precedence over classes that come later

