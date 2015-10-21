#/bin/bash
name=`basename $0`
if [ $# -lt 2 ] ;then
	echo Usage: $name [keyword list] sourcefile
	exit 1
fi
if [ -f ${!#} ];then	#can not use ${$#}
	#echo Processing...
	#generate output file
	output=''
	script=''
	for (( i=1;i<$#;i++ )); do
		output=$output${!i}
		script=$script\/${!i}\/p\;
		script=$script\/${!i}\/b\;
	done
	#echo $output
	#echo $script
	script=\{$script\}
	sed -n -e $script ${!#}
else
	echo $2 not found!
fi
