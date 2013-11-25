<?php
   $a =isset($_POST['text'])?$_POST['text']:'not yet';
/*
   echo $a ;
   $my_file = 'file.txt';
   $handle = fopen($my_file, 'w') or die('Cannot open file:  '.$my_file);

   fwrite($handle, $a);
*/   
   $comm='/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar -mapper "/usr/bin/python /var/www/DataMining/AnalysisByYear/AnalysisByYear_mapper.py '.$a.'" -reducer "/usr/bin/python /var/www/DataMining/AnalysisByYear/AnalysisByYear_reducer.py" -input /user/hduser/dataset/final_eval.txt -output /user/hduser/dataset-outputyear';
   $mys=exec($comm);
   $comm1='/usr/local/hadoop/bin/hadoop dfs -copyToLocal /user/hduser/dataset-outputyear/part-00000 /var/www/year.txt';
   $mys1=exec($comm1);
   //sleep(5);
   $file = '/var/www/year.txt';
   $contents = file($file); 
   $string = implode($contents);
   echo $string;
   ?>