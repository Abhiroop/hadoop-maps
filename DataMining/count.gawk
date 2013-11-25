#!/usr/bin/awk -f

BEGIN       {
            recno = 1;
           
            }
/Data Value/{
            recno++;
            print recno;
            }
            

