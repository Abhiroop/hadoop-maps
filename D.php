<?php
   //sleep(4);
   $a =isset($_POST['text'])?$_POST['text']:'not yet'; 
   $comm='/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar -mapper "/usr/bin/python /var/www/DataMining/AnalysisByCountry/City_find_mapper.py '.$a.'" -reducer "/usr/bin/python /var/www/DataMining/AnalysisByCountry/City_find_reducer.py" -input /user/hduser/dataset/final_eval.txt -output /user/hduser/dataset-outputCountry_city';
   $mys=exec($comm);
   $comm1='/usr/local/hadoop/bin/hadoop dfs -copyToLocal /user/hduser/dataset-outputCountry_city/part-00000 /var/www/leadCountry_city.txt';
   $mys1=exec($comm1);
   $comm2=exec('sort -r -nk2 leadCountry_city.txt > sortedleadCountry_city.txt');
   $comm3=exec('/usr/bin/python /var/www/refine.py > cleanedsortedevent.txt');
   $comm4=shell_exec('head -6 cleanedsortedevent.txt');
   $comm5=exec('/usr/bin/python /var/www/geojsoncretor_country.py');
   echo $comm4;
   /*
   $coco=exec('/usr/local/hadoop/bin/hadoop dfs -rmr /user/hduser/dataset-out*');
   $coco1=exec('rm -rf /var/www/*.txt');
   */
   ?>