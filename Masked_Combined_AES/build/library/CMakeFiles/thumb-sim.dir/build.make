# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/build

# Include any dependencies generated for this target.
include library/CMakeFiles/thumb-sim.dir/depend.make

# Include the progress variables for this target.
include library/CMakeFiles/thumb-sim.dir/progress.make

# Include the compile flags for this target's objects.
include library/CMakeFiles/thumb-sim.dir/flags.make

library/CMakeFiles/thumb-sim.dir/main.cpp.o: library/CMakeFiles/thumb-sim.dir/flags.make
library/CMakeFiles/thumb-sim.dir/main.cpp.o: ../library/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object library/CMakeFiles/thumb-sim.dir/main.cpp.o"
	cd /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/build/library && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/thumb-sim.dir/main.cpp.o -c /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/library/main.cpp

library/CMakeFiles/thumb-sim.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/thumb-sim.dir/main.cpp.i"
	cd /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/build/library && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/library/main.cpp > CMakeFiles/thumb-sim.dir/main.cpp.i

library/CMakeFiles/thumb-sim.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/thumb-sim.dir/main.cpp.s"
	cd /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/build/library && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/library/main.cpp -o CMakeFiles/thumb-sim.dir/main.cpp.s

# Object files for target thumb-sim
thumb__sim_OBJECTS = \
"CMakeFiles/thumb-sim.dir/main.cpp.o"

# External object files for target thumb-sim
thumb__sim_EXTERNAL_OBJECTS =

bin/thumb-sim: library/CMakeFiles/thumb-sim.dir/main.cpp.o
bin/thumb-sim: library/CMakeFiles/thumb-sim.dir/build.make
bin/thumb-sim: lib/libthumb-sim.a
bin/thumb-sim: library/CMakeFiles/thumb-sim.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../bin/thumb-sim"
	cd /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/build/library && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/thumb-sim.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
library/CMakeFiles/thumb-sim.dir/build: bin/thumb-sim

.PHONY : library/CMakeFiles/thumb-sim.dir/build

library/CMakeFiles/thumb-sim.dir/clean:
	cd /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/build/library && $(CMAKE_COMMAND) -P CMakeFiles/thumb-sim.dir/cmake_clean.cmake
.PHONY : library/CMakeFiles/thumb-sim.dir/clean

library/CMakeFiles/thumb-sim.dir/depend:
	cd /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1 /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/library /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/build /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/build/library /home/IWAS/mahpar/Documents/daily_work/027OCT/1r_1bS_1sh_0k_1/build/library/CMakeFiles/thumb-sim.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : library/CMakeFiles/thumb-sim.dir/depend
