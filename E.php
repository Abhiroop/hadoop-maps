<?php
   $a =isset($_POST['text'])?$_POST['text']:'not yet';
   $comm='/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar -mapper "/usr/bin/python /var/www/DataMining/AnalysisByCountry/Country_mapper.py '.$a.'" -reducer "/usr/bin/python /var/www/DataMining/AnalysisByCountry/Country_reducer.py" -input /user/hduser/dataset/final_eval.txt -output /user/hduser/dataset-outputCountry';
   $mys=exec($comm);
   $comm1='/usr/local/hadoop/bin/hadoop dfs -copyToLocal /user/hduser/dataset-outputCountry/part-00000 /var/www/selectedcountry.txt';
   $mys1=exec($comm1);
   //sleep(5);
   $file = '/var/www/selectedcountry.txt';
   $contents = file($file); 
   $string = implode($contents);
   echo $string;
   ?>