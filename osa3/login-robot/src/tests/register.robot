*** Settings ***
Resource  resource.robot
Test Setup  Input New Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Credentials  kalle  kalle123
    Output Should Contain  User already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username must be at least 3 characters long

Register With Long Enough But Invalid Username And Valid Password
    Input Credentials  Kalle1  kalle123
    Output Should Contain  Username must contain only lowercase letters

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kal123
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekal
    Output Should Contain  Password must contain numbers or special characters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
