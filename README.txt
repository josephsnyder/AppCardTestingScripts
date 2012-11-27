The Appointment Card test suite is an expansion to the OSEHRA Automated Testing suite.
To run the Appointment Card tests, you need to first have a configured checkout of the OSEHRA Automated Testing following the instructions here:
    http://www.osehra.org/wiki/setting-testing-environment
   
After you have a checkout, you need to append one line to the end of the CMakeLists.txt in the OSEHRA-Automated-Testing folder.  The following line should be appended to the bottom of the file:

    add_subdirectory("C:/path/to/source/PostCardTesting" "C:/path/to/some/binary/")

This line will instruct CMake to find this folder and process the CMakeLists.txt that is held within.  The binary folder isn't required to be in the build tree.  

SIKULI Notes:

If the CSP side of the Appointment Card submission is to be tested, we have some assumptions as to the environment that it uses.  We assume:

- Firefox is used as the browser.  Other browsers can be used, but the tests will likely not complete successfully.
- When the browser window opens, it is full screened.
- The login page is the home page of the browser.
- Form completion has been turned off 
    + Options -> Privacy
    + Change 'Remember History' to 'Use Custom Settings'
    + Uncheck the 'Remember search and form history' checkbox