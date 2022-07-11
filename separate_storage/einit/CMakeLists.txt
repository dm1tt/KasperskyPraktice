project (einit)

# Toolkit for working with NK parser.
include (platform/image)

# Set compilation flags.
project_header_default ("STANDARD_GNU_11:YES" "STRICT_WARNINGS:NO")

# Define an ENTITIES variable with a list of entities.
set (ENTITIES UserManager VfsUser)

# Create image of ext2 file system with two partitions, and copy there required files.
add_custom_target (
                hdd.img
                COMMAND ${CMAKE_COMMAND} -E make_directory
                ${CMAKE_BINARY_DIR}/hdd_part1
                COMMAND ${CMAKE_COMMAND} -E make_directory
                ${CMAKE_BINARY_DIR}/hdd_part2
                COMMAND ${CMAKE_COMMAND} -E make_directory
                ${CMAKE_BINARY_DIR}/hdd_part3
                COMMAND ${CMAKE_COMMAND} -E copy
                ${CMAKE_SOURCE_DIR}/resources/files/userlist.txt ${CMAKE_BINARY_DIR}/hdd_part2
                COMMAND ${KL_SDK_ROOT_PATH}/common/prepare_hdd_img.sh   -s 128 -%1 10 -%2 45 -%3 45 
                                                                        -p1 ${CMAKE_BINARY_DIR}/hdd_part1 
                                                                        -p2 ${CMAKE_BINARY_DIR}/hdd_part2 
                                                                        -p3 ${CMAKE_BINARY_DIR}/hdd_part3
                                                                        -img hdd.img)

set (QEMU_DEPENDENCIES hdd.img)

if ("${CMAKE_SYSTEM_PROCESSOR}" MATCHES "arm|aarch64")
    set(SECURITY_PSL_FILE src/security_arm.psl)
    # Connect a package which imports components to work with SD-card.
    find_package (sdcard REQUIRED)
    include_directories (${sdcard_INCLUDE})

    # We need SDCARD driver to be connected with our implementation of VFS

    # We need SDCARD driver to be connected with our implementation of VFS
    set_target_properties (VfsUser PROPERTIES ${blkdev_ENTITY}_REPLACEMENT ${sdcard_ENTITY})

    set (QEMU_FLAGS "-sd hdd.img")
    set (QEMU_DEPENDENCIES hdd.img)
else ()
    set (SECURITY_PSL_FILE src/security_x86.psl)
    # Connect a package which imports components to work with ATA-device.
    find_package (ata REQUIRED)
    include_directories (${ata_INCLUDE})

    # We need ATA driver to be connected with our implementation of VFS.

    # We need ATA driver to be connected with our implementation of VFS.
    set_target_properties (VfsUser PROPERTIES ${blkdev_ENTITY}_REPLACEMENT ${ata_ENTITY})

    set (
        QEMU_FLAGS "-device ahci,id=ahci \
                    -drive id=disk1,file=hdd.img,if=none \
                    -device ide-drive,drive=disk1,bus=ahci.0")
endif ()

# The KasperskyOS image for the hardware platform.
build_kos_hw_image (
                    kos-image
                    EINIT_ENTITY EinitHw
                    CONNECTIONS_CFG "src/init.yaml.in"
                    SECURITY_PSL  ${SECURITY_PSL_FILE}
                    IMAGE_FILES ${ENTITIES})

# The KasperskyOS image for QEMU with emulation targets (sim, gdbsim, gdb).
build_kos_qemu_image (
                    kos-qemu-image
                    EINIT_ENTITY EinitQemu
                    CONNECTIONS_CFG "src/init.yaml.in"
                    SECURITY_PSL  ${SECURITY_PSL_FILE}
                    IMAGE_FILES ${ENTITIES}
                    QEMU_FLAGS "${QEMU_FLAGS}"
                    QEMU_DEPENDENCIES "${QEMU_DEPENDENCIES}")
                      
