# Learning

A repository to house my progress learning new languages/frameworks and improve my skills with ones I already know.

The initial commits are based around the 2023 advent of code challenges. Text files containing the challenge data are stored in the "advent-storage" directory.

Each language has its own sub directory; "learning-cpp" contains c++ files.

The "compile.sh" file at the top level of the repo is used to compile and run each sub file. It expects at minimum the input file and has an optional arg to specify an alternate output file. The default output is "out.log" at the top level of the repo. "compile.sh" dumps the output of each program (and in the case of assembly, also the exit code) into "out.log" and reads it back to the terminal.

Go is where this paradigm starts to get a little weird
The folder "learning-go" contains several sub folders, each containing a separate go module. The sub folder name is the same as the .go filename is the same as the module name. When cd'd into the subfolder, go init mod {subfolder} is ran


ex: ./compile.sh learning-rust/advent-24-1.rs 
ex: ./compile.sh learning-c/hello-world.c c-output.log
ex: ./compile.sh learning-go/hello-world/hello-world.go

