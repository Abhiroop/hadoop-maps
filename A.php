<?php
   $a =isset($_POST['text'])?$_POST['text']:'not yet'; 
   $comm='/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar -mapper "/usr/bin/python /var/www/DataMining/AnalysisByEvent/Event_mapper.py '.$a.'" -reducer "/usr/bin/python /var/www/DataMining/AnalysisByEvent/Event_reducer.py" -input /user/hduser/dataset/final_eval.txt -output /user/hduser/dataset-outputEvent';
   $mys=exec($comm);
   $comm1='/usr/local/hadoop/bin/hadoop dfs -copyToLocal /user/hduser/dataset-outputEvent/part-00000 /var/www/EventleadCountries.txt';
   $mys1=exec($comm1);
   $comm2='sort -r -nk2 /var/www/EventleadCountries.txt > /var/www/SortedEvent.txt';
   $mys2=exec($comm2);
   //sleep(5);
   $mys3=shell_exec('head -10 /var/www/SortedEvent.txt');
   echo $mys3;
   ?>