#/bin/bash
name=`basename $0`
usage="Usage: $name [keyword list] logfile"
usagef="Usage: $name -f KeywordFile logfie"
if [ $# -lt 2 ] ;then
	echo $usage
	echo $usagef
	exit 1
fi
if [ -f ${!#} ];then	#can not use ${$#}
	#echo Processing...
	#generate keywordlist and script
	output=''
	script=''
	keywordlist=()
	case $1 in
	-f)
		if [ $# -ne 3 ] ;then
			echo $usagef
			exit 1
		fi
		if [ ! -f $2 ] ;then
			echo "file [$2] can not found!"
			exit 1
		fi
		while read word #keywordlist kept unchanged when using pipe
		do
			keywordlist[${#keywordlist[@]}]=${word}
		done < $2 ;;
	*)
		#echo $@
		keywordlist=( $@ )
		unset keywordlist[${#keywordlist[@]}-1];;
	esac
	#echo $output
	#echo ${keywordlist[*]}
	for (( i=0;i<${#keywordlist[@]};i++ )); do
		#output=$output${!i}
		script=$script\/${keywordlist[i]}\/p\;
		script=$script\/${keywordlist[i]}\/b\;
	done
	script=\{$script\}
	#echo $script
	sed -n -e "$script" ${!#}
else
	echo $2 not found!
fi
