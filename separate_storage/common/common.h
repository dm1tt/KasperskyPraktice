/* © 2021 AO Kaspersky Lab */
#ifndef SEPARATE_STORAGE_COMMON_H
#define SEPARATE_STORAGE_COMMON_H

#define USER_PARTITION 1U
#define CERTIFICATE_PARTITION 2U

int MountFileSystem(unsigned partitionId);

#endif