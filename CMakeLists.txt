#---------------------------------------------------------------------------
# Copyright 2012 The Open Source Electronic Health Record Agent
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#---------------------------------------------------------------------------

configure_file("${CMAKE_CURRENT_SOURCE_DIR}/RAS/SetupTIUDocument.py.in" "${CMAKE_CURRENT_BINARY_DIR}/SetupTIUDocument.py")
configure_file("${CMAKE_CURRENT_SOURCE_DIR}/RAS/AddR1ACKeys.py.in" "${CMAKE_CURRENT_BINARY_DIR}/AddR1ACKeys.py")

make_directory("${CMAKE_CURRENT_BINARY_DIR}/Log")
execute_process(COMMAND ${PYTHON_EXECUTABLE} "${CMAKE_CURRENT_BINARY_DIR}/SetupTIUDocument.py")
execute_process(COMMAND ${PYTHON_EXECUTABLE} "${CMAKE_CURRENT_BINARY_DIR}/AddR1ACKeys.py")

option(AppCard_SIK "Use Sikuli to test the Appointment Card Web interface.  These scripts were created assuming that the Firefox browser is used.  Others can be used , but will have poor test results." OFF)
if(AppCard_SIK)
  
  # Find necessary programs: Firefox browser and Sikuli.
  find_program(BROWSER_EXECUTABLE firefox.exe DOC "Path to the web browser that has the Appointment Card login page as its start page.")
  find_program(SIKULI_EXECUTABLE Sikuli-IDE.bat DOC "Path to the Sikul-IDE.bat file" HINTS "C:/Program Files/Sikuli X/" "C:/Program Files (x86)/Sikuli X/" )
  
  
  #Glob for Sikuli folders in the 'Sikuli' directory
  file(GLOB testfiles ${CMAKE_CURRENT_SOURCE_DIR}/Sikuli/*.sikuli)
  foreach(testfile ${testfiles})
    get_filename_component(testfile_name "${testfile}" NAME_WE)
    if(${testfile_name} STREQUAL "libs")
      # Configure the libs.sikuli python and html to have the correct browser to open.
      configure_file("${CMAKE_CURRENT_SOURCE_DIR}/Sikuli/libs.sikuli/libs.py.in" "${CMAKE_CURRENT_SOURCE_DIR}/Sikuli/libs.sikuli/libs.py")
      configure_file("${CMAKE_CURRENT_SOURCE_DIR}/Sikuli/libs.sikuli/libs.html.in" "${CMAKE_CURRENT_SOURCE_DIR}/Sikuli/libs.sikuli/libs.html")
    else()
      # If not 'libs', then we make running the sikuli file a test.
      add_test(AppCard_SIK_${testfile_name} ${SIKULI_EXECUTABLE} -s -r "${testfile}")
    endif()
    
    # Set up test dependencies
    if(${testfile_name} STREQUAL "DeleteClinicSetup")
      set_property(TEST AppCard_SIK_${testfile_name} PROPERTY DEPENDS "AppCard_SIK_DeleteTemplate;AppCard_SIK_DeletePostcardText;AppCard_SIK_DeleteOverrideAddress;AppCard_SIK_InactivateClinic;AppCard_SIK_ReactivateClinic;AppCard_SIK_UpdateClinicAddress")
    elseif(${testfile_name} STREQUAL "DeleteTemplate")
      set_property(TEST AppCard_SIK_${testfile_name} PROPERTY DEPENDS AppCard_SIK_DetachTemplate)
    elseif(${testfile_name} STREQUAL "DeleteOverrideAddress")
      set_property(TEST AppCard_SIK_${testfile_name} PROPERTY DEPENDS AppCard_SIK_EditOverrideAddress)
    elseif(${testfile_name} STREQUAL "DeleteInactivationReason")
      set_property(TEST AppCard_SIK_${testfile_name} PROPERTY DEPENDS "AppCard_SIK_InactivateClinic;AppCard_SIK_ReactivateClinic")
    elseif(${testfile_name} STREQUAL "DeletePostcardText")
      set_property(TEST AppCard_SIK_${testfile_name} PROPERTY DEPENDS "AppCard_SIK_DetachTemplate")
    endif()
  endforeach()
endif()

option(AppCard_RAS "Test the Appointment Card Roll-and-Scroll interface" ON)
if(AppCard_RAS)

  if(NOT AppCard_SIK)
    configure_file("${CMAKE_CURRENT_SOURCE_DIR}/RAS/RASTemplateSetup.py.in" "${CMAKE_CURRENT_BINARY_DIR}/RAS/RASTemplateSetup.py")
    configure_file("${CMAKE_CURRENT_SOURCE_DIR}/RAS/ClinicEditSetup.py.in" "${CMAKE_CURRENT_BINARY_DIR}/RAS/ClinicEditSetup.py")
    
    execute_process(COMMAND ${PYTHON_EXECUTABLE} "${CMAKE_CURRENT_BINARY_DIR}/RAS/RASTemplateSetup.py")
    execute_process(COMMAND ${PYTHON_EXECUTABLE} "${CMAKE_CURRENT_BINARY_DIR}/RAS/ClinicEditSetup.py")
  endif()
  
  # Glob for *.py.in files in the 'RAS' Directory 
  file(GLOB testfiles ${CMAKE_CURRENT_SOURCE_DIR}/RAS/DISPLAY*.py.in)
  foreach(testfile ${testfiles})
    get_filename_component(testfile_name "${testfile}" NAME_WE)
    configure_file("${testfile}" "${CMAKE_CURRENT_BINARY_DIR}/AppCard_${testfile_name}.py")
    
    # Make a  test for each one. 
    add_test(AppCard_RAS_${testfile_name} ${PYTHON_EXECUTABLE} "${CMAKE_CURRENT_BINARY_DIR}/AppCard_${testfile_name}.py")
    
    if(${testfile_name} STREQUAL "DISPLAY4C-DeleteAllBlueBoxText")
      set_property(TEST AppCard_RAS_${testfile_name} PROPERTY DEPENDS "AppCard_RAS_DISPLAY4A-EditCrosswalkClinic")
    elseif(${testfile_name} STREQUAL "DISPLAY8E-EditNotifLtrPostSignatureCode")
          set_property(TEST AppCard_RAS_${testfile_name} PROPERTY DEPENDS "AppCard_RAS_DISPLAY8A-EditSiteParametesrforNotifLtrs")
    endif()
  endforeach()
endif()