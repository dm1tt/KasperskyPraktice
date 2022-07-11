#include "user_manager.h"

#include <iostream>
#include <fstream>
#include <string>

bool UserManager::Read(const std::string& userListFileName)
{
    std::ifstream userListFile;

    userListFile.open(userListFileName);
    if (!userListFile.is_open())
    {
        return false;
    }

    for (std::string userName; userListFile >> userName;)
    {
        m_userList.push_back(userName);
    }

    userListFile.close();

    return m_userList.size() > 0;
}