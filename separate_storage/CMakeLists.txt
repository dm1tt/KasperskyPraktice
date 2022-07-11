cmake_minimum_required (VERSION 3.12)

project(separateStorage)
# Initialize the CMake library for the KasperskyOS SDK.
include (platform)
initialize_platform ()

# Connect artifact installation functions.
include (platform/install)

include (platform/nk)
nk_build_edl_files (separate_storage_user_manager NK_MODULE "separate_storage" EDL "resources/edl/UserManager.edl")
nk_build_edl_files (separate_storage_vfs_user  NK_MODULE "separate_storage" EDL "resources/edl/VfsUser.edl")

# Connect a package which imports components
# to work with the virtual file system.
find_package (vfs REQUIRED COMPONENTS FS_LIB CLIENT_LIB SERVER_LIB)
include_directories (${vfs_INCLUDE})

# Connect a package that imports components 
# to work with the ext2/ext3/ext4 file systems.
find_package (LWEXT4 REQUIRED)
include_directories (${LWEXT4_INCLUDE})

# Attach a directory with a header containing file name definitions.
include_directories (common)

add_subdirectory (user_manager)
add_subdirectory (vfs_user)

# Binary image of the KasperskyOS.
add_subdirectory (einit)
