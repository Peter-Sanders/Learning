#!/bin/bash 

file=${1:-"foo"} 
out=${2:-"out.log"}
compile=1

function compile_file {
	file=$1
	out=$2
	filearr=(${file//./ })
	filename=${filearr[0]}
	fileext=${filearr[1]}  
	filedirarr=(${filename//// })
	filedirdir=${filedirarr[0]}
	filedirname=${filedirarr[1]}
	fileexename="$filedirname"."$fileext"


	case $fileext in 
		c)
			gcc $file -o $filename 
			./$filename > $out
			;;
		cpp)
			g++ $file -o $filename 
			./$filename > $out
			;;
		py)
			python3 $file > $out
			;;
		java)n
			cd $filedirdir 
			javac $fileexename
			java $filedirname > ../$out
			cd ..
			;;
		cbl)
			cd $filedirdir 
			cobc -free -x -o $filedirname $fileexename
			./$filedirname > ../$out
			cd ..
			;;
		asm)
			nasm -felf64 $file && ld $filedirdir/$filedirname.o -o $filedirdir/$filedirname && ./$filedirdir/$filedirname > $out
			echo $? > $out
			;;
		rs)
			cd $filedirdir
			rustc $fileexename  
			./$filedirname > ../$out
			cd ..
			;;
    go)
      cd $filedirdir/$filedirname
      go build .
      go run . > ../../$out 
      cd ../.. 
      ;;
    zig)
      cd $filedirdir/$filedirname
      zig build run > ../../$out
      cd ../..
      ;;
		*)
		echo "extension $fileext not supported" > $out
			;;
	esac
}

# check if we have file arg provided
if [ $file = foo ]; then
	echo "no file provided" > $out
	compile=0
fi

# check if provided file exists
if ! test -f $file; then 
	echo "file does not exist" > $out 
	compile=0
fi 

# compile the file
if [ $compile = 1 ]; then 
	compile_file $file $out
fi 


# read the output
cat $out

