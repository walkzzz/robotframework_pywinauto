*** Settings ***
Library    pywinautoLibrary    timeout=10
Test Teardown    close_all_applications

*** Test Cases ***
Calculator Addition Test
    [Documentation]    Test addition functionality in Calculator.
    Open Application    calc.exe
    Wait For Window    Calculator
    Click Element    Seven
    Click Element    Plus
    Click Element    Three
    Click Element    Equals
    Wait Until Element Contains Text    ResultLabel    10
    Close Application

Calculator Subtraction Test
    [Documentation]    Test subtraction functionality in Calculator.
    Open Application    calc.exe
    Wait For Window    Calculator
    Click Element    Nine
    Click Element    Minus
    Click Element    Five
    Click Element    Equals
    Wait Until Element Contains Text    ResultLabel    4
    Close Application

Calculator Multiplication Test
    [Documentation]    Test multiplication functionality in Calculator.
    Open Application    calc.exe
    Wait For Window    Calculator
    Click Element    Four
    Click Element    Multiply by
    Click Element    Six
    Click Element    Equals
    Wait Until Element Contains Text    ResultLabel    24
    Close Application

Calculator Division Test
    [Documentation]    Test division functionality in Calculator.
    Open Application    calc.exe
    Wait For Window    Calculator
    Click Element    Eight
    Click Element    Divide by
    Click Element    Two
    Click Element    Equals
    Wait Until Element Contains Text    ResultLabel    4
    Close Application
