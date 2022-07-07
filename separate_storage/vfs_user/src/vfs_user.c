#include <stdlib.h>
#include <errno.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <sys/mount.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include "common.h"

#define _VFS_SERVER_INTERFACE
#include <vfs/basic.h>

/* Dispatch to the main thread. */
static _vfs_server_thread_routine_t threadRoutine = NULL;
static void *threadRoutineArg = NULL;

static const char EntityName[] = "VfsUser";

/* This function must be defined to dispatch IFilesyste interface methods on the main thread. */
void _vfs_server_set_main_thread_routine(_vfs_server_thread_routine_t func, void *arg)
{
    threadRoutine = func;
    threadRoutineArg = arg;
}

int main(void)
{
    if (MountFileSystem(USER_PARTITION) != EXIT_SUCCESS)
    {
        fprintf(
            stderr,
            "[%s][Error]: can`t mount user partition!"
            " %s is terminating!\n",
            EntityName,
            EntityName);
        return EXIT_FAILURE;
    }

    if (threadRoutine != NULL)
    {
        (*threadRoutine)(threadRoutineArg);
    }
    else
    {
        fprintf(
            stderr,
            "[%s][Error]: threadRoutine pointer is null! %s is terminating!\n",
            EntityName,
            EntityName);
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}