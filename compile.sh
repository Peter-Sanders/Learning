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

	if [ $fileext = c ]; then
		gcc $file -o $filename
		./$filename > $out
	elif [ $fileext = cpp ]; then 
		g++ $file -o $filename 
		./$filename > $out
	elif [ $fileext = py ]; then 
		python3 $file > $out
	elif [ $fileext = java ]; then
		cd $filedirdir 
		javac $fileexename
		java $filedirname > ../$out
		cd ..
	elif [ $fileext = cbl ]; then
		cd $filedirdir 
		cobc -free -x -o $filedirname $fileexename
		./$filedirname > ../$out
		cd ..
	elif [ $fileext = asm ]; then 
		nasm -felf64 $file && ld $filedirdir/$filedirname.o -o $filedirdir/$filedirname && ./$filedirdir/$filedirname > $out
		echo $? >> $out
	elif [ $fileext = rs ]; then 
		cd $filedirdir
		rustc $fileexename  
		./$filedirname > ../$out
		cd ..
	else 
		echo "extension $fileext not supported" > $out
	fi
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

