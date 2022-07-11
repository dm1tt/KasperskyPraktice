#include <sys/mount.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>

const char *MountPath = "/c";
const char *FileSystemType = "ext2";

#define MAX_FS_PATH_SIZE 1024

int MountFileSystem(unsigned partitionId)
{
    char fs_path[MAX_FS_PATH_SIZE];

    if (mkdir(MountPath, S_IRWXU | S_IRWXG | S_IRWXO))
    {
        fprintf(
            stderr,
            "Failed to create \"%s\" dir. Error %d: \"%s\"\n",
            MountPath,
            errno,
            strerror(errno));
        return EXIT_FAILURE;
    }

    snprintf(fs_path, MAX_FS_PATH_SIZE, "%s0,%d", BLKDEV, partitionId);

    if (mount(fs_path, MountPath, FileSystemType, 0, ""))
    {
        fprintf(
            stderr,
            "Failed to mount %s, %s, %s. Error %d: \"%s\"\n",
            fs_path,
            MountPath,
            FileSystemType,
            errno,
            strerror(errno));
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}