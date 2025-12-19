*** Settings ***
Library    pywinautoLibrary    timeout=10
Test Teardown    close_all_applications

*** Test Cases ***
Open Notepad and Write Text
    [Documentation]    Test opening Notepad, writing text, and closing it.
    Open Application    notepad.exe
    Wait For Window    无标题 - Notepad
    Click Element    Edit
    Type Text    Hello, Robot Framework!
    Close Application

Open Multiple Applications
    [Documentation]    Test opening multiple applications and switching between them.
    ${alias1}=    Open Application    notepad.exe
    Wait For Window    无标题 - Notepad
    ${alias2}=    Open Application    notepad.exe
    Wait For Window    无标题 - Notepad
    Switch Application    ${alias1}
    Click Element    Edit
    Type Text    First Notepad
    Switch Application    ${alias2}
    Click Element    Edit
    Type Text    Second Notepad
    Close All Applications

Connect To Existing Application
    [Documentation]    Test connecting to an existing Notepad instance.
    # First, open Notepad manually or using another keyword
    Open Application    notepad.exe
    Wait For Window    无标题 - Notepad
    # Get the process ID of the current Notepad instance
    ${process_id}=    Get Current Process ID
    # Close the application
    Close Application
    # Reconnect to the application using the process ID
    Connect To Application    process_id=${process_id}
    Wait For Window    无标题 - Notepad
    Close Application

*** Keywords ***
get_current_process_id
    [Documentation]    Get the process ID of the current application.
    # Note: This keyword assumes that pywinauto's Application object has a process attribute
    ${app}=    get_current_application
    ${process_id}=    Evaluate    ${app}.process
    RETURN    ${process_id}

get_current_application
    [Documentation]    Get the current application instance.
    ${ctx}=    Get Library Instance    pywinautoLibrary
    RETURN    ${ctx.app}
