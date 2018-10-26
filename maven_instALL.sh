for dir in */ ; do 
	#echo "  $dir";
	cd "$dir";
	for dir2 in */ ; do
		if [ "$dir2" != "*/" ] && [ "$dir2" != "src/" ] && [ "$dir2" != "target/" ]; then
			#echo "    $dir2"; 
			cd "$dir2"; 
			mvn install;
			cd ../;
		fi 
	done; 
	mvn install;	
	cd ../; 
done;

for dir in */ ; do 
	#echo "  $dir";
	cd "$dir";
	for dir2 in */ ; do
		if [ "$dir2" != "*/" ] && [ "$dir2" != "src/" ] && [ "$dir2" != "target/" ]; then
			#echo "    $dir2"; 
			cd "$dir2"; 
			mvn build;
			cd ../;
		fi 
	done; 
	mvn build;	
	cd ../; 
done;