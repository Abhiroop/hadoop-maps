<?php
$filename='/var/www/SortedEvent.txt';
while (!file_exists($filename)) sleep(1);
$file = fopen("/var/www/SortedEvent.txt", "r") or exit("Unable to open file!");
$a =isset($_POST['text'])?$_POST['text']:'not yet';
$k=fgets($file);
$pieces = explode("\t", $k);
//echo $pieces[0];
$comm='/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar -mapper "/usr/bin/python /var/www/DataMining/AnalysisByEvent/City_list_mapper.py '.$pieces[0].' '.$a.'" -reducer "/usr/bin/python /var/www/DataMining/AnalysisByEvent/CityList_reducer.py" -input /user/hduser/dataset/final_eval.txt -output /user/hduser/dataset-outputCountry_event';
$mys=exec($comm);
$comm1='/usr/local/hadoop/bin/hadoop dfs -copyToLocal /user/hduser/dataset-outputCountry_event/part-00000 /var/www/leadCountry.txt';
$comm2='sort -r -nk2 leadCountry.txt > sortedleadCountry.txt';
$comm3='/usr/bin/python /var/www/refinecity.py > cleanedsortedcities.txt';
$comm4='head -6 cleanedsortedcities.txt';
$comm5='/usr/bin/python /var/www/geojsoncreatorcities.py';
$mys1=exec($comm1);
$mys2=exec($comm2);
$mys3=exec($comm3);
$mys4=shell_exec($comm4);
$mys5=exec($comm5);
echo $mys4;
fclose($file);
/*
$coco=exec('/usr/local/hadoop/bin/hadoop dfs -rmr /user/hduser/dataset-out*');
$coco1=exec('rm -rf /var/www/*.txt');
*/
?>