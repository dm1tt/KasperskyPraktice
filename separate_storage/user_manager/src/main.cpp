#include "user_manager.h"
#include "file_names.h"

#include <iostream>
#include <fstream>
#include <time.h>

const std::string Tag = "[UserManager] ";
const std::string ErrorTag = "[Error] ";

void UserListOutput(const UserList& users)
{
    for(const auto& User : users)
    {
        std::cout << Tag << "User name: " << User << std::endl;
    }
}

void OpenUnavailableFile(const std::string &fileName)
{
    std::cout << Tag << "Try to read unavailable file '" << fileName << "'" << std::endl;

    std::ifstream inpFile;
    inpFile.open(fileName);
    if (!inpFile.is_open())
    {
        std::cout << Tag << "Unable to open the '" << fileName << "' file. It is correct behaviour." << std::endl;
    }
    else
    {
        std::cout << Tag << ErrorTag << "The '" << fileName << "' fileis open. It is not correct behaviour." << std::endl;
    }
}

int main(int argc, char* argv[])
{
    try
    {
        UserManager users;

        // Read the file we have access to.
        std::cout << Tag << "Try to read '" << UserListFileName << "' file" << std::endl;
        if (!users.Read(UserListFileName))
        {
               std::cout << Tag << ErrorTag << "Unable to read file: '" << UserListFileName << "'" << std::endl;
        }
        else
        {
            std::cout << Tag << "Success" << std::endl;
            UserListOutput(users.Get());
        }

        // Trying to read a file we do not have access to.
    }
    catch(std::exception& ex)
    {
        std::cout << Tag << ErrorTag << ex.what() << std::endl;
        return EXIT_FAILURE;
    }
    
    return EXIT_SUCCESS;
}
