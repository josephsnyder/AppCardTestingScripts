The Appointment Card test suite is an expansion to the OSEHRA Automated Testing suite.
To run the Appointment Card tests, you need to first have a configured checkout of the OSEHRA Automated Testing following the instructions here:
    http://www.osehra.org/wiki/setting-testing-environment
   
After you have a checkout, you need to append one line to the end of the CMakeLists.txt in the OSEHRA-Automated-Testing folder.  The following line should be appended to the bottom of the file:

    add_subdirectory("C:/path/to/source/PostCardTesting" "C:/path/to/some/binary/")

This line will instruct CMake to find this folder and process the CMakeLists.txt that is held within.  The binary folder isn't required to be in the build tree.  

Selenium Notes:

This testing uses the Python implementation of Selenium to test the CSP page aspect of the Appointment Card software.  It will need to be installed within Python prior to running the tests:

The chosen method of installation is via the "easy_install" program, which is an installer for Python packages not in the main distribution.  The "easy_install" setup is part of the setuptools 
(http://pypi.python.org/pypi/setuptools) package.

After installing the setuptools package, you will find the easy_install executable in the Scripts/ directory of your python installation.  Selenium will be installed via the command:

    $ easy_install selenium

A simple way to check that the installation was a success is to run the 'python' command to get the environment and try to import selenium.  An example follows:

  $ python
  Python 2.7.2 (default, Jun 12 2011, 15:08:59) [MSC v.1500 32 bit (Intel)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import selenium
  >>>

No return signifies that the import was successful.  

If the CSP side of the Appointment Card submission is to be tested, we have some assumptions as to the environment that it uses.  We assume:

- Firefox is used as the browser.  Other browsers can be used, but the tests will likely not complete successfully.
- Form completion has been turned off 
    + Options -> Privacy
    + Change 'Remember History' to 'Use Custom Settings'
    + Uncheck the 'Remember search and form history' checkbox