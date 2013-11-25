<?php
   //sleep(4);
   $a =isset($_POST['text'])?$_POST['text']:'not yet';
   $command='/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar -mapper "/usr/bin/python /var/www/DataMining/AnalysisByYear/gen_leading_countries_mapper.py '.$a.'" -reducer "/usr/bin/python /var/www/DataMining/AnalysisByYear/gen_leading_countries_reducer.py" -input /user/hduser/dataset/final_eval.txt -output /user/hduser/dataset-outputyearinter';
   $mystring = exec($command);
   //sleep(5);
   $command2='/usr/local/hadoop/bin/hadoop dfs -copyToLocal /user/hduser/dataset-outputyearinter/part-00000 /var/www/DataMining/AnalysisByYear/country_stats.txt';
   $mystring1 = exec($command2);
   $command3='/usr/bin/python /var/www/DataMining/AnalysisByYear/gen_country_stats.py > /var/www/DataMining/AnalysisByYear/abcd.txt';
   $mystring3 = exec($command3);
   $test='/usr/bin/python /var/www/DataMining/AnalysisByYear/geojsoncreator.py';
   $tester=exec($test);
   $string=shell_exec('head -4 /var/www/DataMining/AnalysisByYear/abcd.txt');
   echo $string;
   /*
   $coco=exec('/usr/local/hadoop/bin/hadoop dfs -rmr /user/hduser/dataset-out*');
   $coco1=exec('rm -rf /var/www/*.txt');
   */
   ?>