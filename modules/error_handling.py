######################## Error Handling #########################
#
#
# x = int(input("Please enter a number: "))
# y = int(input("Please enter another number: "))

# try:
#     result = x / y
#     print(result)
# except:
#     print("Something went wrong!")
#     print("Please try again")


# print ("Goodybe!")
# ---------------------------------------------------------------
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         y = int(input("Please enter another number: "))
#         result = x / y
#         print(result)
#         break
#     except:
#         print("Something went wrong!")
#         user_response = input("Do you want to continue? (yes/no): ")
#         if user_response == "No":
#             break


#     print ("Goodybe!")
# ---------------------------------------------------------------
# try:
#     x = int(input("Please enter a number: "))
#     y = int(input("Please enter another number: "))
#     result = x / y
#     print(result)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("You must enter a valid number!")
# except:
#     print("Something went wrong!")


# print ("Goodybe!")
# ---------------------------------------------------------------
from builtins import WindowsError


try:
    x = int(input("Please enter a number: "))
    y = int(input("Please enter another number: "))
    result = x / y
    print(result)
except ArithmeticError:     # Errors with math operations
    pass
except AssertionError:      # Errors with assert statements
    pass
except AttributeError:      # lst.delete()  >>> NOT correct
    pass
except BufferError:         # ERROR on Memory!
    pass
except BlockingIOError:     # Error on input/output
    pass
except ConnectionError:
    pass
except ConnectionAbortedError:
    pass
except ConnectionRefusedError:
    pass
except ConnectionResetError:
    pass
# ------------------------------
except EOFError:            # End of File Error
    pass
except EnvironmentError:
    pass
except FileExistsError:
    pass
except FileNotFoundError:
    pass
except FloatingPointError:  # 19.24
    pass
except ImportError:
    pass
except IndentationError:
    pass
except IndexError:          # Incorrect index of a list
    pass
except InterruptedError:
    pass
except IOError:             # Input/Output Error
    pass
except KeyError:            # Incorrect key in a dict
    pass
# ------------------------------
except MemoryError:         # Memeory is full
    pass
except ModuleNotFoundError:
    pass
except NameError:           # x = 12 >> print(a) XX
    pass
except NotADirectoryError:
    pass
except OSError:
    pass
except OverflowError:       # Too large to be shown
    pass
except RuntimeError:
    pass
except IndexError:
    pass
except StopIteration:       # related to generators
    pass
except SystemError:         # Internal error in python
    pass
# ------------------------------
except TabError:
    pass
except TimeoutError:
    pass
except TypeError:           # Incorrect type of argument
    pass
except UnicodeError:
    pass
except UnicodeEncodeError:
    pass
except UnicodeDecodeError:
    pass
except ValueError:          # Incorrect value of argument
    pass
except WindowsError:        # I/O Error on Windows
    pass
except ZeroDivisionError:
    pass    